# Changelog do Apêndice Vivo

> Histórico mensal de atualizações, mudanças observadas e errata pública.
> Cadência: dias 1-7 de cada mês. Mudanças relevantes fora da janela geram alerta extraordinário aqui.

---

## 2026-07 (planejado — lançamento oficial)

### Adicionado
- Snapshot completo de modelos vigentes em julho/2026
- Preços oficiais com cotação USD/BRL do mês
- Benchmarks atualizados conforme leaderboards oficiais
- Janelas de contexto e SLAs por plano

### Marco
- Versão 1.0 do Apêndice Vivo casando com o lançamento do livro

---

## 2026-06-18 (populamento extraordinário — rascunho para conferência do autor)

### Contexto
Populamento de todos os campos TBD com dados correntes de junho/2026, obtidos via pesquisa em fontes primárias (Anthropic docs, Google AI pricing) e pesquisa web confirmando dados de terceiros (OpenAI). Marcado como rascunho — autor deve conferir antes da publicação oficial de julho.

### Preenchido em MODELOS.md
- **Claude (Anthropic):** API IDs correntes confirmados (`claude-fable-5`, `claude-mythos-5`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5`); janelas de contexto; nota sobre lançamento Fable 5/Mythos 5 em 09/06/2026.
  · fonte: https://platform.claude.com/docs/en/about-claude/models/overview · data: 2026-06-18
- **GPT (OpenAI):** modelos correntes mapeados (GPT-5.5, GPT-5.5 Pro, GPT-4.1, GPT-4.1 mini, GPT-4.1 nano, o3, o4-mini); GPT-4o marcado como descontinuado no ChatGPT (13/02/2026).
  · fonte: https://developers.openai.com/api/docs/models/all · data: 2026-06-18
- **Gemini (Google):** modelos correntes mapeados (Gemini 3.1 Pro Preview, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite); Gemini 2.0 Flash descontinuado com shutdown 01/06/2026.
  · fonte: https://ai.google.dev/gemini-api/docs/pricing · data: 2026-06-18

### Preenchido em PRECOS.md
- **Anthropic — preços completos confirmados** em fonte primária (docs.anthropic.com/pricing):
  - Claude Fable 5: $10/$50 por MTok (input/output)
  - Claude Opus 4.8: $5/$25 por MTok
  - Claude Sonnet 4.6: $3/$15 por MTok
  - Claude Haiku 4.5: $1/$5 por MTok
  - Cache write 5min: 1,25x input; cache write 1h: 2x input; cache read: 0,1x input
  - Batch API: 50% desconto em todos os modelos
  · fonte: https://platform.claude.com/docs/en/about-claude/pricing · data: 2026-06-18
- **OpenAI — preços obtidos via pesquisa web** (não diretamente da página oficial por timeout):
  - GPT-5.5: $5/$30 por MTok; batch: $2,50/$15
  - GPT-4.1: $2/$8 por MTok
  - GPT-4.1 mini: $0,40/$1,60 por MTok
  - GPT-4.1 nano: $0,10/$0,40 por MTok
  - o3: $2/$8 por MTok
  - o4-mini: $1,10/$4,40 por MTok
  · fonte: pesquisa web (openai.com/api/pricing/ — confirmar antes de orçamento) · data: 2026-06-18
- **Google Gemini — preços completos confirmados** em fonte primária (ai.google.dev/gemini-api/docs/pricing):
  - Gemini 3.1 Pro Preview: $2,00/$12,00 por MTok (≤200K prompt)
  - Gemini 2.5 Pro: $1,25/$10,00 por MTok (≤200K prompt)
  - Gemini 2.5 Flash: $0,30/$2,50 por MTok
  - Gemini 2.5 Flash-Lite: $0,10/$0,40 por MTok
  · fonte: https://ai.google.dev/gemini-api/docs/pricing · data: 2026-06-18
- **USD/BRL:** mantido TBD — cotação PTAX de junho/2026 ainda não consolidada ao final do mês.

### Preenchido em BENCHMARKS.md
- **SWE-bench Verified:** scores de terceiros (morphllm.com) — Claude Fable 5 ~95%, Opus 4.8 ~88,6%, GPT-5.5 ~82,6%. Nota de cautela: confirmar no leaderboard oficial https://www.swebench.com/verified.html
  · fonte: https://www.morphllm.com/claude-benchmarks · data: 2026-06-18
- **GPQA Diamond:** top cluster 93-94% (Gemini 3.1 Pro Preview, Claude Opus 4.7 Adaptive, Claude Opus 4.8). Benchmark em saturação avançada.
  · fonte: pesquisa web (artificialanalysis.ai) · data: 2026-06-18
- **AIME 2025:** top models (GPT-5.2, Gemini 3 Pro) em ~100%. Score Claude não confirmado em fonte primária — mantido TBD.
  · fonte: pesquisa web (lmcouncil.ai) · data: 2026-06-18
- **MMLU-Pro e LiveCodeBench:** mantidos TBD — leaderboards dinâmicos não acessíveis via fetch estático.

### Preenchido em JANELAS-SLA.md
- **Claude — janelas de contexto confirmadas:**
  - Fable 5, Mythos 5, Opus 4.8/4.7/4.6, Sonnet 4.6: 1M tokens (via Claude API, Bedrock, Vertex)
  - Opus 4.8 via Microsoft Foundry: 200K tokens
  - Haiku 4.5: 200K tokens
  · fonte: https://platform.claude.com/docs/en/about-claude/models/overview · data: 2026-06-18
- **Long context pricing:** 1M tokens ao preço padrão por token para modelos Opus/Sonnet (sem premium).
  · fonte: https://platform.claude.com/docs/en/about-claude/pricing · data: 2026-06-18
- **Endpoints regionais Bedrock/Vertex:** documentados (+10% para regional vs. global a partir de Claude 4.5).
- **SLAs por plano:** mantidos TBD para Team/Enterprise/API — não publicados em detalhe em página pública; requere consulta direta.
- **Janelas OpenAI/Gemini:** GPT-4.1 = 1M tokens confirmado; Gemini 2.5 Pro/Flash = 1M tokens confirmado. GPT-5.5 e Gemini 3.1 Pro Preview marcados TBD.

### Campos que permanecem TBD após este populamento
| Arquivo | Campo TBD | Motivo |
|---|---|---|
| PRECOS.md | Cotação USD/BRL junho/2026 | PTAX não consolidado no meio do mês |
| PRECOS.md | Preços OpenAI (verificação) | Página oficial teve timeout; confirmar em openai.com/api/pricing/ |
| BENCHMARKS.md | Score Claude AIME 2025 | Fonte primária Anthropic não encontrada |
| BENCHMARKS.md | MMLU-Pro scores | Leaderboard dinâmico; consultar HuggingFace |
| BENCHMARKS.md | LiveCodeBench scores | Leaderboard dinâmico mensal; consultar livecodebench.github.io |
| BENCHMARKS.md | SWE-bench scores verificados oficialmente | Leaderboard usa JS dinâmico; confirmar em swebench.com/verified.html |
| JANELAS-SLA.md | SLAs numéricos por plano | Não publicados em detalhe na página pública Anthropic |
| JANELAS-SLA.md | Janela de contexto GPT-5.5 | Modelo muito recente; confirmar em platform.openai.com/docs/models |
| JANELAS-SLA.md | Janela de contexto Gemini 3.1 Pro Preview | Preview; confirmar em ai.google.dev/gemini-api/docs/models |
| JANELAS-SLA.md | Janela de contexto Gemini 2.5 Flash-Lite | Não encontrado no fetch; confirmar em ai.google.dev |

---

## 2026-06-06 (seed inicial)

### Adicionado
- Estrutura do Apêndice Vivo: 5 arquivos temáticos + changelog
- Princípios de leitura para cada arquivo
- Lista de fontes primárias estruturada
- Padrões de versionamento explícito (modelo + data)
- Padrão de transparência temporal (`Atualizado em` em cada item)

### Princípios estabelecidos
- Fonte primária obrigatória em cada item
- Errata pública via este changelog
- Cadência mensal declarada (dias 1-7)
- Sem cherry-picking de benchmark
- Cotação cambial via Banco Central

---

## Errata pública

*Quando informação anterior estava errada, errata explícita aqui com data, descrição e correção. Não removida silenciosamente do histórico do snapshot.*

Formato típico de errata:

```
### Errata YYYY-MM-DD
- **Arquivo**: PRECOS.md
- **Item**: Preço de Sonnet 4.6 input
- **Anterior**: $X / MTok
- **Correto**: $Y / MTok
- **Fonte**: link para doc oficial vigente na correção
- **Impacto para o leitor**: orçamentos calculados com valor anterior precisam ser revisitados.
```

Nenhuma errata até o momento.

---

## Alertas extraordinários

*Mudanças relevantes fora da janela mensal (lançamento de modelo, mudança de preço, incidente grave) geram alerta aqui sem esperar a janela.*

### Alerta 2026-06-09
- **Tipo**: Lançamento de modelos
- **Descrição**: Anthropic lança Claude Fable 5 (disponibilidade ampla via Claude API, Bedrock, Vertex, Foundry) e Claude Mythos 5 (acesso limitado via Project Glasswing). API IDs: `claude-fable-5` e `claude-mythos-5`. Janela de contexto: 1M tokens. Preço: $10/$50 por MTok (input/output).
- **Fonte**: https://platform.claude.com/docs/en/about-claude/models/overview
- **Impacto para o leitor**: novo tier de topo disponível para uso geral; Fable 5 torna-se a recomendação para workloads de máxima capacidade amplamente disponíveis.

---

## Cadência

| Janela | Atividade |
|---|---|
| Dia 1-3 do mês | Coleta de mudanças nas fontes primárias |
| Dia 4-6 do mês | Atualização dos arquivos do Apêndice |
| Dia 7 do mês | Publicação do snapshot do mês |
| Mid-month | Alertas extraordinários se aplicável |

**Compromisso declarado**: a cadência mensal é compromisso editorial. Não cumprir compromisso vira perda de credibilidade da obra.

---

## Como contribuir

Observou mudança em fonte primária que não está refletida no Apêndice Vivo?

1. Abra issue no repositório com label `errata` ou `nova-fonte`
2. Inclua link para fonte primária
3. Descreva a mudança e o impacto
4. Mantenedor processa na próxima janela mensal (ou em alerta extraordinário se crítico)

Veja [CONTRATO.md](../CONTRATO.md) para o fluxo completo.
