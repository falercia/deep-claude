# Janelas de Contexto e SLAs — Snapshot

> **Snapshot 2026-06-18 · rascunho para conferência do autor**
> Atualizado em: 2026-06-18 (populamento com dados correntes — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-06-06 (seed inicial)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

**Janela de contexto** é o limite total de tokens (input + output) que um modelo aceita em uma única chamada. Determina o tamanho máximo de documentos, históricos de conversa, RAG context, ou contexto de agente.

**SLA** (Service Level Agreement) é o compromisso de disponibilidade declarado pelo fornecedor. Crítico para aplicações de produção; ausência de SLA em tier gratuito é regra.

**Cotas** definem requisições por minuto, tokens por dia, etc., conforme plano e tier.

---

## Anthropic — Claude

### Janelas de contexto (junho 2026)

| Modelo | Janela (Claude API) | Observação |
|---|---|---|
| **Claude Fable 5** | 1M tokens | ~750-800k palavras em português |
| **Claude Mythos 5** | 1M tokens | Acesso limitado (Project Glasswing) |
| **Claude Opus 4.8** | 1M tokens (API/Bedrock/Vertex) | 200K no Microsoft Foundry |
| **Claude Opus 4.7** | 1M tokens | — |
| **Claude Opus 4.6** | 1M tokens | GA; sem beta header necessário |
| **Claude Sonnet 4.6** | 1M tokens | GA; sem beta header necessário |
| **Claude Haiku 4.5** | 200K tokens | ~150K palavras em português |

· fonte: https://platform.claude.com/docs/en/about-claude/models/overview · data: 2026-06-18

**Conversão prática.** Em português brasileiro, 1 token ≈ 0,5-0,7 palavras (depende de palavras compostas e termos técnicos). 200K tokens ≈ 130-150k palavras ≈ 250-300 páginas de livro técnico. 1M tokens ≈ 650-750k palavras ≈ 1200-1500 páginas.

**Performance dentro da janela.** Modelos têm queda mensurável de qualidade após ~50-70% da janela (efeito "lost in the middle"). Para uso crítico, mantenha contexto enxuto via RAG ou compressão (Caps 25, 27).

**Long context pricing.** Claude Fable 5, Mythos 5, Opus 4.8/4.7/4.6 e Sonnet 4.6 incluem a janela completa de 1M tokens ao preço padrão por token (sem premium por contexto longo).
· fonte: https://platform.claude.com/docs/en/about-claude/pricing · data: 2026-06-18

### SLAs por plano

| Plano | SLA declarado | Suporte |
|---|---|---|
| **Free / Pro individual** | Sem SLA formal | Comunidade |
| **Team** | TBD (a confirmar) | Suporte standard |
| **Enterprise** | TBD (a confirmar — contrato negociado) | Suporte dedicado, conta CSM |
| **API standard** | TBD (a confirmar) | Suporte por ticket |

**Nota.** SLAs específicos do plano Enterprise são negociados por contrato e não são publicados em página pública de forma detalhada. Para confirmar SLA vigente, consultar https://www.anthropic.com/legal/ssa e o time de conta Anthropic.
· fonte: https://www.anthropic.com/legal/ssa · data: 2026-06-18

### Cotas por plano (referência)

| Plano | Mensagens / dia (Web/Desktop/Mobile) | Tokens API / minuto |
|---|---|---|
| Free | Limite diário (varia) | N/A |
| Pro | 5x do Free típico | N/A |
| Team / Enterprise | Maior, com flex | Maior, com tiers (Tier 1-4) |

API segue **rate limit por tier de organização**, com tiers 1-4 conforme histórico de uso e pagamento.
· fonte: https://platform.claude.com/docs/en/api/rate-limits · data: 2026-06-18

### Disponibilidade regional

| Região | Disponibilidade | Soberania |
|---|---|---|
| **AWS Bedrock** (regiões globais) | Disponível | Conforme região escolhida |
| **AWS Bedrock** (endpoint global) | Disponível | Roteamento dinâmico (max disponibilidade) |
| **AWS Bedrock** (endpoint regional) | Disponível; +10% de custo | Dados garantidos na região |
| **Google Vertex AI** | Disponível | Conforme região (global, multi-region, regional) |
| **Anthropic API direta** | Disponível | Datacenters EUA (padrão) |
| **Anthropic API (data residency US)** | Disponível para Opus 4.6/Sonnet 4.6 e posteriores | Inferência garantida nos EUA; +10% custo |
| **Claude Platform on AWS** | Disponível | Segue Bedrock; billing via AWS Marketplace |
| **Microsoft Foundry** | Disponível (Opus 4.8 com janela de 200K) | Conforme região Azure |

· fonte: https://platform.claude.com/docs/en/about-claude/pricing · data: 2026-06-18

**Para casos com LGPD restritiva** (Caps 38, 44 do livro): use Bedrock endpoint regional ou Anthropic API com `inference_geo: "us"`. Para casos com transferência internacional autorizada via base legal LGPD: qualquer opção. Sempre conferir contrato vigente.

---

## Concorrentes

### OpenAI — Janelas de contexto (junho 2026)

| Modelo | Janela de contexto |
|---|---|
| **GPT-5.5** | TBD (a confirmar; >200K esperado) |
| **GPT-4.1** | 1M tokens |
| **GPT-4.1 mini** | TBD (a confirmar) |
| **o3** | TBD (a confirmar) |

· fonte: https://platform.openai.com/docs/models (a confirmar) · data: 2026-06-18

### Google Gemini — Janelas de contexto (junho 2026)

| Modelo | Janela de contexto |
|---|---|
| **Gemini 3.1 Pro Preview** | TBD (a confirmar) |
| **Gemini 2.5 Pro** | 1M tokens |
| **Gemini 2.5 Flash** | 1M tokens |
| **Gemini 2.5 Flash-Lite** | TBD (a confirmar) |

· fonte: https://ai.google.dev/gemini-api/docs/models · data: 2026-06-18

---

## Histórico de incidentes

*Esta seção registra incidentes públicos de disponibilidade que afetaram operação relevante.*

- **2026-06-18**: snapshot populado, sem incidentes relevantes recentes registrados. Para histórico de status, consultar https://status.anthropic.com/ e https://status.openai.com/.

**Como contribuir.** Observou incidente público relevante? Abra issue com label `incidente`, com link para status page oficial e descrição de impacto.

---

## Recomendações executivas

**Para piloto** (Cap 42 do livro): API direta com tier inicial. Sem SLA formal mas suficiente para validação.

**Para produção operacional** (Cap 42): Team ou Enterprise, com SLA declarado. Para fluxos críticos com LGPD, Bedrock endpoint regional ou Anthropic API com data residency.

**Para uso institucional sensível**: Enterprise com BAA/DPA assinado, SLA garantido, suporte dedicado. ISO 42001 em vigor é diferencial (Cap 44).

**Para backup**: arquitetura multi-modelo via gateway (LiteLLM, OpenRouter ou proprietário) garante fallback quando provedor falha.

---

## Mudanças recentes

- **2026-06-18**: snapshot populado com janelas de contexto confirmadas (Claude: 1M para Fable 5/Opus/Sonnet; 200K para Haiku 4.5). Informações sobre endpoints regionais Bedrock/Vertex adicionadas. SLAs por plano ainda TBD — requere consulta direta ao time Anthropic.
- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**SLA Enterprise.** SLAs concretos de uptime (ex.: 99,9%) para planos Enterprise não são publicados em página pública pela Anthropic — são definidos por contrato. Para o livro, esta seção documenta o que é público; o leitor com necessidade de SLA formal deve solicitar ao time de vendas.

**Janelas OpenAI/Gemini.** Alguns valores marcados TBD para GPT-5.5 e Gemini 3.1 Pro Preview porque são modelos muito recentes ou em preview com documentação técnica ainda não completamente disponível via fetch estático. Confirmar em https://platform.openai.com/docs/models e https://ai.google.dev/gemini-api/docs/models.

---

## Fontes primárias

- Anthropic Models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- Anthropic Context windows: https://platform.claude.com/docs/en/build-with-claude/context-windows
- Anthropic Service Standards: https://www.anthropic.com/legal/ssa
- Anthropic Status: https://status.anthropic.com/
- Anthropic Pricing (long context, data residency): https://platform.claude.com/docs/en/about-claude/pricing
- AWS Bedrock (Anthropic): https://aws.amazon.com/bedrock/claude/
- Google Vertex (Anthropic): https://cloud.google.com/vertex-ai/docs/generative-ai/partner-models/claude
- OpenAI Models: https://platform.openai.com/docs/models
- Google Gemini Models: https://ai.google.dev/gemini-api/docs/models

Ver [`FONTES.md`](./FONTES.md) para lista completa.
