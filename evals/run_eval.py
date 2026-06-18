#!/usr/bin/env python3
"""
run_eval.py — Harness de eval executável para o repo Deep Claude.

Uso básico:
    python run_eval.py ../prompts/P-LEG-CLAUDE-01/golden_set.yaml
    python run_eval.py ../prompts/P-LEG-CLAUDE-01/golden_set.yaml --dry-run

Lógica:
    1. Lê o golden_set.yaml e o prompt.xml da mesma pasta.
    2. Para cada caso, monta o prompt substituindo os placeholders do XML.
    3. Chama a API Anthropic para obter a resposta (modelo-alvo).
    4. Avalia cada critério_aceitacao via LLM-as-judge (segunda chamada).
    5. Imprime tabela de PASS/FAIL por caso e taxa global de cobertura.

Modo --dry-run:
    Valida o YAML, monta os prompts e imprime o plano — sem chamar a API.
    Útil em CI, revisão editorial, e para testar sem chave disponível.

Capítulo de referência: Cap 34 do livro (evals offline + LLM-as-judge).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Configuração de modelo
# ---------------------------------------------------------------------------
# Altere as constantes abaixo conforme a geração corrente.
# IDs com data garantem reprodutibilidade em produção (sem drift comportamental).
# Referência canônica: apendice-vivo/MODELOS.md
#
# Modelo-alvo: executa o prompt sob avaliação.
MODELO_ALVO = os.environ.get("EVAL_MODEL_ALVO", "claude-sonnet-4-5-20251022")
#
# Modelo-juiz: avalia a resposta do modelo-alvo contra os critérios.
# Pode ser o mesmo ou diferente do modelo-alvo.
# Sonnet é suficiente para julgamento estruturado (JSON puro).
MODELO_JUIZ = os.environ.get("EVAL_MODEL_JUIZ", "claude-sonnet-4-5-20251022")

# Tokens máximos para a resposta do modelo-alvo (ajuste por domínio)
MAX_TOKENS_ALVO = int(os.environ.get("EVAL_MAX_TOKENS_ALVO", "4096"))

# Tokens máximos para o juiz (JSON pequeno — não precisa de muito)
MAX_TOKENS_JUIZ = int(os.environ.get("EVAL_MAX_TOKENS_JUIZ", "1024"))

# ---------------------------------------------------------------------------
# Helpers de leitura de arquivos
# ---------------------------------------------------------------------------


def carregar_golden_set(caminho: Path) -> dict:
    """Lê e valida o golden_set.yaml. Lança exceção com mensagem clara se inválido."""
    with open(caminho, encoding="utf-8") as f:
        dados = yaml.safe_load(f)

    if not isinstance(dados, dict):
        raise ValueError(f"golden_set.yaml inválido: raiz deve ser um dicionário. ({caminho})")
    if "casos" not in dados or not isinstance(dados["casos"], list):
        raise ValueError(f"golden_set.yaml inválido: faltando chave 'casos' como lista. ({caminho})")
    if not dados["casos"]:
        raise ValueError(f"golden_set.yaml inválido: lista 'casos' está vazia. ({caminho})")

    return dados


def carregar_prompt_xml(pasta_prompt: Path) -> str:
    """Carrega o prompt.xml da mesma pasta do golden_set."""
    caminho = pasta_prompt / "prompt.xml"
    if not caminho.exists():
        raise FileNotFoundError(f"prompt.xml não encontrado em: {pasta_prompt}")
    return caminho.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Montagem do prompt para cada caso
# ---------------------------------------------------------------------------


def _extrair_system_prompt(xml: str) -> str:
    """
    Extrai o conteúdo útil do XML para usar como system prompt.
    Mantém o XML completo — Claude lida bem com estrutura XML como instrução.
    """
    return xml.strip()


def montar_prompt_usuario(caso: dict, xml: str) -> tuple:
    """
    Retorna (system_prompt, mensagem_usuario) montados para o caso.

    Estratégia de substituição de placeholders:
    - O prompt.xml usa {{variavel}} como marcadores no bloco <contexto>.
    - Para cada caso, preenchemos com os valores de caso['contexto'] quando disponíveis.
    - O 'input' do caso vira o corpo da mensagem do usuário.

    Se o caso não tem campo 'input', monta mensagem sintética a partir do contexto
    para permitir o dry-run mesmo em golden sets incompletos.
    """
    system_prompt = _extrair_system_prompt(xml)

    # Substituição de placeholders {{chave}} pelo contexto do caso
    contexto = caso.get("contexto", {})
    prompt_preenchido = system_prompt

    if contexto:
        for chave, valor in contexto.items():
            placeholder = "{{" + chave + "}}"
            prompt_preenchido = prompt_preenchido.replace(placeholder, str(valor))
        # Remove placeholders não substituídos (deixa o nome sem chaves para não quebrar o XML)
        prompt_preenchido = re.sub(r"\{\{[^}]+\}\}", "[nao especificado]", prompt_preenchido)

    # Monta mensagem do usuário
    input_caso = caso.get("input")
    if input_caso is None:
        # Caso sem campo 'input': monta mensagem sintética a partir do contexto e descrição
        descricao = caso.get("descricao", "Caso sem descricao")
        partes = ["Analisar: " + descricao]
        if contexto:
            for k, v in contexto.items():
                partes.append("- " + str(k) + ": " + str(v))
        mensagem_usuario = "\n".join(partes)
        mensagem_usuario += "\n\n[NOTA: input sintetico gerado pelo harness — caso sem campo 'input' explicito]"
    elif isinstance(input_caso, dict):
        # Campo 'input' é um dicionário (estruturado) — serializa legível
        linhas = ["Analisar o seguinte contrato/documento:"]
        for k, v in input_caso.items():
            if isinstance(v, list):
                linhas.append("- " + str(k) + ":")
                for item in v:
                    linhas.append("    * " + str(item))
            else:
                linhas.append("- " + str(k) + ": " + str(v))
        mensagem_usuario = "\n".join(linhas)
    else:
        # Campo 'input' é string direta
        mensagem_usuario = str(input_caso)

    return prompt_preenchido, mensagem_usuario


# ---------------------------------------------------------------------------
# Plano de execução (dry-run)
# ---------------------------------------------------------------------------


def imprimir_plano(dados: dict, xml: str, caminho_gs: Path) -> None:
    """Imprime o plano de execução sem chamar a API."""
    prompt_id = dados.get("prompt_id", "desconhecido")
    casos = dados["casos"]

    print("=" * 72)
    print("PLANO DE EXECUCAO — MODO DRY-RUN")
    print("=" * 72)
    print("  Golden set  : " + str(caminho_gs))
    print("  Prompt ID   : " + prompt_id)
    print("  Versao GS   : " + str(dados.get("version", "?")) + "  |  Data: " + str(dados.get("data", "?")))
    print("  Total casos : " + str(len(casos)))
    print("  Modelo-alvo : " + MODELO_ALVO)
    print("  Modelo-juiz : " + MODELO_JUIZ)
    print()

    total_criterios = 0
    for i, caso in enumerate(casos, 1):
        case_id = caso.get("id", "CASE-" + str(i).zfill(3))
        descricao = caso.get("descricao", "sem descricao")
        criterios = caso.get("criterios_aceitacao", [])
        total_criterios += len(criterios)
        tem_input = "input" in caso

        print("  [" + str(i).zfill(2) + "] " + case_id + " — " + descricao)
        print("       Criterios : " + str(len(criterios)))
        print("       Tem input : " + ("sim" if tem_input else "nao (input sintetico sera gerado)"))

        # Mostra prévia do prompt do usuário
        _, msg_usuario = montar_prompt_usuario(caso, xml)
        preview = msg_usuario[:120].replace("\n", " ")
        if len(msg_usuario) > 120:
            preview += "..."
        print("       Preview   : " + preview)
        print()

    print("-" * 72)
    print("  Total de criterios a avaliar: " + str(total_criterios))
    print("  Chamadas API que seriam feitas: " + str(len(casos)) + " (alvo) + " + str(len(casos)) + " (juiz) = " + str(len(casos) * 2))
    print()
    print("  [OK] YAML valido. Estrutura de prompt monta sem erros.")
    print("  [OK] Pronto para rodar sem --dry-run (exige ANTHROPIC_API_KEY).")
    print("=" * 72)


# ---------------------------------------------------------------------------
# Avaliação via LLM-as-judge
# ---------------------------------------------------------------------------


PROMPT_JUIZ_SYSTEM = """Voce e um avaliador rigoroso de outputs de LLM.
Recebera uma RESPOSTA gerada pelo modelo e uma lista de CRITERIOS DE ACEITACAO.
Para cada criterio, julgue se a resposta o atende (PASS) ou nao (FAIL).

Responda APENAS em JSON valido, no formato exato abaixo, sem texto adicional:

{
  "avaliacoes": [
    {"criterio": "<texto exato do criterio>", "resultado": "PASS", "justificativa": "<1 frase>"},
    {"criterio": "<texto exato do criterio>", "resultado": "FAIL", "justificativa": "<1 frase>"}
  ]
}

Regras:
- Seja conservador: so marque PASS se a resposta cumpre claramente o criterio.
- Justificativa deve ser objetiva e baseada em evidencia textual da resposta.
- Nao infira intencao — avalie o que esta escrito.
"""


def avaliar_com_juiz(client, resposta_modelo, criterios):
    """
    Chama o modelo-juiz e retorna lista de avaliações por critério.
    Cada item: {"criterio": str, "resultado": "PASS"|"FAIL", "justificativa": str}
    """
    criterios_formatados = "\n".join("- " + c for c in criterios)
    mensagem = (
        "RESPOSTA DO MODELO:\n\n" + resposta_modelo + "\n\n"
        "CRITERIOS DE ACEITACAO:\n" + criterios_formatados
    )

    resposta_juiz = client.messages.create(
        model=MODELO_JUIZ,
        max_tokens=MAX_TOKENS_JUIZ,
        system=PROMPT_JUIZ_SYSTEM,
        messages=[{"role": "user", "content": mensagem}],
    )

    texto_json = resposta_juiz.content[0].text.strip()

    # Remove blocos de código Markdown se o modelo os adicionar (defensivo)
    if texto_json.startswith("```"):
        texto_json = re.sub(r"^```[a-z]*\n?", "", texto_json)
        texto_json = re.sub(r"\n?```$", "", texto_json)

    try:
        dados_juiz = json.loads(texto_json)
        return dados_juiz.get("avaliacoes", [])
    except json.JSONDecodeError as e:
        # Retorna FAIL para todos os critérios se o JSON vier malformado
        print("    [AVISO] Juiz retornou JSON invalido: " + str(e))
        return [
            {"criterio": c, "resultado": "FAIL", "justificativa": "Juiz retornou JSON invalido"}
            for c in criterios
        ]


# ---------------------------------------------------------------------------
# Execução real (com API)
# ---------------------------------------------------------------------------


def executar_caso(client, caso, xml, indice, total):
    """
    Executa um único caso: chama modelo-alvo, depois juiz.
    Retorna dicionário com resultado completo do caso.
    """
    case_id = caso.get("id", "CASE-" + str(indice).zfill(3))
    descricao = caso.get("descricao", "sem descricao")
    criterios = caso.get("criterios_aceitacao", [])

    print("\n[" + str(indice) + "/" + str(total) + "] " + case_id + " — " + descricao)
    print("  Criterios a avaliar: " + str(len(criterios)))

    # Monta prompts
    system_prompt, mensagem_usuario = montar_prompt_usuario(caso, xml)

    # Chamada ao modelo-alvo
    print("  -> Chamando modelo-alvo (" + MODELO_ALVO + ")...", end=" ", flush=True)
    resposta_alvo = client.messages.create(
        model=MODELO_ALVO,
        max_tokens=MAX_TOKENS_ALVO,
        system=system_prompt,
        messages=[{"role": "user", "content": mensagem_usuario}],
    )
    texto_resposta = resposta_alvo.content[0].text
    tokens_alvo = resposta_alvo.usage.input_tokens + resposta_alvo.usage.output_tokens
    print("OK (" + str(tokens_alvo) + " tokens)")

    # Chamada ao juiz
    print("  -> Avaliando com juiz (" + MODELO_JUIZ + ")...", end=" ", flush=True)
    avaliacoes = avaliar_com_juiz(client, texto_resposta, criterios)
    print("OK")

    # Conta passes
    passes = sum(1 for a in avaliacoes if a.get("resultado") == "PASS")
    taxa = passes / len(criterios) if criterios else 0.0

    # Imprime resultado do caso
    for av in avaliacoes:
        simbolo = "OK" if av.get("resultado") == "PASS" else "XX"
        print("    [" + simbolo + "] " + av.get("resultado", "?") + "  — " + av.get("criterio", "?"))
        if av.get("resultado") == "FAIL":
            print("         Justificativa: " + av.get("justificativa", ""))

    print("  Score: " + str(passes) + "/" + str(len(criterios)) + " (" + str(int(taxa * 100)) + "%)")

    return {
        "case_id": case_id,
        "descricao": descricao,
        "passes": passes,
        "total_criterios": len(criterios),
        "taxa": taxa,
        "avaliacoes": avaliacoes,
        "tokens_alvo": tokens_alvo,
    }


def executar_eval(caminho_gs):
    """Executa o eval completo com chamadas reais à API."""
    # Importa anthropic aqui — não no topo — para que --dry-run funcione sem a lib
    try:
        import anthropic
    except ImportError:
        print(
            "ERRO: biblioteca 'anthropic' nao encontrada.\n"
            "Instale com: pip install -r evals/requirements.txt\n"
            "Ou use --dry-run para testar sem a biblioteca."
        )
        sys.exit(1)

    chave = os.environ.get("ANTHROPIC_API_KEY")
    if not chave:
        print(
            "ERRO: variavel de ambiente ANTHROPIC_API_KEY nao definida.\n"
            "Export com: export ANTHROPIC_API_KEY=sk-ant-...\n"
            "Ou use --dry-run para testar sem chave."
        )
        sys.exit(1)

    client = anthropic.Anthropic(api_key=chave)

    dados = carregar_golden_set(caminho_gs)
    xml = carregar_prompt_xml(caminho_gs.parent)
    casos = dados["casos"]
    prompt_id = dados.get("prompt_id", "desconhecido")

    print("=" * 72)
    print("EVAL — " + prompt_id + "  (" + str(len(casos)) + " casos)")
    print("=" * 72)

    resultados = []
    for i, caso in enumerate(casos, 1):
        resultado = executar_caso(client, caso, xml, i, len(casos))
        resultados.append(resultado)

    # ---------------------------------------------------------------------------
    # Tabela de resumo
    # ---------------------------------------------------------------------------
    total_passes = sum(r["passes"] for r in resultados)
    total_criterios = sum(r["total_criterios"] for r in resultados)
    total_tokens = sum(r["tokens_alvo"] for r in resultados)
    taxa_global = total_passes / total_criterios if total_criterios else 0.0

    print("\n" + "=" * 72)
    print("RESUMO")
    print("=" * 72)
    print("{:<16} {:<40} {}".format("CASE ID", "DESCRICAO", "SCORE"))
    print("-" * 72)
    for r in resultados:
        barra = "#" * int(r["taxa"] * 10) + "." * (10 - int(r["taxa"] * 10))
        linha = "{:<16} {:<40} {}/{} [{}] {}%".format(
            r["case_id"],
            r["descricao"][:40],
            r["passes"],
            r["total_criterios"],
            barra,
            int(r["taxa"] * 100),
        )
        print(linha)

    print("-" * 72)
    barra_global = "#" * int(taxa_global * 10) + "." * (10 - int(taxa_global * 10))
    print("{:<16} {:<40} {}/{} [{}] {}%".format(
        "TOTAL", "", total_passes, total_criterios, barra_global, int(taxa_global * 100)
    ))
    print()
    print("  Tokens consumidos (alvo): " + str(total_tokens))
    print("  Modelo-alvo : " + MODELO_ALVO)
    print("  Modelo-juiz : " + MODELO_JUIZ)

    # Limiar de produção (padrão 85%; golden sets individuais podem declarar o seu)
    limiar = 0.85
    status = "APROVADO" if taxa_global >= limiar else "REPROVADO"
    print("\n  Limiar de producao : " + str(int(limiar * 100)) + "%")
    print("  Resultado          : " + status + " (" + str(round(taxa_global * 100, 1)) + "%)")
    print("=" * 72)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Harness de eval para prompts do repo Deep Claude.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Dry-run (sem API, valida estrutura e imprime plano):
  python evals/run_eval.py prompts/P-LEG-CLAUDE-01/golden_set.yaml --dry-run

  # Execucao real (exige ANTHROPIC_API_KEY):
  python evals/run_eval.py prompts/P-LEG-CLAUDE-01/golden_set.yaml

  # Modelo customizado via variavel de ambiente:
  EVAL_MODEL_ALVO=claude-opus-4-20260401 python evals/run_eval.py prompts/P-LEG-CLAUDE-01/golden_set.yaml

Referencia: Cap 34 do livro Deep Claude (evals offline + LLM-as-judge).
""",
    )
    parser.add_argument(
        "golden_set",
        type=Path,
        help="Caminho para o golden_set.yaml do prompt a avaliar.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Valida o YAML e imprime o plano sem chamar a API.",
    )

    args = parser.parse_args()

    caminho_gs = args.golden_set.resolve()
    if not caminho_gs.exists():
        print("ERRO: arquivo nao encontrado: " + str(caminho_gs))
        sys.exit(1)

    # Carrega e valida golden set (sempre, mesmo em dry-run)
    try:
        dados = carregar_golden_set(caminho_gs)
    except (ValueError,) as e:
        print("ERRO no golden_set.yaml: " + str(e))
        sys.exit(1)

    # Carrega prompt.xml (sempre)
    try:
        xml = carregar_prompt_xml(caminho_gs.parent)
    except FileNotFoundError as e:
        print("ERRO: " + str(e))
        sys.exit(1)

    if args.dry_run:
        imprimir_plano(dados, xml, caminho_gs)
    else:
        executar_eval(caminho_gs)


if __name__ == "__main__":
    main()
