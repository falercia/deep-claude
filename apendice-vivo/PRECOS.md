# Preços — Snapshot

> **Snapshot 2026-10-09**
> Atualizado em: 2026-10-09 (Haiku 5.5, correção do cache read do Sonnet 5.5, aumento de tarifa do Gemini Flash em 01/01/2027 — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-10-01
> Próxima atualização: novembro/2026 (checagem mensal)
> Cotação USD/BRL referência: ver abaixo
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

Preços de API são cobrados por **token**, normalmente por milhão de tokens (MTok = 1.000.000). Input e output têm preços distintos, com output tipicamente 3-5x mais caro que input.

**Desconto por caching** (prompt caching) reduz significativamente custo de input em chamadas repetidas. Anthropic oferece cache read a 10% do preço de input (desconto de 90%) nas gerações anteriores e no Haiku 5.5, a 5% no Opus 5.5 e no Sonnet 5.5 (US$ 0,20 e US$ 0,10 por MTok) e a 2,5% no Fable 5.1 e no Mythos 5.1 (US$ 0,25 por MTok). Para detalhes, ver Capítulo 25 do livro.

**Desconto por batch** (Batch API) oferece 50% de desconto para requisições não-síncronas processadas em até 24h. Para detalhes, ver Capítulo 21 do livro.

---

## Anthropic — Claude (outubro 2026)

**Tabela de preços confirmados por fonte primária:**

| Modelo | Input ($/MTok) | Output ($/MTok) | Cache write 5min | Cache write 1h | Cache read (hit) | Batch input | Batch output |
|---|---|---|---|---|---|---|---|
| **Claude Fable 5.1** (01/set/2026) | $10,00 | $50,00 | $12,50 | $20,00 | $0,25 | $5,00 | $25,00 |
| **Claude Mythos 5.1** (restrito) | $10,00 | $50,00 | $12,50 | $20,00 | $0,25 | $5,00 | $25,00 |
| **Claude Opus 5.5** (22/set/2026) | $4,00 | $20,00 | $5,00 | $8,00 | $0,20 | $2,00 | $10,00 |
| **Claude Sonnet 5.5** (28/set/2026) | $2,00 | $10,00 | $2,50 | $4,00 | $0,10 | $1,00 | $5,00 |
| **Claude Haiku 5.5** (07/out/2026), prompt até 100k tokens | $0,10 | $0,50 | $0,125 | $0,20 | $0,01 | $0,05 | $0,25 |
| **Claude Haiku 5.5**, prompt acima de 100k tokens | $0,50 | $2,50 | $0,625 | n/d | $0,05 | $0,25 | $1,25 |
| **Claude Fable 5** | $10,00 | $50,00 | $12,50 | $20,00 | $1,00 | $5,00 | $25,00 |
| **Claude Mythos 5** (restrito, Glasswing) | $10,00 | $50,00 | $12,50 | $20,00 | $1,00 | $5,00 | $25,00 |
| **Claude Opus 5** | $5,00 | $25,00 | $6,25 | $10,00 | $0,50 | $2,50 | $12,50 |
| **Claude Opus 4.8** | $5,00 | $25,00 | $6,25 | $10,00 | $0,50 | $2,50 | $12,50 |
| **Claude Sonnet 5** | $2,00 | $10,00 | $2,50 | $4,00 | $0,20 | $1,00 | $5,00 |
| **Claude Sonnet 4.6** | $3,00 | $15,00 | $3,75 | $6,00 | $0,30 | $1,50 | $7,50 |
| **Claude Haiku 4.5** (geração anterior) | $1,00 | $5,00 | $1,25 | $2,00 | $0,10 | $0,50 | $2,50 |

· fonte: https://platform.claude.com/docs/en/about-claude/pricing · data: 2026-10-09 (linhas 5.1/5.5 e Opus 5.5 também em platform.claude.com/docs/en/models/*/overview; Haiku 5.5 também em platform.claude.com/docs/en/models/haiku-5-5/overview e anthropic.com/claude-haiku-5-5). Fable 5, Mythos 5, Opus 5 e Sonnet 5 permanecem listados como geração anterior. "n/d" = a página consultada não publica o valor.

**Notas:**
- Todos os valores em USD por milhão de tokens (MTok).
- **Sonnet 5: aumento cancelado.** O preço de lançamento ($2/$10) virou preço padrão; o aumento programado para $3/$15 em 01/09/2026 **não vai ocorrer** (nota oficial na página de pricing, capturada em 12/08/2026).
- **Tokenizer novo (geração 4.7+, incl. Opus 5, Fable 5, Sonnet 5):** o mesmo texto mapeia para ~30% mais tokens. Compare **custo por tarefa**, nunca custo por token, ao cruzar gerações.
- Cache write cobra a 1,25x (5 min) ou 2x (1h) o preço de input; cache read cobra a 0,1x o preço de input, **exceto Fable 5.1 e Mythos 5.1 (0,025x) e Opus 5.5 e Sonnet 5.5 (0,05x)**.
- **Haiku 5.5 (07/10/2026):** preço escalonado pelo tamanho do prompt, medido por requisição e contando input, cache reads e cache writes; até 100k tokens custa $0,10/$0,50, acima disso $0,50/$2,50. Contexto de 1M, saída de 128K, retirada não antes de 07/10/2027. Usa o tokenizer novo, cerca de 30% mais tokens que o Haiku 4.5, e rejeita `temperature`, `top_p` e `top_k` não padrão com erro 400. Fontes: https://www.anthropic.com/claude-haiku-5-5 e https://platform.claude.com/docs/en/models/haiku-5-5/overview.
- **Opus 5.5** custa 40% do Fable 5.1 e 80% do Opus 5; Fast mode (research preview, só Claude API) a $8 input / $40 output.
- **Cobrança além do token:** Managed Agents cobra **US$ 0,08 por session-hour** em estado `running` (sem Batch, sem cloud parceira); `inference_geo: "us"` multiplica todos os tokens por 1,1x (Claude 4.6+); web search US$ 10 por 1.000 buscas; web fetch sem custo adicional; code execution grátis junto de search/fetch, e fora disso 1.550 h grátis por organização por mês e US$ 0,05 por hora depois; toolsets de computer use e browser use somam cerca de 4.500 e 6.600 tokens de input por requisição.
- Batch API processa requisições de forma assíncrona (até 24h); desconto de 50% sobre input e output.
- **Fast mode (research preview)** para Opus 5 e Opus 4.8: $10 input / $50 output por MTok. Indisponível em Opus 4.7 (erro) e 4.6 (roda em velocidade padrão).
- **Data residency (US-only inference)**: multiplicador de 1,1x sobre todos os tokens.
- **Usage credits (corrigido em 01/10/2026):** em Max e seats premium, Fable 5 e 5.1 são parte do plano até 50% dos limites semanais, sem data de término; em Pro e seats standard o acesso é por usage credits, e a promoção anterior terminou em 19/07/2026 (não 07/07); a única taxa publicada é a da API ($10/$50). Fonte: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan. Marketplaces (AWS, Microsoft Foundry) faturam em CCU: 100 CCU = US$ 1,00.

**Sempre confirmar em:** https://platform.claude.com/docs/en/about-claude/pricing

---

## OpenAI — GPT (outubro 2026)

| Modelo | Input ($/MTok) | Output ($/MTok) | Observação |
|---|---|---|---|
| **GPT-6 Astra** (03/set/2026) | $10,00 | $50,00 | Flagship; cache read $1,00; contexto 1M; Fast 2x, Ultrafast 6x |
| **GPT-6.1 Sol** (29/09/2026) | $2,00 | $10,00 | Capacidade comparável à do Astra segundo a OpenAI; system card em 29/09 |
| **GPT-6 Luna** | $0,10 | $0,50 | Tier de volume na página de pricing de out/2026 |
| **GPT-5.6 Sol** | $5,00 | $30,00 | Flagship da família 5.6 (lançada 09/07/2026) |
| **GPT-5.6 Terra** | $2,00 | $12,00 | Tier balanceado; preço pós-corte de 30/07/2026 |
| **GPT-5.6 Luna** | $0,20 | $1,20 | Tier de volume; corte de ~80% em 30/07/2026 |
| **GPT-5.5 Pro** | $30,00 | $180,00 | Tier "research-grade" da geração anterior (verificado jun/2026) |

· fonte: https://developers.openai.com/api/docs/pricing · data: 2026-10-01 (linhas GPT-6) e 2026-08-12 (linhas GPT-5.6, **reverificar se ainda listadas**). O Sol 5.6 foi cortado para $4/$20 promocional até ao menos 21/11/2026 (corte de 21/08).

**Atenção:** o tier de volume da OpenAI teve dois repricings em 2026; é o preço mais volátil do mercado. Confirmar na página oficial antes de orçamento: https://developers.openai.com/api/docs/pricing

---

## Google Gemini (outubro 2026)

### Via Gemini API (ai.google.dev) — Paid Tier

| Modelo | Input ($/MTok) | Output ($/MTok) | Cache read | Observação |
|---|---|---|---|---|
| **Gemini 3.1 Pro** | $2,00 (≤200K prompt) / $4,00 (>200K) | $12,00 (≤200K) / $18,00 (>200K) | $0,20 (≤200K) / $0,40 (>200K) | Flagship (release 19/02/2026); janela de 2M tokens |
| **Gemini 3.8 Flash** | $0,75 (tarifa padrão até 31/12/2026); $1,50 a partir de 01/01/2027 | $3,75; $7,50 a partir de 01/01/2027 | — | GA; contexto 1M e saída 64K (página do modelo); batch com 50% |
| **Gemini 2.5 Pro** | $1,25 (≤200K) / $2,50 (>200K) | $10,00 (≤200K) / $15,00 (>200K) | $0,125 (≤200K) / $0,25 (>200K) | Stable; inclui tokens de thinking |
| **Gemini 2.5 Flash** | $0,30 (texto/img/vídeo) / $1,00 (áudio) | $2,50 | $0,03 (texto) | Raciocínio híbrido; thinking budgets |
| **Gemini 2.5 Flash-Lite** | $0,10 (texto/img/vídeo) / $0,30 (áudio) | $0,40 | $0,01 (texto) | Mais econômico |

· fonte: https://ai.google.dev/gemini-api/docs/pricing · data: 2026-06-18

**Notas:**
- Output de Gemini inclui tokens de thinking quando aplicável.
- **Aumento programado em 01/01/2027 (conferido em 2026-10-09):** as tarifas dos Flash 3.6, 3.7 e 3.8 dobram, assim como Batch, Flex e Priority; o armazenamento de cache sobe de $0,50 para $1,00 por 1M tokens por hora. Fonte: https://ai.google.dev/gemini-api/docs/pricing (página lida até 100 mil dos 126 mil caracteres).
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

- **Prompt caching**: cache read a uma fração do preço de input (10% na maioria dos modelos, 5% no Opus 5.5 e no Sonnet 5.5, 2,5% no Fable 5.1)
- **Batch API**: 50% de desconto para fluxos não-síncronos
- **Router pattern**: rotear casos simples para Haiku, complexos para Sonnet, críticos para Opus
- **Compressão de prompt**: reduzir tokens de entrada via XML enxuto

---

## Mudanças recentes

- **2026-10-09**: **Haiku 5.5** (07/10, $0,10/$0,50 até 100k tokens de prompt e $0,50/$2,50 acima); correção do cache read do Sonnet 5.5 ($0,10, e não $0,20); notas de cache atualizadas (0,05x no Opus 5.5 e no Sonnet 5.5); aumento de tarifa do Gemini Flash em 01/01/2027. OpenAI reconferida na página oficial: GPT-6 Astra $10/$50, GPT-6.1 Sol $2/$10 e Luna $0,10/$0,50, sem mudança. Fable 5.1, Opus 5.5, Sonnet 5.5, Sonnet 5 e Haiku 4.5 reconferidos, sem mudança.
- **2026-10-01**: geração Claude 5.1/5.5 (Fable 5.1 cache read $0,25; Opus 5.5 $4/$20; Sonnet 5.5 $2/$10); correção da nota de usage credits (Help Center); bloco de cobrança além do token (session-hour, residência 1,1x, ferramentas); GPT-6 Astra, GPT-6.1 Sol e Luna; Gemini 3.8 Flash.
- **2026-08-12**: snapshot de agosto. **Sonnet 5 consolidado em $2/$10** (aumento de 01/09 cancelado pela Anthropic — fonte primária); Opus 5 e Mythos 5 adicionados à tabela; fast mode atualizado (Opus 5/4.8, $10/$50); notas de tokenizer (~30%, geração 4.7+) e usage credits/CCU; OpenAI atualizado para família GPT-5.6 (Sol $5/$30, Terra $2/$12, Luna $0,20/$1,20 pós-corte de 30/07); Gemini 3.1 Pro consolidado como flagship GA.
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
