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

## DATA DO SNAPSHOT INICIAL

**Versão v0.1 — 2026-05-31.**
Primeira edição operacional. Cobertura inicial focada nas três famílias frontier proprietárias, principais open-weights e benchmarks que ainda discriminam capacidade. Será expandida conforme a demanda da operação.

---

## SEÇÃO 1 — FAMÍLIAS DE MODELO PROPRIETÁRIOS

### 1.1 — Anthropic — Família Claude

**Status:** ativa, com três tiers canônicos (Opus · Sonnet · Haiku).
**Posicionamento estratégico:** força relativa em código, escrita executiva, filosofia de alignment pública (Constitutional AI).
**Fonte primária:** [docs.claude.com — models](https://docs.claude.com/en/docs/about-claude/models) · [anthropic.com/news](https://www.anthropic.com/news) · [Anthropic Release Timeline](https://hidekazu-konishi.com/entry/anthropic_claude_model_release_timeline.html).

> **Versões correntes desta rodada e benchmarks correspondentes ficam para atualização no próximo snapshot, com link individual por afirmação.** Esta é a estrutura — o conteúdo numérico vivo será populado conforme o autor confirmar fontes oficiais por linha.

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

> Esta seção será populada com snapshots por tier (premium, balanceado, pequeno) e por família, com fonte por linha. Os números mudam frequentemente e devem ser conferidos no pricing page oficial de cada vendor.

| Tier | Faixa típica observada | Cuidado |
|------|------------------------|---------|
| Premium proprietário | Faixa significativamente mais cara que balanceado | Variação alta entre vendors; comparar input vs output |
| Balanceado proprietário | Faixa intermediária | Cavalo de batalha da maioria das aplicações |
| Pequeno proprietário | Significativamente mais barato | Cobre o grosso de tarefas estruturadas |
| Open weights self-hosted | TCO total varia por hardware | Comparar com proprietário considerando ops |

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
| v0.2 | (próxima) | Primeira rodada de números por família proprietária + benchmarks líderes | Autor + revisão |
| v0.3 | (mensal) | Atualização padrão | Autor |

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
