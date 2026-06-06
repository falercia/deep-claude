# Modelos — Snapshot

> Atualizado em: 2026-06-06 (seed inicial; lançamento oficial em 2026-07)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Famílias rastreadas

| Família | Fornecedor | Tier alto | Tier médio | Tier baixo | Open weights |
|---|---|---|---|---|---|
| **Claude** | Anthropic | Opus | Sonnet | Haiku | Não |
| **GPT** | OpenAI | Tier topo da geração corrente | Tier intermediário | Tier mini | Não |
| **Gemini** | Google DeepMind | Ultra/Pro | Flash | Nano | Não (varia) |
| **Llama** | Meta | 405B+ | 70B | 8B | Sim |
| **Mistral** | Mistral AI | Large | Medium | Small | Parcial |
| **Qwen** | Alibaba | Max | Plus | Turbo | Sim |
| **DeepSeek** | DeepSeek | R-series | V-series | — | Sim |

---

## Claude — geração 4.x (Anthropic)

Anthropic mantém três tiers vivos, com versionamento explícito por data de release. O leitor sério acompanha o release notes oficial e este snapshot.

| Modelo | Posicionamento | Casos típicos | Limites práticos |
|---|---|---|---|
| **Opus** (geração corrente) | Raciocínio complexo, planejamento multi-etapa | Pesquisa profunda, decisões críticas, agentes de longa duração | Latência maior, custo maior |
| **Sonnet** (geração corrente) | Equilíbrio entre qualidade e custo | Maioria das aplicações de produção, agentes operacionais, automação | Cobertura típica de 70-80% dos casos |
| **Haiku** (geração corrente) | Latência baixa, custo mínimo | Classificação, filtros, roteamento, sub-tarefas de pipeline | Limitações em raciocínio complexo |

**Mecânica de versionamento.** Anthropic identifica modelos com `claude-<tier>-<versão>-<data>` (exemplo: `claude-sonnet-4-5-20251022`). A versão data garante reprodutibilidade — pinning explícito em produção evita drift comportamental quando Anthropic publica nova revisão.

**Alias estáveis.** Em paralelo aos identificadores datados, existem aliases (`claude-sonnet-4`, etc.) que apontam para a revisão corrente. Conveniente para desenvolvimento, perigoso em produção sem teste de regressão.

---

## GPT — geração corrente (OpenAI)

OpenAI mantém múltiplos modelos vivos. Estrutura típica:

| Modelo | Posicionamento | Observação |
|---|---|---|
| Tier topo | Raciocínio complexo, agentes | Concorrente direto de Opus |
| Tier intermediário | Equilíbrio qualidade/custo | Concorrente direto de Sonnet |
| Tier mini/nano | Latência e custo mínimos | Concorrente direto de Haiku |

Versionamento da OpenAI também usa datas explícitas para reprodutibilidade.

---

## Gemini — geração corrente (Google DeepMind)

Google mantém família Gemini com tiers Ultra, Pro, Flash, Nano. Disponibilidade via Vertex AI e Google AI Studio. Forte em multimodal nativo.

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

*Esta seção registra mudanças observadas desde a última publicação do snapshot.*

- **2026-06-06**: snapshot seed criado. Detalhamento específico de versão e data será preenchido na publicação oficial de 2026-07.

---

## Notas editoriais

**TBD — Publicação oficial (2026-07).** Snapshot inicial estabelece estrutura. A publicação oficial em julho de 2026 trará identificadores específicos de modelo + data de release vigentes naquele momento, conforme release notes oficial da Anthropic e dos demais fornecedores.

**Como contribuir.** Observou modelo lançado ou mudança não capturada? Abra issue com label `errata` ou `nova-fonte`. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

Ver [`FONTES.md`](./FONTES.md) para lista completa com links de docs oficiais.
