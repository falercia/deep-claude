# evals/ — Harness de Eval Executável

Runner mínimo para validar prompts do repo `deep-claude` contra seus golden sets.
Conecta diretamente às pastas `prompts/*/`, lê o `golden_set.yaml` e o `prompt.xml`,
e executa dois estágios de chamada à API Anthropic:

1. **Modelo-alvo** — executa o prompt do caso de teste.
2. **LLM-as-judge** — avalia a resposta contra os `criterios_aceitacao` e devolve PASS/FAIL em JSON.

---

## Instalação

```bash
pip install -r evals/requirements.txt
```

---

## Configuração

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

Os modelos usados têm padrão razoável, mas podem ser sobrescritos por variável de ambiente:

```bash
# Modelo que executa o prompt (modelo-alvo)
export EVAL_MODEL_ALVO=claude-sonnet-4-5-20251022

# Modelo que julga a resposta (LLM-as-judge)
export EVAL_MODEL_JUIZ=claude-sonnet-4-5-20251022
```

Referência canônica dos modelos disponíveis: `apendice-vivo/MODELOS.md`.

---

## Como rodar

### Dry-run (sem chave de API)

Valida o YAML, monta todos os prompts e imprime o plano de execução sem chamar a API.
Útil para CI, revisão editorial, e verificação de estrutura:

```bash
python evals/run_eval.py prompts/P-LEG-CLAUDE-01/golden_set.yaml --dry-run
python evals/run_eval.py prompts/P-FIN-CLAUDE-01/golden_set.yaml --dry-run
python evals/run_eval.py prompts/P-MED-CLAUDE-01/golden_set.yaml --dry-run
```

### Execução real

```bash
python evals/run_eval.py prompts/P-LEG-CLAUDE-01/golden_set.yaml
python evals/run_eval.py prompts/P-FIN-CLAUDE-01/golden_set.yaml
```

O runner imprime uma tabela de PASS/FAIL por caso e a taxa global de cobertura ao final.
O limiar padrão de aprovação para produção é **85%** (configurável no código).

---

## O que é LLM-as-judge — e seus vieses

**Conceito.** Em vez de comparar a saída do modelo com uma string de referência exata (frágil),
um segundo LLM recebe a resposta gerada + a lista de critérios e devolve PASS/FAIL com justificativa
para cada critério. Isso permite avaliar propriedades qualitativas ("tom executivo", "não diagnostica")
que não têm gabarito de string fixo.

O Cap 34 do livro detalha o processo completo. Aqui o resumo dos vieses que o leitor precisa conhecer:

| Viés | Descrição | Mitigação |
|---|---|---|
| **Preferência por prolixidade** | Juízes LLM tendem a marcar PASS em respostas longas mesmo quando o conteúdo é vago | Critérios devem ser específicos ("cita Art. 7 LGPD", não "aborda LGPD") |
| **Viés de posição** | O juiz pode favorecer o início da resposta; critérios sobre disclaimer (no final) podem ser subavaliados | Rodar com critérios em ordem aleatória; validar amostra manualmente |
| **Auto-favorecimento** | Se o modelo-juiz for o mesmo do modelo-alvo, há tendência de marcar PASS em outputs que se parecem com seu próprio estilo | Usar modelos distintos para alvo e juiz quando possível (`EVAL_MODEL_JUIZ`) |
| **Falta de conhecimento jurídico** | O juiz pode marcar PASS em referências legais incorretas que soam plausíveis | Golden sets com critérios verificáveis por humano; "analista-no-loop" em casos críticos |
| **Calibração de limiar** | 85% no golden set não equivale a 85% de qualidade no tráfego real — o golden set pode não cobrir edge cases de produção | Expandir o golden set periodicamente com casos reais anonimizados |

**Recomendação editorial (Cap 34):** LLM-as-judge é excelente para iteração rápida de prompt engineering.
Para decisões de lançamento em produção, combine com revisão humana de amostra (mínimo 20% dos casos de maior criticidade).

---

## Estrutura dos arquivos

```
evals/
  run_eval.py       # runner principal
  requirements.txt  # anthropic, pyyaml
  README.md         # este arquivo
```

Cada pasta de prompt segue o padrão:

```
prompts/P-XXX-CLAUDE-01/
  prompt.xml          # system prompt com placeholders {{variavel}}
  golden_set.yaml     # casos de teste com criterios_aceitacao
  README.md           # documentação do prompt
  changelog.md        # histórico de versões
```

---

## Adicionando novos casos ao golden set

Um caso mínimo válido:

```yaml
- id: "CASE-013"
  descricao: "Descrição curta do cenário"
  contexto:
    setor: "SaaS"
    jurisdicao: "Brasil"
    relacao: "B2B"
    criticidade: "medio"
  input:
    tipo: "Tipo do documento"
    # texto_exemplo é opcional mas recomendado para demonstração:
    texto_exemplo: |
      [EXEMPLO ILUSTRATIVO — FICTÍCIO]
      Conteúdo do contrato de exemplo...
  criterios_aceitacao:
    - "Critério verificável e específico"
    - "Outro critério sem ambiguidade"
```

Campos `texto_exemplo` e `output_esperado` são opcionais mas tornam o harness mais
demonstrativo e facilitam a revisão humana. Ver CASE-001 e CASE-002 do `P-LEG-CLAUDE-01`
como exemplo.

---

## Referências no livro

- **Cap 21** — Primeira chamada à API (padrão de código Python do repo)
- **Cap 24** — Engenharia de prompt com XML
- **Cap 34** — Evals offline: golden sets, LLM-as-judge, limiar de produção
- **Cap 44** — Segurança e compliance: o que não avaliar com LLM puro
