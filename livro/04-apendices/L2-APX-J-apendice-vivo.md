# APÊNDICE J — APÊNDICE VIVO
## Versões, preços, benchmarks e mercado: snapshot único com fonte e data

> 🧭 **Por que este apêndice existe**
>
> Este é o coração operacional da **Camada Dupla (Invariante 3)**. Os dois livros são deliberadamente atemporais no corpo; todo número volátil — versão de modelo, preço por milhão de tokens, posição em benchmark público, tamanho de janela, latência declarada — mora aqui, com fonte verificável e data do snapshot. Quando a operação precisar do número da semana, é aqui que se consulta. Quando os números mudarem, é aqui que se atualiza, sem tocar no resto da obra.

---

## CONTRATO DESTE APÊNDICE

| Item | Compromisso |
|------|-------------|
| **Periodicidade declarada** | Atualização ao menos mensal; reedições maiores a cada trimestre |
| **Fonte por linha** | Toda afirmação quantitativa cita o link de origem |
| **Data do snapshot** | No topo desta página e no rodapé de cada bloco |
| **Sem extrapolação** | Padrões e tendências ficam nos capítulos do L1; aqui ficam os números |
| **Versão impressa = foto do momento** | A edição impressa carimba a data; a edição digital é atualizada online |
| **Disciplina pública** | Mudanças relevantes ficam no [Controle de versão deste apêndice](#controle-de-versão-deste-apêndice) |

---

## ALERTA DE LEITURA

> ⚠️ **Como ler este apêndice sem cometer o erro óbvio**
>
> Os números abaixo são úteis para decisão informada **agora**. Não os memorize. Aprenda a ler a fonte e a atualizar com ela. Toda decisão arquitetural de longo prazo deve assumir que estes números mudam — o que **não** muda é o padrão descrito nos capítulos do Livro 1.

---

## DATA DO SNAPSHOT

**Versão v0.2 — 2026-07-05.**
Snapshot atualizado com a rodada de fronteira da família Claude (Fable 5 / Mythos 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5), preços por milhão de tokens conferidos na fonte oficial, o novo **modelo de precificação por *usage credits*** e a mudança de tokenizer. As demais famílias proprietárias (GPT, Gemini, Grok) e os open-weights mantêm a estrutura mapeada; o populamento numérico por linha, com fonte oficial de cada vendor, entra em rodadas seguintes — sem fabricar número que não tenha fonte primária.

> **Como este bloco foi checado:** cada preço e data abaixo tem link para a fonte primária da Anthropic (docs de pricing e posts de anúncio), consultada em 2026-07-05. Nenhum número foi estimado.

---

## SEÇÃO 1 — FAMÍLIAS DE MODELO PROPRIETÁRIOS

### 1.1 — Anthropic — Família Claude

**Status:** ativa. A nomenclatura em formas literárias, que começou tripartite (Opus · Sonnet · Haiku) com Claude 3, ganhou em 2026 uma **camada de fronteira acima de Opus**: a classe **Mythos**. O trio de trabalho diário permanece Opus/Sonnet/Haiku; acima dele fica o tier de fronteira, entregue em duas formas — **Fable** (com salvaguardas fortes, para uso geral) e **Mythos** (as mesmas capacidades com salvaguardas de cyber removidas, acesso restrito). *Fable* vem de *fabula* ("aquilo que se conta"), parente do grego *mythos*: a salvaguarda é o que separa os dois nomes.
**Posicionamento estratégico:** força relativa em código, agentes de horizonte longo, escrita executiva, e uma filosofia de alignment pública (Constitutional AI). O tier de fronteira (Mythos-class) é, segundo a própria Anthropic, o mais capaz que já disponibilizaram.
**Fonte primária:** [platform.claude.com — pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [platform.claude.com — models overview](https://platform.claude.com/docs/en/about-claude/models/overview) · [anthropic.com/news](https://www.anthropic.com/news).

#### Lineup e preços correntes (snapshot 2026-07-05)

Preços em USD por milhão de tokens (MTok). "Cache read" = leitura de cache (10% do input). Janela de contexto de 1M tokens no padrão para os modelos de fronteira e Sonnet 5; Haiku opera em janela menor. Fonte da tabela: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing), consultada em 2026-07-05.

| Modelo | ID de API | Input | Output | Batch (in/out) | Cache read | Papel no encaixe (Inv. 4) |
|--------|-----------|-------|--------|----------------|-----------|---------------------------|
| **Fable 5** | `claude-fable-5` | $10 | $50 | $5 / $25 | $1 | Fronteira geral: planejamento, arquitetura e os problemas mais difíceis / horizonte longo. O modelo mais caro da lista. |
| **Mythos 5** *(restrito — [Glasswing](https://anthropic.com/glasswing))* | — | $10 | $50 | $5 / $25 | $1 | Mesmo modelo do Fable, salvaguardas de cyber removidas. Ciberdefesa de fronteira; acesso só a parceiros aprovados. |
| **Opus 4.8** | `claude-opus-4-8` | $5 | $25 | $2,50 / $12,50 | $0,50 | Fronteira geral a metade do preço do Fable; é para onde o Fable **redireciona** requisições sensíveis (cyber/bio/destilação). Fast mode a $10/$50. |
| **Sonnet 5** *(intro, até 31/ago/2026)* | `claude-sonnet-5` | $2 | $10 | $1 / $5 | $0,20 | Cavalo de batalha de produção; **default de Free e Pro**. Roteie bulk/coding aqui. |
| **Sonnet 5** *(padrão, a partir de 01/set/2026)* | `claude-sonnet-5` | $3 | $15 | $1,50 / $7,50 | $0,30 | Mesmo modelo, preço padrão após a janela introdutória. |
| **Haiku 4.5** | `claude-haiku-4-5` | $1 | $5 | $0,50 / $2,50 | $0,10 | Volume alto, latência baixa: classificação, extração, roteamento. Um décimo do preço do Fable. |

> **Multiplicadores de cache** (sobre o input base): escrita de 5 min = 1,25×; escrita de 1 h = 2×; leitura (hit) = 0,1×. Válidos para toda a família.

#### Tokenizer novo (afeta contagem de tokens e, logo, custo)

Opus 4.7+, Fable 5, Mythos 5 e Sonnet 5 usam um **tokenizer novo**: o mesmo texto passa a mapear para mais tokens — cerca de **1,0× a 1,35×** conforme o tipo de conteúdo. Consequência prática: um custo comparado modelo-a-modelo *por token* subestima o custo real *por tarefa* nesses modelos. A Anthropic calibrou o preço introdutório do Sonnet 5 para que a migração a partir do Sonnet 4.6 seja aproximadamente custo-neutra. Fonte: [nota de rodapé do anúncio do Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5).

#### O modelo de precificação por *usage credits* (mudança estrutural, não só de número)

A novidade que mais importa para orçamento não é um preço — é um **mecanismo de cobrança**. Para os modelos de fronteira (a começar pelo Fable 5), a Anthropic passou a **desacoplar o acesso da inclusão fixa na assinatura**, movendo-o para *usage credits* (crédito de uso medido):

| Plano / superfície | Como o Fable 5 é cobrado |
|--------------------|--------------------------|
| Pro, Max, Team, Enterprise *premium* | Incluído até **50% dos limites semanais de uso até 07/jul/2026**; depois disso, via **usage credits**. Fonte: [post de redeploy](https://www.anthropic.com/news/redeploying-fable-5). |
| Enterprise *standard* | **Sem franquia**: usage credits desde o dia 1. Se os créditos não estiverem habilitados, o Fable 5 simplesmente não roda. |
| API / Enterprise por consumo | Metered desde sempre, a $10/$50 por MTok. |
| Marketplaces (Claude Platform on AWS, Claude in Microsoft Foundry) | Faturado em **Claude Consumption Units (CCU)**: 100 CCU = US$ 1,00, convertidos das taxas por token. |

> ⚠️ **O que a Anthropic NÃO publicou** (trate como desconhecido, confira no seu dashboard, não modele em cima): o que "50% dos limites semanais" equivale em tokens/mensagens/dólares por plano, e a conversão crédito→dólar depois de 07/jul. O único número confirmado é a taxa por token da API. Fonte da franquia e do corte: [manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) · [post de redeploy](https://www.anthropic.com/news/redeploying-fable-5).

**Linha do tempo do Fable 5 (contexto do porquê houve dois cortes):** lançado 09/jun/2026 → controles de exportação dos EUA em 12/jun (acesso suspenso globalmente) → controles suspensos em 30/jun → **redeploy global em 01/jul** com nova janela → **corte para usage credits em 07/jul**. O primeiro corte anunciado (23/jun) nunca ocorreu porque o modelo estava offline. Fonte: [anúncio Fable/Mythos](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [redeploy](https://www.anthropic.com/news/redeploying-fable-5).

> 🧭 **Leitura durável (o que este número diz sobre o padrão — Inv. 3):** dois movimentos aqui sobrevivem à rodada específica. Primeiro, **surgiu um tier de fronteira acima do topo anterior** — a hierarquia de capacidade/custo se estende para cima, não só para os lados. Segundo, **o acesso a modelos de fronteira migra de "incluído na assinatura" para "crédito medido"** — sinal de que capacidade de ponta tende a ser precificada por consumo, não por assinatura plana. A decisão que dura não é "qual o preço do Fable"; é a **política de roteamento**: reserve o tier de fronteira para julgamento e problemas difíceis, mande produção/bulk para o balanceado, e escreva essa regra antes de a fatura chegar. O número muda; a disciplina de roteamento é o Invariante 4 operando sobre o Invariante 3.

---

### 1.2 — OpenAI — Família GPT

**Status:** ativa, com tier premium e variantes reduzidas (mini, nano).
**Posicionamento estratégico:** força relativa em raciocínio matemático competitivo e em *computer use*.
**Fonte primária:** [platform.openai.com — models](https://platform.openai.com/docs/models) · [openai.com/news](https://openai.com/news).

> Conteúdo numérico será populado na próxima edição.

---

### 1.3 — Google DeepMind — Família Gemini

**Status:** ativa, com tier premium (Pro) e variante de produção em volume (Flash).
**Posicionamento estratégico:** força relativa em multimodal (vídeo, imagem, áudio) e em contexto longo; pricing premium frequentemente agressivo.
**Fonte primária:** [ai.google.dev/gemini-api/docs/models/gemini](https://ai.google.dev/gemini-api/docs/models/gemini) · [blog.google/technology/ai](https://blog.google/technology/ai).

> Conteúdo numérico será populado na próxima edição.

---

### 1.4 — xAI — Família Grok

**Status:** ativa.
**Posicionamento estratégico:** acesso nativo em tempo real ao X; tolerância maior a temas sensíveis.
**Fonte primária:** [x.ai](https://x.ai/) · [docs.x.ai](https://docs.x.ai/).

---

## SEÇÃO 2 — FAMÍLIAS DE MODELO OPEN WEIGHTS RELEVANTES

| Família | Vendor | Posicionamento estratégico | Fonte primária |
|---------|--------|----------------------------|----------------|
| Llama | Meta | Referência principal em open source ocidental; tier large e médio | [llama.meta.com](https://llama.meta.com/) |
| DeepSeek (V3, R1) | DeepSeek | Custo-benefício extremo; modelo de raciocínio com thinking visível | [api-docs.deepseek.com](https://api-docs.deepseek.com/) |
| Qwen | Alibaba | Open weights chinês com tier premium competitivo | [qwenlm.github.io](https://qwenlm.github.io/) |
| GLM | Z.AI | Open weights chinês com tier premium | [bigmodel.cn](https://bigmodel.cn/) |
| Mistral / Mixtral | Mistral AI | Foco em eficiência; presença europeia | [mistral.ai](https://mistral.ai/) |

> Conteúdo numérico será populado na próxima edição.

---

## SEÇÃO 3 — BENCHMARKS QUE AINDA DISCRIMINAM

### O que cada um mede

| Benchmark | O que mede | Estado de saturação | Fonte primária |
|-----------|------------|---------------------|----------------|
| **MMLU** | Conhecimento geral multitarefa | Saturado (~90%); perdeu poder discriminatório | [paperswithcode.com/sota/multi-task-language-understanding-on-mmlu](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu) |
| **GPQA Diamond** | Raciocínio científico em nível doutorado | Próximo da saturação no topo | [arxiv.org/abs/2311.12022](https://arxiv.org/abs/2311.12022) |
| **SWE-bench Verified** | Issues reais de GitHub resolvidos | Discriminatório; subiu rapidamente em 2024-2026 | [swebench.com](https://www.swebench.com/) |
| **SWE-bench Pro** | Issues mais complexos de GitHub | Discriminatório | [swebench.com](https://www.swebench.com/) |
| **AIME** | Matemática competitiva | Discriminatório em raciocínio formal | [maa.org/student-programs/amc/aime](https://www.maa.org/math-competitions/aime) |
| **ARC-AGI-2** | Raciocínio abstrato sobre padrões visuais | Discriminatório; escapa de memorização | [arcprize.org](https://arcprize.org/) |
| **OSWorld** | *Computer use* (operação de OS como humano) | Discriminatório | [os-world.github.io](https://os-world.github.io/) |
| **Video-MME** | Compreensão de vídeo | Discriminatório em multimodal temporal | [video-mme.github.io](https://video-mme.github.io/) |
| **Humanity's Last Exam** | Expertise de fronteira em campos específicos | Topo do estado da arte; nenhum modelo perto da metade | [agi.safe.ai/about](https://agi.safe.ai/about) |

### Líderes correntes desta rodada

> Conteúdo a popular: por benchmark, qual modelo lidera no momento do snapshot, com link direto ao leaderboard ou paper. **Manter sem atualização paralela em outros documentos da obra.**

---

## SEÇÃO 4 — LEADERBOARDS PÚBLICOS

| Leaderboard | O que oferece | Cuidado de leitura |
|-------------|---------------|--------------------|
| [LMSYS Chatbot Arena](https://lmarena.ai/) | Preferência humana cega entre modelos | Sensível a viés de quem vota; útil para escrita conversacional |
| [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models) | Comparativo multidimensional (capacidade, preço, latência) | Boa síntese; conferir metodologia por eixo |
| [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard) | Benchmarks consolidados | Atualizado com regularidade |
| [LM Council Benchmarks](https://lmcouncil.ai/benchmarks) | Curadoria por usuários enterprise | Útil para casos corporativos |
| [Aider Leaderboards](https://aider.chat/docs/leaderboards/) | Capacidade de edição de código real | Padrão para escolha de modelo de coding agent |
| [SWE-bench leaderboard](https://www.swebench.com/) | Resolução de issues de GitHub | Padrão da indústria para engenharia de software |
| [OSWorld leaderboard](https://os-world.github.io/) | Computer use | Padrão para agentes que operam software |

---

## SEÇÃO 5 — PADRÕES DE PREÇO E LATÊNCIA

Os números por família mudam a cada release e devem ser conferidos no pricing oficial de cada vendor. Para a família Claude, o snapshot corrente está na **Seção 1.1** deste apêndice. A leitura por *tier* abaixo é o padrão que dura; a faixa de proporção entre tiers é o que importa reter.

| Tier | Referência corrente na família Claude (por MTok, 2026-07-05) | Cuidado de leitura |
|------|--------------------------------------------------------------|--------------------|
| Fronteira (Mythos-class) | Fable 5 · $10 / $50 — o mais caro da lista | Reserve para julgamento e horizonte longo; cobrança tende a *usage credits* na assinatura |
| Premium | Opus 4.8 · $5 / $25 (metade do Fable) | Fronteira geral e fallback de segurança do Fable |
| Balanceado | Sonnet 5 · $2 / $10 intro (→ $3 / $15 em set/2026) | Cavalo de batalha de produção; default de Free/Pro |
| Pequeno / velocidade | Haiku 4.5 · $1 / $5 | Um décimo do Fable; volume e latência |
| Open weights self-hosted | TCO varia por hardware | Comparar com proprietário **incluindo** ops |

> Padrão a reter (não o número): a família mantém uma razão **input:output de 1:5** em todos os tiers, e cada degrau de tier costuma dobrar ou halvar o preço do adjacente. É a *forma* da curva de custo — não o valor absoluto — que informa a arquitetura.

Fontes oficiais de pricing (consultar diretamente):
- [Anthropic pricing](https://www.anthropic.com/pricing)
- [OpenAI pricing](https://openai.com/api/pricing/)
- [Google AI Studio pricing](https://ai.google.dev/pricing)
- [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)

---

## SEÇÃO 6 — REGULAÇÃO E MERCADO BR (camada de Apêndice Vivo)

| Tema | Status corrente | Fonte primária |
|------|-----------------|----------------|
| LGPD aplicada a IA | Em vigor; consulta a guias da ANPD | [gov.br/anpd](https://www.gov.br/anpd/pt-br) |
| PL de IA brasileiro | Em tramitação; conferir versão corrente no Senado e Câmara | [congresso.leg.br](https://www.congresso.leg.br/) |
| AI Act (União Europeia) | Em fases de aplicação progressiva | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) |
| NIST AI RMF | Referencial voluntário, com aplicação crescente | [nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| ISO/IEC 42001 | Padrão de sistema de gestão de IA | [iso.org/standard/81230.html](https://www.iso.org/standard/81230.html) |

---

## CONTROLE DE VERSÃO DESTE APÊNDICE

| Versão | Data | O que mudou | Quem atualizou |
|--------|------|-------------|----------------|
| v0.1 | 2026-05-31 | Criação inicial; estrutura definida; fontes mapeadas; populamento numérico pendente | Conselho Editorial |
| v0.2 | 2026-07-05 | Família Claude populada: lineup + preços por MTok (Fable 5, Mythos 5, Opus 4.8, Sonnet 5, Haiku 4.5); tokenizer novo; **modelo de precificação por usage credits** (corte do Fable em 07/jul); tier de fronteira Mythos-class acima de Opus. Fonte oficial por linha. | Editor executivo |
| v0.3 | (próxima) | Números por família proprietária concorrente (GPT, Gemini, Grok) + benchmarks líderes | Autor + revisão |

---

## REFERÊNCIA CRUZADA AOS CAPÍTULOS QUE APONTAM PARA AQUI

- **L1-C01 §1.4.9 e §1.4.10** — Era dos Agentes e Platô da Fronteira (números migrados)
- **L1-C15 §15.3.1, §15.3.3, §15.4, §15.8** — Comparação dos modelos (padrões aqui, números no Apêndice)
- **L1-C18** — Modelos Claude (specs concretas aqui, padrões de família no capítulo)
- **L1-C35** — GitHub Repos (lista volátil aqui, critérios no capítulo)
- **L1-C36** — Economia de Tokens (fórmula no capítulo, faixas de preço aqui)
- **L1-C38** — Futuro da IA (vetores de mudança no capítulo, prazos correntes aqui)

---

> *"Este apêndice é uma foto datada da rodada atual. Os princípios que decidem se um modelo serve à sua operação estão no Livro 1. A combinação dos dois é o que separa decisão informada de decisão de moda."*
