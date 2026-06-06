# Labs

> Exercícios práticos executáveis por capítulo da obra *Deep Claude*.

---

## Por que esta pasta existe

Capítulos densos sem laboratório de prática viram conhecimento conceitual sem operacionalização. Esta pasta carrega exercícios práticos por capítulo, com código executável, datasets de exemplo e scripts de validação, para que o leitor saia da leitura com mão na massa.

Cada lab é autossuficiente: instruções em README próprio, dependências declaradas, código rodável em ambiente local ou notebook.

---

## Estrutura por lab

Cada lab segue a estrutura:

```
labs/cap-XX-nome-do-lab/
  README.md         — objetivo, pré-requisitos, instruções
  requirements.txt  — dependências Python (ou package.json para Node)
  exemplo.py        — código executável
  dataset/          — dados de exemplo
  outputs/          — esperado depois da execução (gitignored)
```

---

## Cobertura inicial — v1.0 (jul/2026)

| Capítulo | Lab | Status |
|---|---|---|
| Cap 9 — Claude Code | `cap-09-claude-code-tour` | Planejado |
| Cap 21 — API + SDKs | `cap-21-api-primeira-chamada` | Planejado |
| Cap 30 — Claude Skills | `cap-30-construir-skill-do-zero` | Planejado |

---

## Cobertura roadmap

### v1.1 — out/2026

| Capítulo | Lab |
|---|---|
| Cap 22 — Tool Use | `cap-22-tool-use-pratico` |
| Cap 23 — Extended Thinking | `cap-23-thinking-budget` |
| Cap 27 — RAG | `cap-27-rag-com-voyage` |
| Cap 28 — MCP Fundamentos | `cap-28-mcp-hello-world` |
| Cap 29 — MCP Avançado | `cap-29-mcp-com-claude-code` |
| Cap 31 — Subagents | `cap-31-orquestrador-especialistas` |

### v1.2 — jan/2027

| Capítulo | Lab |
|---|---|
| Cap 32 — Computer Use | `cap-32-computer-use-pratico` |
| Cap 33 — Vision | `cap-33-vision-multimodal` |
| Cap 34 — Evaluations | `cap-34-eval-runner-completo` |
| Cap 35 — LLMOps | `cap-35-observabilidade-end-to-end` |

---

## Pré-requisitos gerais

| Requisito | Comentário |
|---|---|
| Python 3.10+ | Para a maioria dos labs |
| Node 20+ | Para labs envolvendo Claude Agent SDK em TS |
| Conta Anthropic | Com API Key (Cap 21 do livro) |
| Git | Para clonar e contribuir |

Cada lab declara suas dependências específicas no `requirements.txt` ou `package.json` próprio.

---

## Princípios dos labs

**Executável em 15 minutos.** Cada lab deve rodar do zero em até 15 minutos, considerando setup. Labs que exigem mais tempo são divididos em etapas independentes.

**Sem custo desnecessário.** Labs usam tier econômico (Haiku) por padrão. Quando precisam de Opus ou Sonnet, o README avisa e oferece versão simplificada com Haiku.

**Validação automática.** Cada lab tem `validate.py` que confirma que o output esperado foi gerado. Sem validação, lab não está pronto.

**Documentação no código.** Comentários generosos no código explicam a intenção, não a sintaxe. Leitor entende o porquê de cada decisão.

---

## Como contribuir com novo lab

1. Abra issue com label `novo-lab` e a proposta
2. Aguarde alinhamento (até 7 dias)
3. Abra PR com a estrutura completa (README + código + dataset + validate)
4. Lab passa por revisão funcional e editorial
5. Após merge, lab é incorporado ao changelog datado

Veja [CONTRATO.md](../CONTRATO.md) para princípios completos.

---

## Capítulos relacionados

Todos os labs amarram com capítulos específicos da obra:

- **Caps 9, 21, 22, 23**: API e desenvolvimento Claude Code
- **Caps 27, 28, 29**: RAG e MCP
- **Caps 30, 31**: Skills e Subagents
- **Caps 32, 33**: Computer Use e Vision
- **Caps 34, 35**: Evaluations e LLMOps

Sem ler o capítulo do livro, o lab vira receita sem fundamento. Leia primeiro, rode depois.
