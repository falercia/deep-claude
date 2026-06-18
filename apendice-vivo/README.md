# Apêndice Vivo

> A camada que muda. Modelos, preços, benchmarks, janelas de contexto, SLAs.
> Cadência mensal declarada. Errata pública. Fonte primária em cada item.

---

## Por que esta pasta existe

A obra *Deep Claude* opera sob o princípio editorial da **Camada Dupla**: o livro carrega o padrão durável (frameworks, conceitos, métodos), e este Apêndice Vivo carrega o número que muda no tempo (modelos, preços, benchmarks, janelas, SLAs).

Sem Apêndice Vivo, o livro técnico fica obsoleto em meses. Com cadência mensal cumprida, a obra permanece calibrada por anos.

> **Fonte única da série.** Este Apêndice Vivo é a **camada de números cross-vendor de toda a série** (Claude, GPT, Gemini e open-source). O livro *Inteligência Aumentada · Os Invariantes* — que ensina o método vendor-neutral de ler esses números — aponta para cá através do seu repositório companion ([`inteligencia-aumentada-recursos` → `apendice-vivo`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/apendice-vivo)). Mantém-se em **um só lugar** para que a cadência mensal nunca se fragmente em dois datasets.

---

## Estrutura

| Arquivo | Conteúdo |
|---|---|
| [`MODELOS.md`](./MODELOS.md) | Famílias de modelos atualizadas: Claude, GPT, Gemini, modelos open-source |
| [`PRECOS.md`](./PRECOS.md) | Preços normalizados por milhão de tokens, com cotação USD e BRL |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | SWE-bench, MMLU-Pro, GPQA, HumanEval+ e similares |
| [`JANELAS-SLA.md`](./JANELAS-SLA.md) | Janelas de contexto, cotas por plano, SLAs declarados |
| [`FONTES.md`](./FONTES.md) | Fontes primárias linkadas para rastreabilidade |
| [`REGULACAO.md`](./REGULACAO.md) | Status regulatório de IA: LGPD, ANPD, PL 2338/2023, normas setoriais BR; EU AI Act, NIST AI RMF, ISO/IEC 42001 |
| [`CHANGELOG-APENDICE.md`](./CHANGELOG-APENDICE.md) | Histórico mensal de atualizações e errata |
| [`2026-MM-snapshot.md`](./) | Snapshot consolidado do mês corrente |

---

## Cadência

**Atualização mensal**, entre os dias 1 e 7 de cada mês. Cadência declarada publicamente é compromisso editorial; não cumprir vira perda de credibilidade.

Mudanças relevantes fora da janela mensal (lançamento de modelo, mudança de preço, incidente grave) geram alerta no `CHANGELOG-APENDICE.md` com data e tipo, sem esperar a janela mensal.

---

## Como o leitor usa

**Para uso individual**: consulte antes de decisão sobre tier, modelo, preço. Confira data de atualização de cada item. Quando dúvida, vá à fonte primária linkada.

**Para uso organizacional**: instale leitura mensal do CHANGELOG como ritual técnico. Sinalize ao time quando mudança relevante afeta operação. Integre atualizações ao orçamento (Cap 43 do livro) e à arquitetura.

**Para uso em treinamento**: use como referência viva em workshops, cursos internos, mentorias. Estudantes aprendem padrão durável no livro e consultam números atuais aqui.

---

## Princípios

**Fonte primária obrigatória.** Cada item carrega link para fonte primária (doc oficial, blog launch, paper). Sem fonte primária, item não entra.

**Errata pública.** Quando informação anterior estava errada, errata explícita no CHANGELOG com correção. Não removida silenciosamente.

**Sem benchmark inflado.** Reportamos resultados como divulgados pelas fontes primárias, sem cherry-picking de configuração favorável.

**Transparência temporal.** Cada item carrega `Atualizado em: AAAA-MM-DD`. Leitor sabe a frescura do dado.

---

## Capítulos relacionados

- **Capítulo 45 — Apêndice Vivo** (mecanismo editorial)
- **Capítulo 46 — Regulação e Compliance de IA** (usa `REGULACAO.md` como referência viva)
- **Capítulo 4 — Modelos Claude** (escolha entre Opus, Sonnet, Haiku)
- **Capítulo 5 — Quando usar cada tier** (matriz de decisão)
- **Capítulo 6 — Refresher Tokens** (mecânica de cobrança)
- **Capítulo 19 — Team / Enterprise** (cotas e SLAs corporativos)

---

## Roadmap

| Versão | Data | Conteúdo |
|---|---|---|
| Seed v0 | 2026-06 | Estrutura inicial e template |
| v1.0 | 2026-07 | Snapshot de lançamento da obra |
| v1.1+ | Mensal | Atualização mensal contínua |
