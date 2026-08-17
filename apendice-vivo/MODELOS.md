# Modelos — Snapshot

> **Snapshot 2026-08-12**
> Atualizado em: 2026-08-12 (Opus 5, Sonnet 5, família GPT-5.6, timeline Fable 5, watermarking — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-06-18
> Próxima atualização: setembro/2026 (checagem mensal)
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Famílias rastreadas

| Família | Fornecedor | Tier alto | Tier médio | Tier baixo | Open weights |
|---|---|---|---|---|---|
| **Claude** | Anthropic | Fable/Mythos (fronteira) / Opus | Sonnet | Haiku | Não |
| **GPT** | OpenAI | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna | Não |
| **Gemini** | Google DeepMind | Gemini 3.1 Pro | Gemini Flash (família 3.x) | Gemini Flash-Lite | Não (varia) |
| **Llama** | Meta | 405B+ | 70B | 8B | Sim |
| **Mistral** | Mistral AI | Large | Medium | Small | Parcial |
| **Qwen** | Alibaba | Max | Plus | Turbo | Sim |
| **DeepSeek** | DeepSeek | R-series | V-series | — | Sim |

---

## Claude — geração 4.x/5 e classe Mythos (Anthropic)

Anthropic mantém múltiplas gerações ativas. Em agosto/2026, a estrutura tem três camadas: a classe de fronteira Mythos (Fable 5 / Mythos 5) acima do trio de trabalho, o tier Opus (Opus 5 como topo desde 24/07) e os tiers Sonnet/Haiku.

### Modelos correntes (agosto 2026)

| Modelo | API ID (Claude API) | Posicionamento | Janela de contexto |
|---|---|---|---|
| **Claude Fable 5** | `claude-fable-5` | Fronteira em ampla disponibilidade; raciocínio e trabalho agêntico de longa duração | 1M tokens |
| **Claude Mythos 5** | `claude-mythos-5` | Mesmo modelo do Fable, salvaguardas de cyber removidas; restrito (Project Glasswing) | 1M tokens |
| **Claude Opus 5** | `claude-opus-5` | Topo do tier Opus (GA 24/07/2026); default do plano Max; recebe fallback de biologia do Fable 5 | 1M tokens |
| **Claude Opus 4.8** | `claude-opus-4-8` | Tier Opus da geração anterior; recebe fallback de cyber do Fable 5 | 1M tokens (200K no Microsoft Foundry) |
| **Claude Sonnet 5** | `claude-sonnet-5` | Cavalo de batalha de produção; default de Free e Pro | 1M tokens |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | Geração anterior do tier balanceado, ainda ativa | 1M tokens |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251001` / alias `claude-haiku-4-5` | Modelo mais rápido; volume e latência | 200K tokens |

· fonte: https://platform.claude.com/docs/en/about-claude/models/overview · data: 2026-08-12

**Nota sobre Claude Fable 5 e Mythos 5.** Lançados em 09/06/2026. Timeline do Fable 5: controles de exportação dos EUA suspenderam o acesso global de 12 a 30/06; redeploy mundial em 01/07; migração para usage credits nos planos pagos em 07/07. Requisições sensíveis sofrem fallback automático: cibersegurança → Opus 4.8; biologia dual-use (virologia, toxicologia, design molecular) → Opus 5. Em 07/08/2026, a Anthropic recalibrou o classificador de biologia, reduzindo fallbacks de biologia em ~85% — salvaguarda é parâmetro vivo, muda sem release de modelo. Mythos 5 tem acesso restrito via Project Glasswing (aprovação necessária).

**Marcação de conteúdo (watermarking).** Modelos Claude lançados a partir de 02/08/2026 embutem watermark estatístico imperceptível no texto gerado e metadados de proveniência C2PA em arquivos suportados, em todas as superfícies, mundialmente (compromisso sob o Artigo 50(2) do EU AI Act, anunciado em 11/08/2026). A marca prova processamento, não autoria. Fonte: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content

**Mecânica de versionamento.** A partir da geração 4.6, os IDs de modelo usam formato sem data (ex.: `claude-sonnet-4-6`) que é snapshot fixo, não ponteiro dinâmico. Modelos anteriores à geração 4.6 usam data explícita (ex.: `claude-haiku-4-5-20251001`). Aliases convenientes (ex.: `claude-haiku-4-5`) apontam para a revisão corrente — conveniente para desenvolvimento, perigoso em produção sem teste de regressão.

---

## GPT — geração corrente (OpenAI)

### Modelos correntes (agosto 2026)

| Modelo | Posicionamento | Observação |
|---|---|---|
| **GPT-5.6 Sol** | Flagship; raciocínio complexo, coding, agentes | Família GPT-5.6 lançada em 09/07/2026 |
| **GPT-5.6 Terra** | Tier balanceado | Corte de preço de ~20% em 30/07/2026 |
| **GPT-5.6 Luna** | Tier de volume/custo mínimo | Corte de preço de ~80% em 30/07/2026 |
| **GPT-5.5 Pro** | Tier "research-grade" da geração anterior | Verificado em jun/2026; conferir se há sucessor na família 5.6 |

· fonte: https://developers.openai.com/api/docs/models/all e https://developers.openai.com/api/docs/pricing · data: 2026-08-12 (conforme verificação de agosto do L1-APX-J)

**Nota sobre GPT-4o.** Descontinuado no ChatGPT em 13/02/2026; continua disponível via API.

---

## Gemini — geração corrente (Google DeepMind)

### Modelos correntes (junho 2026)

| Modelo | API ID | Posicionamento | Janela de contexto |
|---|---|---|---|
| **Gemini 3.1 Pro** | `gemini-3.1-pro` | Flagship (release 19/02/2026); multimodal, agêntico | 2M tokens |
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

- **2026-08-12**: snapshot atualizado — Claude Opus 5 (GA 24/07) e Sonnet 5 adicionados; timeline do Fable 5 (blackout jun, redeploy 01/07, usage credits 07/07, recalibração bio 07/08); watermarking (modelos ≥ 02/08); família GPT-5.6 (Sol/Terra/Luna, 09/07, corte 30/07); Gemini 3.1 Pro consolidado como flagship.
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
