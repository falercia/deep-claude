# Preços — Snapshot

> **Snapshot 2026-06-18 · rascunho para conferência do autor**
> Atualizado em: 2026-06-18 (populamento com dados correntes — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-06-06 (seed inicial)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Cotação USD/BRL referência: ver abaixo
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

Preços de API são cobrados por **token**, normalmente por milhão de tokens (MTok = 1.000.000). Input e output têm preços distintos, com output tipicamente 3-5x mais caro que input.

**Desconto por caching** (prompt caching) reduz significativamente custo de input em chamadas repetidas. Anthropic oferece cache read a 10% do preço de input (desconto de 90%). Para detalhes, ver Capítulo 25 do livro.

**Desconto por batch** (Batch API) oferece 50% de desconto para requisições não-síncronas processadas em até 24h. Para detalhes, ver Capítulo 21 do livro.

---

## Anthropic — Claude (junho 2026)

**Tabela de preços confirmados por fonte primária:**

| Modelo | Input ($/MTok) | Output ($/MTok) | Cache write 5min | Cache write 1h | Cache read (hit) | Batch input | Batch output |
|---|---|---|---|---|---|---|---|
| **Claude Fable 5** | $10,00 | $50,00 | $12,50 | $20,00 | $1,00 | $5,00 | $25,00 |
| **Claude Opus 4.8** | $5,00 | $25,00 | $6,25 | $10,00 | $0,50 | $2,50 | $12,50 |
| **Claude Sonnet 4.6** | $3,00 | $15,00 | $3,75 | $6,00 | $0,30 | $1,50 | $7,50 |
| **Claude Haiku 4.5** | $1,00 | $5,00 | $1,25 | $2,00 | $0,10 | $0,50 | $2,50 |

· fonte: https://platform.claude.com/docs/en/about-claude/pricing · data: 2026-06-18

**Notas:**
- Todos os valores em USD por milhão de tokens (MTok).
- Cache write cobra a 1,25x (5 min) ou 2x (1h) o preço de input; cache read cobra a 0,1x o preço de input.
- Batch API processa requisições de forma assíncrona (até 24h); desconto de 50% sobre input e output.
- Claude Mythos 5 (disponibilidade limitada, Project Glasswing): mesmos preços de Fable 5 ($10/$50 per MTok).
- **Fast mode (research preview)** para Opus 4.8: $10 input / $50 output por MTok. Para Opus 4.6/4.7: $30/$150 por MTok.
- **Data residency (US-only inference)**: multiplicador de 1,1x sobre todos os tokens.

**Sempre confirmar em:** https://platform.claude.com/docs/en/about-claude/pricing

---

## OpenAI — GPT (junho 2026)

| Modelo | Input ($/MTok) | Output ($/MTok) | Observação |
|---|---|---|---|
| **GPT-5.5** | $5,00 | $30,00 | Flagship; batch e flex: $2,50/$15,00 |
| **GPT-5.5 Pro** | $30,00 | $180,00 | Tier máximo de raciocínio |
| **GPT-4.1** | $2,00 | $8,00 | Não-raciocínio; 1M contexto |
| **GPT-4.1 mini** | $0,40 | $1,60 | Velocidade/custo |
| **GPT-4.1 nano** | $0,10 | $0,40 | Ultra-baixo custo |
| **o3** | $2,00 | $8,00 | Raciocínio; substitui o1 |
| **o4-mini** | $1,10 | $4,40 | Raciocínio econômico |

· fonte: https://openai.com/api/pricing/ (via WebSearch confirmando dados de terceiros) · data: 2026-06-18

**Atenção:** Preços OpenAI acima foram obtidos por pesquisa web (terceiros e busca direta). Confirmar na página oficial antes de orçamento: https://openai.com/api/pricing/

---

## Google Gemini (junho 2026)

### Via Gemini API (ai.google.dev) — Paid Tier

| Modelo | Input ($/MTok) | Output ($/MTok) | Cache read | Observação |
|---|---|---|---|---|
| **Gemini 3.1 Pro Preview** | $2,00 (≤200K prompt) / $4,00 (>200K) | $12,00 (≤200K) / $18,00 (>200K) | $0,20 (≤200K) / $0,40 (>200K) | Preview; pode mudar |
| **Gemini 2.5 Pro** | $1,25 (≤200K) / $2,50 (>200K) | $10,00 (≤200K) / $15,00 (>200K) | $0,125 (≤200K) / $0,25 (>200K) | Stable; inclui tokens de thinking |
| **Gemini 2.5 Flash** | $0,30 (texto/img/vídeo) / $1,00 (áudio) | $2,50 | $0,03 (texto) | Raciocínio híbrido; thinking budgets |
| **Gemini 2.5 Flash-Lite** | $0,10 (texto/img/vídeo) / $0,30 (áudio) | $0,40 | $0,01 (texto) | Mais econômico |

· fonte: https://ai.google.dev/gemini-api/docs/pricing · data: 2026-06-18

**Notas:**
- Output de Gemini inclui tokens de thinking quando aplicável.
- Vertex AI tem preços próprios; conferir https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models para Claude via Vertex.
- Gemini 2.0 Flash e 2.0 Flash-Lite foram descontinuados com shutdown previsto para 01/06/2026.

---

## Cotação USD/BRL — referência mensal

| Mês | Cotação USD/BRL média | Fonte |
|---|---|---|
| 2026-06 | TBD (a confirmar) | Banco Central — PTAX: https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes |

**Como ler.** Para converter preço de API: `preço_BRL = preço_USD × cotação_média_mês`. Para orçamento institucional, somar 10-15% de buffer para volatilidade cambial.

**Nota:** Cotação PTAX do BCB para junho/2026 ainda não consolidada ao final do mês (consultar em 01-07-2026).

---

## Modelos open-source — custo operacional

Modelos open-source não têm custo de API direto, mas têm custo de infraestrutura. Estimativa típica para inferência em produção:

| Tamanho | Custo de inferência típico |
|---|---|
| 7B-8B | $0,10-0,30/MTok (instância GPU dedicada) |
| 70B | $0,50-2,00/MTok |
| 400B+ | $5,00-15,00/MTok (multi-GPU) |

Custos via provedores managed (Together, Fireworks, Groq, etc.) variam. Sempre comparar com Claude da geração equivalente — modelo open-source só ganha em soberania total ou quando volume justifica.

---

## Calculadora rápida de custo

Para estimar custo mensal de uso típico:

```
custo_mensal = (tokens_input_mês × preço_input/MTok) +
               (tokens_output_mês × preço_output/MTok)
```

Exemplo conservador: 100M tokens input + 30M tokens output em Sonnet 4.6:

```
input:  100M × $3,00/MTok = $300
output:  30M × $15,00/MTok = $450
total mensal: $750 (Sonnet 4.6)
```

**Otimizações típicas** (Cap 25 e Cap 35 do livro):

- **Prompt caching**: cache read a 10% do preço de input (~90% de desconto)
- **Batch API**: 50% de desconto para fluxos não-síncronos
- **Router pattern**: rotear casos simples para Haiku, complexos para Sonnet, críticos para Opus
- **Compressão de prompt**: reduzir tokens de entrada via XML enxuto

---

## Mudanças recentes

- **2026-06-22**: preços da família Claude (Opus 4.8 $5/$25, Sonnet 4.6 $3/$15, Haiku 4.5 $1/$5 por MTok) **reconferidos por busca web — sem mudança** desde 2026-06-18. Demais provedores e a cotação USD/BRL do mês permanecem para reconferência próxima ao fechamento de junho.
- **2026-06-18**: snapshot populado com preços correntes confirmados por fonte primária (Anthropic docs, Google AI pricing). OpenAI confirmado por pesquisa web (verificar em fonte primária antes de orçamento).
- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**Verificação recomendada antes de orçamento.** Preços de API mudam sem aviso prévio. Confirmar sempre nas páginas oficiais antes de qualquer decisão financeira:
- Anthropic: https://platform.claude.com/docs/en/about-claude/pricing
- OpenAI: https://openai.com/api/pricing/
- Google: https://ai.google.dev/gemini-api/docs/pricing

**Como contribuir.** Observou mudança de preço não capturada? Abra issue com label `errata` e link para fonte primária. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

- Anthropic Pricing (docs): https://platform.claude.com/docs/en/about-claude/pricing
- Anthropic Models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- OpenAI API Pricing: https://openai.com/api/pricing/
- OpenAI Developers Pricing: https://developers.openai.com/api/docs/pricing
- Google Gemini API Pricing: https://ai.google.dev/gemini-api/docs/pricing
- Banco Central (USD/BRL PTAX): https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes

Ver [`FONTES.md`](./FONTES.md) para lista completa.
