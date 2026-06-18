# Modelos — Snapshot

> **Snapshot 2026-06-18 · rascunho para conferência do autor**
> Atualizado em: 2026-06-18 (populamento com dados correntes — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-06-06 (seed inicial)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Famílias rastreadas

| Família | Fornecedor | Tier alto | Tier médio | Tier baixo | Open weights |
|---|---|---|---|---|---|
| **Claude** | Anthropic | Opus / Fable | Sonnet | Haiku | Não |
| **GPT** | OpenAI | GPT-5.5 | GPT-4.1 | GPT-4.1 mini/nano | Não |
| **Gemini** | Google DeepMind | Gemini 2.5 Pro / 3.1 Pro Preview | Gemini 2.5 Flash | Gemini 2.5 Flash-Lite | Não (varia) |
| **Llama** | Meta | 405B+ | 70B | 8B | Sim |
| **Mistral** | Mistral AI | Large | Medium | Small | Parcial |
| **Qwen** | Alibaba | Max | Plus | Turbo | Sim |
| **DeepSeek** | DeepSeek | R-series | V-series | — | Sim |

---

## Claude — geração 4.x e além (Anthropic)

Anthropic mantém múltiplas gerações ativas. Em junho/2026, a linha principal é a geração 4.x,
com dois modelos de tier superior lançados recentemente (Fable 5 e Mythos 5).

### Modelos correntes (junho 2026)

| Modelo | API ID (Claude API) | Posicionamento | Janela de contexto |
|---|---|---|---|
| **Claude Fable 5** | `claude-fable-5` | Mais capaz em ampla disponibilidade; raciocínio e trabalho agêntico de longa duração | 1M tokens |
| **Claude Mythos 5** | `claude-mythos-5` | Disponibilidade limitada (Project Glasswing) | 1M tokens |
| **Claude Opus 4.8** | `claude-opus-4-8` | Mais capaz do tier Opus; raciocínio complexo, coding agêntico | 1M tokens (200K no Microsoft Foundry) |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | Melhor equilíbrio velocidade/inteligência | 1M tokens |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251001` / alias `claude-haiku-4-5` | Modelo mais rápido com inteligência próxima ao frontier | 200K tokens |

· fonte: https://platform.claude.com/docs/en/about-claude/models/overview · data: 2026-06-18

**Nota sobre Claude Fable 5 e Mythos 5.** Lançados em 09/06/2026. Fable 5 está disponível via Claude API, Claude Platform on AWS, Amazon Bedrock, Vertex AI e Microsoft Foundry. Mythos 5 tem acesso restrito via Project Glasswing (aprovação necessária).

**Mecânica de versionamento.** A partir da geração 4.6, os IDs de modelo usam formato sem data (ex.: `claude-sonnet-4-6`) que é snapshot fixo, não ponteiro dinâmico. Modelos anteriores à geração 4.6 usam data explícita (ex.: `claude-haiku-4-5-20251001`). Aliases convenientes (ex.: `claude-haiku-4-5`) apontam para a revisão corrente — conveniente para desenvolvimento, perigoso em produção sem teste de regressão.

---

## GPT — geração corrente (OpenAI)

### Modelos correntes (junho 2026)

| Modelo | Posicionamento | Observação |
|---|---|---|
| **GPT-5.5** | Flagship; raciocínio complexo, coding, agentes | Lançado em 24/04/2026 |
| **GPT-5.5 Pro** | Tier máximo; raciocínio de alta estaca | Premium sobre GPT-5.5 |
| **GPT-4.1** | Não-raciocínio mais capaz; 1M contexto | Concorrente direto de Sonnet |
| **GPT-4.1 mini** | Velocidade/custo balanceados | Concorrente direto de Haiku |
| **GPT-4.1 nano** | Mínimo custo/latência | Casos de uso de ultra-baixo custo |
| **o3** | Raciocínio matemático e científico | Substitui o1; disponível via Chat Completions e Responses API |

· fonte: https://developers.openai.com/api/docs/models/all · data: 2026-06-18

**Nota sobre GPT-4o.** Descontinuado no ChatGPT em 13/02/2026; continua disponível via API.

---

## Gemini — geração corrente (Google DeepMind)

### Modelos correntes (junho 2026)

| Modelo | API ID | Posicionamento | Janela de contexto |
|---|---|---|---|
| **Gemini 3.1 Pro Preview** | `gemini-3.1-pro-preview` | Mais capaz; multimodal, agêntico, vibe-coding | TBD (a confirmar) |
| **Gemini 2.5 Pro** | `gemini-2.5-pro` | Raciocínio complexo e coding; stable release | 1M tokens |
| **Gemini 2.5 Flash** | `gemini-2.5-flash` | Raciocínio híbrido; velocidade + thinking budgets | 1M tokens |
| **Gemini 2.5 Flash-Lite** | `gemini-2.5-flash-lite` | Menor custo e mais eficiente; alto volume | TBD (a confirmar) |

· fonte: https://ai.google.dev/gemini-api/docs/pricing · data: 2026-06-18

---

## Modelos open-source relevantes

Para CTOs avaliando alternativas com soberania total de dados, modelos abertos com pesos disponíveis são opção. Lista atualizada:

| Modelo | Tamanho | Forte em |
|---|---|---|
| Llama (Meta) | 8B, 70B, 405B+ | Generalista, multilingue |
| Mistral | 7B-Large | Eficiência |
| Qwen (Alibaba) | 7B-72B | Multilingue, código |
| DeepSeek | 67B+ | Raciocínio, matemática |

---

## Mudanças recentes

- **2026-06-18**: snapshot populado com dados correntes — modelos identificados com API IDs e janelas de contexto confirmadas por fonte primária (Anthropic docs, Google AI pricing).
- **2026-06-09**: Anthropic lança Claude Fable 5 (disponibilidade ampla) e Claude Mythos 5 (Project Glasswing, acesso limitado).
- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**Como contribuir.** Observou modelo lançado ou mudança não capturada? Abra issue com label `errata` ou `nova-fonte`. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

- Anthropic Models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- OpenAI Models: https://developers.openai.com/api/docs/models/all
- Google Gemini Models: https://ai.google.dev/gemini-api/docs/models
- Google Gemini Pricing: https://ai.google.dev/gemini-api/docs/pricing

Ver [`FONTES.md`](./FONTES.md) para lista completa com links de docs oficiais.
