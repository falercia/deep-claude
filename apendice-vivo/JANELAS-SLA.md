# Janelas de Contexto e SLAs — Snapshot

> Atualizado em: 2026-06-06 (seed inicial; lançamento oficial em 2026-07)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

**Janela de contexto** é o limite total de tokens (input + output) que um modelo aceita em uma única chamada. Determina o tamanho máximo de documentos, históricos de conversa, RAG context, ou contexto de agente.

**SLA** (Service Level Agreement) é o compromisso de disponibilidade declarado pelo fornecedor. Crítico para aplicações de produção; ausência de SLA em tier gratuito é regra.

**Cotas** definem requisições por minuto, tokens por dia, etc., conforme plano e tier.

---

## Anthropic — Claude

### Janelas de contexto

| Modelo | Janela | Observação |
|---|---|---|
| **Opus** (geração corrente) | 200K tokens | ~150k palavras em português |
| **Sonnet** (geração corrente) | 200K tokens | ~150k palavras em português |
| **Haiku** (geração corrente) | 200K tokens | ~150k palavras em português |

**Conversão prática.** Em português brasileiro, 1 token ≈ 0,5-0,7 palavras (depende de palavras compostas e termos técnicos). 200K tokens ≈ 130-150k palavras ≈ 250-300 páginas de livro técnico.

**Performance dentro da janela.** Modelos têm queda mensurável de qualidade após ~50-70% da janela (efeito "lost in the middle"). Para uso crítico, mantenha contexto enxuto via RAG ou compressão (Caps 25, 27).

### SLAs por plano

| Plano | SLA declarado | Suporte |
|---|---|---|
| **Free / Pro individual** | Sem SLA formal | Comunidade |
| **Team** | TBD (best effort) | Suporte standard |
| **Enterprise** | TBD (uptime garantido) | Suporte dedicado, conta CSM |
| **API standard** | TBD | Suporte por ticket |

**Fonte oficial:** https://www.anthropic.com/legal/ssa (Service Standards Agreement)

### Cotas por plano (referência)

| Plano | Mensagens / dia (Web/Desktop/Mobile) | Tokens API / minuto |
|---|---|---|
| Free | Limite diário (varia) | N/A |
| Pro | 5x do Free típico | N/A |
| Team / Enterprise | Maior, com flex | Maior, com tiers |

API segue **rate limit por tier de organização**, com tiers 1-4 conforme histórico de uso e pagamento.

### Disponibilidade regional

| Região | Disponibilidade | Soberania |
|---|---|---|
| **AWS Bedrock SP** | Disponível | Dados ficam no Brasil |
| **AWS Bedrock global** | Disponível | Conforme região escolhida |
| **Google Vertex AI** | Disponível | Conforme região |
| **Anthropic API direta** | Disponível | Datacenters EUA |

**Para casos com LGPD restritiva** (Caps 38, 44 do livro): use Bedrock SP. Para casos com transferência internacional autorizada via base legal LGPD: qualquer opção. Sempre conferir contrato vigente.

---

## Concorrentes

| Família | Janela típica | SLA Enterprise |
|---|---|---|
| **GPT** (OpenAI) | Variável (128K-2M conforme modelo) | SLA Azure OpenAI declarado |
| **Gemini** (Google) | Variável (1M-2M conforme modelo) | SLA Vertex AI declarado |

---

## Histórico de incidentes

*Esta seção registra incidentes públicos de disponibilidade que afetaram operação relevante.*

- **2026-06-06**: snapshot seed criado, sem incidentes registrados.

**Como contribuir.** Observou incidente público relevante? Abra issue com label `incidente`, com link para status page oficial e descrição de impacto.

---

## Recomendações executivas

**Para piloto** (Cap 42 do livro): API direta com tier inicial. Sem SLA formal mas suficiente para validação.

**Para produção operacional** (Cap 42): Team ou Enterprise, com SLA declarado. Para fluxos críticos com LGPD, Bedrock SP.

**Para uso institucional sensível**: Enterprise com BAA/DPA assinado, SLA garantido, suporte dedicado. ISO 42001 em vigor é diferencial (Cap 44).

**Para backup**: arquitetura multi-modelo via gateway (LiteLLM, OpenRouter ou proprietário) garante fallback quando provedor falha.

---

## Mudanças recentes

- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**TBD — Publicação oficial (2026-07).** Snapshot inicial estabelece estrutura. A publicação oficial em julho de 2026 trará SLAs específicos e cotas vigentes conforme tabelas oficiais.

---

## Fontes primárias

- Anthropic Models: https://docs.anthropic.com/en/docs/about-claude/models
- Anthropic Service Standards: https://www.anthropic.com/legal/ssa
- Anthropic Status: https://status.anthropic.com/
- AWS Bedrock (Anthropic): https://aws.amazon.com/bedrock/claude/
- Google Vertex (Anthropic): https://cloud.google.com/vertex-ai/docs/generative-ai/partner-models/claude

Ver [`FONTES.md`](./FONTES.md) para lista completa.
