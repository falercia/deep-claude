# Preços — Snapshot

> Atualizado em: 2026-06-06 (seed inicial; lançamento oficial em 2026-07)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Cotação USD/BRL referência: ver `FONTES.md`
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

Preços de API são cobrados por **token**, normalmente por milhão de tokens (1M = 1.000.000). Input e output têm preços distintos, com output tipicamente 3-5x mais caro que input.

**Desconto por caching** (prompt caching) reduz significativamente custo de input em chamadas repetidas. Anthropic oferece desconto típico de 90% para tokens em cache (cache hit). Para detalhes, ver Capítulo 25 do livro.

**Desconto por batch** (Batch API) oferece tipicamente 50% de desconto para requisições não-síncronas processadas em até 24h. Para detalhes, ver Capítulo 21 do livro.

---

## Anthropic — Claude (geração corrente)

**Tabela estrutural** (valores a confirmar na publicação oficial conforme fonte primária):

| Modelo | Input ($/1M tokens) | Output ($/1M tokens) | Cache write | Cache hit | Batch |
|---|---|---|---|---|---|
| **Opus** | TBD | TBD | TBD | TBD (~10% input) | TBD (-50%) |
| **Sonnet** | TBD | TBD | TBD | TBD (~10% input) | TBD (-50%) |
| **Haiku** | TBD | TBD | TBD | TBD (~10% input) | TBD (-50%) |

**Padrões observados em gerações anteriores** (referência):

| Tier | Input típico | Output típico | Comentário |
|---|---|---|---|
| Opus | ~$15/1M | ~$75/1M | Premium |
| Sonnet | ~$3/1M | ~$15/1M | Equilibrado |
| Haiku | ~$0.25-1/1M | ~$1-5/1M | Econômico |

**Sempre conferir doc oficial em https://docs.anthropic.com/en/docs/about-claude/models e https://www.anthropic.com/pricing antes de orçamento.**

---

## Cotação USD/BRL — referência mensal

| Mês | Cotação USD/BRL média | Fonte |
|---|---|---|
| 2026-06 | TBD | Banco Central |

**Como ler.** Para converter preço de API: `preço_BRL = preço_USD × cotação_média_mês`. Para orçamento institucional, somar 10-15% de buffer para volatilidade cambial.

---

## Concorrentes — referência

| Família | Tier alto | Tier médio | Tier baixo |
|---|---|---|---|
| **GPT** (OpenAI) | TBD | TBD | TBD |
| **Gemini** (Google) | TBD | TBD | TBD |

Snapshot oficial trará valores comparáveis para decisão multi-modelo.

---

## Modelos open-source — custo operacional

Modelos open-source não têm custo de API direto, mas têm custo de infraestrutura. Estimativa típica para inferência em produção:

| Tamanho | Custo de inferência típico |
|---|---|
| 7B-8B | $0.10-0.30/1M tokens (instância GPU dedicada) |
| 70B | $0.50-2/1M tokens |
| 400B+ | $5-15/1M tokens (multi-GPU) |

Custos via provedores managed (Together, Fireworks, Groq, etc.) variam. Sempre comparar com Claude da geração equivalente — modelo open-source só ganha em soberania total ou quando volume justifica.

---

## Calculadora rápida de custo

Para estimar custo mensal de uso típico:

```
custo_mensal = (tokens_input_mês × preço_input/1M) +
               (tokens_output_mês × preço_output/1M)
```

Exemplo conservador: 100M tokens input + 30M tokens output em Sonnet:

```
input:  100M × $3/1M  = $300
output:  30M × $15/1M = $450
total mensal: $750 (Sonnet)
```

**Otimizações típicas** (Cap 25 e Cap 35 do livro):

- **Prompt caching**: 50-90% de desconto em chamadas com contexto repetido
- **Batch API**: 50% de desconto para fluxos não-síncronos
- **Router pattern**: rotear casos simples para Haiku, complexos para Sonnet, críticos para Opus
- **Compressão de prompt**: reduzir tokens de entrada via XML enxuto

---

## Mudanças recentes

*Esta seção registra mudanças observadas desde a última publicação do snapshot.*

- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**TBD — Publicação oficial (2026-07).** Snapshot inicial estabelece estrutura e princípios de leitura. A publicação oficial em julho de 2026 trará valores específicos conforme tabela oficial vigente, com data de release.

**Como contribuir.** Observou mudança de preço não capturada? Abra issue com label `errata` e link para fonte primária. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

- Anthropic Pricing: https://www.anthropic.com/pricing
- Anthropic Docs (Models): https://docs.anthropic.com/en/docs/about-claude/models
- OpenAI Pricing: https://openai.com/pricing
- Google AI Pricing: https://ai.google.dev/pricing
- Banco Central (USD/BRL): https://www.bcb.gov.br/

Ver [`FONTES.md`](./FONTES.md) para lista completa.
