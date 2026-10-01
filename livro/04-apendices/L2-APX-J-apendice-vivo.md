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

**Versão v0.5 — 2026-10-01.**
Segunda renovação de versão, cobrindo o intervalo 12/ago a 01/out. Seis movimentos: (1) **geração 5.1/5.5 da família Claude**: Fable 5.1 (01/set, US$ 10/50, cache read cai para US$ 0,25), **Opus 5.5** (22/set, **US$ 4/20**, 20% abaixo do Opus 5) e **Sonnet 5.5** (28/set, US$ 2/10, mesmo preço do Sonnet 5); Haiku 5.5 anunciado para "as próximas semanas", ainda não lançado; (2) **breaking changes de API comuns à geração**: tool use forçado retorna erro 400, thinking não pode ser desligado no Opus 5.5, blocos de thinking presos a modelo e conversa, nova ferramenta de computer use; (3) **salvaguardas como produto**: Life Sciences Verification Program (17/set), Enterprise Frontier Safeguards (01/set) e fallbacks redesenhados no Fable 5.1; (4) **Model Hardware Standard** em research preview (27/ago), agentes operando instrumentos físicos; (5) novas betas de API (compact on demand, tools definidas na mensagem, efforts por mensagem, mensagens de sistema com escopo de turno); (6) tokenizer e usage credits **reconferidos**: sem mudança documentada. O Sonnet 5 permanece em US$ 2/10, sem janela introdutória listada no pricing oficial.

**Correções em relação à v0.4 (três erros de interpretação ou de fato, registrados por honestidade editorial):**
1. **Usage credits.** A v0.4 juntou Max e Pro numa linha e fixou o corte em 07/jul. O Help Center oficial diz outra coisa: Max e seats premium têm Fable incluído até 50% dos limites semanais, sem data de término; Pro e seats standard usam usage credits, e a promoção que os incluía terminou em 19/jul. A tabela foi reescrita abaixo.
2. **Multiplicador de cache "válido para toda a família".** Deixou de ser verdade em 01/set: Fable 5.1 e Mythos 5.1 leem cache a 0,025× do input.
3. **"Efeito Bruxelas" por cálculo de custo.** A Anthropic declara outra razão para o watermark mundial: limitação técnica de escopo regional, com provisoriedade sinalizada. A leitura durável foi reescrita.

**Histórico v0.4 — 2026-08-12.**
Primeira renovação de versão do apêndice. Quatro movimentos: (1) **Sonnet 5 consolidado em $2/$10** — a Anthropic cancelou o aumento programado para $3/$15 em 01/set/2026 e converteu o preço de lançamento em preço padrão; (2) **recalibração das salvaguardas de biologia do Fable 5** (07/ago): fallbacks de biologia caíram ~85%, e o roteamento bio → Opus 5 ficou restrito a usos dual-use; (3) **marcação de conteúdo gerado (watermarking)**: modelos lançados a partir de 02/ago/2026 embutem watermark no texto e metadados C2PA em arquivos, com aplicação mundial; (4) os placeholders numéricos das famílias concorrentes foram substituídos por referência cruzada ao **L1-APX-J (Trilha do Número)**, consolidando a decisão de fonte única de números da série. Demais preços da família Claude reconferidos na fonte oficial, sem alteração.

> **Como este bloco foi checado:** cada preço e data abaixo tem link para a fonte primária da Anthropic (docs de pricing, posts de anúncio e Help Center), consultada em 2026-08-12. Nenhum número foi estimado.

---

## SEÇÃO 1 — FAMÍLIAS DE MODELO PROPRIETÁRIOS

### 1.1 — Anthropic — Família Claude

**Status:** ativa. A nomenclatura em formas literárias, que começou tripartite (Opus · Sonnet · Haiku) com Claude 3, ganhou em 2026 uma **camada de fronteira acima de Opus**: a classe **Mythos**. O trio de trabalho diário permanece Opus/Sonnet/Haiku; acima dele fica o tier de fronteira, entregue em duas formas — **Fable** (com salvaguardas fortes, para uso geral) e **Mythos** (as mesmas capacidades com salvaguardas de cyber removidas, acesso restrito). *Fable* vem de *fabula* ("aquilo que se conta"), parente do grego *mythos*: a salvaguarda é o que separa os dois nomes.
**Posicionamento estratégico:** força relativa em código, agentes de horizonte longo, escrita executiva, e uma filosofia de alignment pública (Constitutional AI). O tier de fronteira (Mythos-class) é, segundo a própria Anthropic, o mais capaz que já disponibilizaram.
**Fonte primária:** [platform.claude.com — pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [platform.claude.com — models overview](https://platform.claude.com/docs/en/about-claude/models/overview) · [anthropic.com/news](https://www.anthropic.com/news).

#### Lineup e preços correntes (snapshot 2026-10-01)

Preços em USD por milhão de tokens (MTok). "Cache read" = leitura de cache (10% do input). Janela de contexto de 1M tokens no padrão para os modelos de fronteira e Sonnet 5; Haiku opera em janela menor. Fonte da tabela: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing), consultada em 2026-10-01.

| Modelo | ID de API | Input | Output | Batch (in/out) | Cache read | Papel no encaixe (Inv. 4) |
|--------|-----------|-------|--------|----------------|-----------|---------------------------|
| **Fable 5.1** | `claude-fable-5-1` | $10 | $50 | $5 / $25 | $0,25 | Fronteira geral (GA 01/set/2026): problemas difíceis e agentes de horizonte longo. Cache read a 0,025× do input, abaixo dos 0,1× da família. Requer retenção de 30 dias na documentação do modelo (ver nota sobre Enterprise Frontier Safeguards). |
| **Mythos 5.1** *(restrito, Glasswing e programas confiáveis)* | — | $10 | $50 | $5 / $25 | $0,25 | Mesma classe do Fable 5.1 com salvaguardas de cyber e vida-ciências ajustadas para parceiros verificados. Hoje limitado a organizações dos EUA. |
| **Opus 5.5** | `claude-opus-5-5` | $4 | $20 | $2 / $10 | $0,20 | Novo topo do tier Opus (GA 22/set/2026). Segundo a Anthropic, rende como o Fable 5.1 na maioria das tarefas e gera saída mais de 30% mais rápido que o Opus 5. Thinking sempre ligado, effort padrão `medium`. Fast mode (research preview, só Claude API) a $8/$40. |
| **Sonnet 5.5** | `claude-sonnet-5-5` | $2 | $10 | $1 / $5 | $0,20 | Equilíbrio velocidade/inteligência (GA 28/set/2026), mesmo preço do Sonnet 5, tokenizer idêntico ao do Sonnet 5, effort padrão `high`. Sem retirada antes de 28/set/2027. |
| **Fable 5** *(geração anterior)* | `claude-fable-5` | $10 | $50 | $5 / $25 | $1 | Fronteira geral: planejamento, arquitetura e os problemas mais difíceis / horizonte longo. O modelo mais caro da lista. |
| **Mythos 5** *(restrito — [Glasswing](https://anthropic.com/glasswing))* | — | $10 | $50 | $5 / $25 | $1 | Mesmo modelo do Fable, salvaguardas de cyber removidas. Ciberdefesa de fronteira; acesso só a parceiros aprovados. |
| **Opus 5** *(geração anterior)* | `claude-opus-5` | $5 | $25 | $2,50 / $12,50 | $0,50 | Novo topo do tier Opus (GA 24/jul/2026): quase-fronteira à metade do preço do Fable; **default do plano Max**. Recebe o fallback de **biologia** do Fable. Fast mode a $10/$50. |
| **Opus 4.8** | `claude-opus-4-8` | $5 | $25 | $2,50 / $12,50 | $0,50 | Tier Opus da geração anterior; é para onde o Fable **redireciona** requisições de **cyber** e destilação (biologia passou ao Opus 5 em 24/jul). Fast mode a $10/$50. |
| **Sonnet 5** *(geração anterior)* | `claude-sonnet-5` | $2 | $10 | $1 / $5 | $0,20 | Cavalo de batalha de produção; **default de Free e Pro**. Roteie bulk/coding aqui. O preço de lançamento ($2/$10) virou **padrão** em ago/2026: o aumento programado para $3/$15 em 01/set/2026 **foi cancelado** pela Anthropic. |
| **Haiku 4.5** | `claude-haiku-4-5` | $1 | $5 | $0,50 / $2,50 | $0,10 | Volume alto, latência baixa: classificação, extração, roteamento. Um décimo do preço do Fable. |

> **Multiplicadores de cache** (sobre o input base): escrita de 5 min = 1,25×; escrita de 1 h = 2×; leitura (hit) = 0,1×, **exceto Fable 5.1 e Mythos 5.1, em que a leitura é 0,025× (US$ 0,25 por MTok)**. Opus 5.5 lê a US$ 0,20, ou seja, 0,05× do input de US$ 4. Fonte: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing), 01/out/2026.

#### Tokenizer novo (afeta contagem de tokens e, logo, custo)

Os modelos da geração 4.7 em diante — incluindo Opus 5, Fable 5, Mythos 5 e Sonnet 5 — usam um **tokenizer novo**: o mesmo texto passa a mapear para **aproximadamente 30% mais tokens**, variando com o tipo de conteúdo (número oficial da Anthropic). Consequência prática: um custo comparado modelo-a-modelo *por token* subestima o custo real *por tarefa* nesses modelos. A Anthropic calibrou o preço de lançamento do Sonnet 5 (convertido em preço padrão em ago/2026) para que a migração a partir do Sonnet 4.6 seja aproximadamente custo-neutra. Fonte: [nota de rodapé do anúncio do Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5).

#### O modelo de precificação por *usage credits* (mudança estrutural, não só de número)

A novidade que mais importa para orçamento não é um preço — é um **mecanismo de cobrança**. Para os modelos de fronteira (a começar pelo Fable 5), a Anthropic passou a **desacoplar o acesso da inclusão fixa na assinatura**, movendo-o para *usage credits* (crédito de uso medido):

| Plano / superfície | Como o Fable 5 é cobrado |
|--------------------|--------------------------|
| Max, seats *premium* de Team e Enterprise seat-based | Fable 5 e Fable 5.1 fazem **parte padrão do plano**: até 50% dos limites semanais sem custo extra, **sem data de término**. Acima disso, usage credits ou troca de modelo. Fonte: [Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan). |
| Pro e seats *standard* de Team | **Usage credits desde o início**, para os dois modelos. A promoção que incluía o Fable 5 nesses planos terminou em **19/jul/2026 às 23h59 PT** (não em 07/jul). Houve crédito único de compensação para o Fable 5; **não há equivalente para o Fable 5.1**. Mesma fonte. |
| Enterprise *standard* | **Sem franquia**: usage credits desde o dia 1. Se os créditos não estiverem habilitados, o Fable 5 simplesmente não roda. |
| API / Enterprise por consumo | Metered desde sempre, a $10/$50 por MTok. |
| Marketplaces (Claude Platform on AWS, Claude in Microsoft Foundry) | Faturado em **Claude Consumption Units (CCU)**: 100 CCU = US$ 1,00, convertidos das taxas por token. |

> ⚠️ **O que a Anthropic NÃO publicou** (trate como desconhecido, confira no seu dashboard, não modele em cima): o que "50% dos limites semanais" equivale em tokens/mensagens/dólares por plano, e a conversão crédito→dólar depois de 07/jul. O único número confirmado é a taxa por token da API. Fonte da franquia e do corte: [manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) · [post de redeploy](https://www.anthropic.com/news/redeploying-fable-5).

**Linha do tempo do Fable 5 (contexto do porquê houve dois cortes):** lançado 09/jun/2026 → controles de exportação dos EUA em 12/jun (acesso suspenso globalmente) → controles suspensos em 30/jun → **redeploy global em 01/jul** com nova janela → fim da promoção do Fable 5 em Pro e standard em **19/jul** (Max e premium nunca tiveram corte; ver tabela acima). O primeiro corte anunciado (23/jun) nunca ocorreu porque o modelo estava offline. Fonte: [anúncio Fable/Mythos](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [redeploy](https://www.anthropic.com/news/redeploying-fable-5).

**Automatic fallbacks na API (beta, desde 24/jul/2026):** requisições flagged pelos classificadores de segurança em Opus 5 ou Fable 5 podem rotear automaticamente para outro modelo em vez de serem bloqueadas — a requisição sempre chega ao melhor modelo disponível. Em Claude.ai, Claude Code e Cowork, o fallback é o comportamento padrão. Fonte: [anúncio Opus 5](https://www.anthropic.com/news/claude-opus-5). Consequência para arquitetura: a política de roteamento deixou de ser só decisão de custo e virou também decisão de *continuidade* — escreva qual modelo aceita como degradação antes de o classificador decidir por você.

**Recalibração das salvaguardas de biologia do Fable 5 (07/ago/2026):** a Anthropic reescreveu a constituição do classificador de biologia do Fable 5 e reduziu os fallbacks relacionados a biologia em **~85%** (queda total de fallbacks por superfície: ~67% no Claude.ai, ~55% no Cowork, ~17% no Claude Code, ~7% na API). O fallback bio → Opus 5 **permanece**, mas restrito a usos dual-use (virologia, toxicologia, design molecular); saúde cotidiana, interpretação de exames, educação e suporte clínico passam a rodar no próprio Fable 5. Fonte: [Improving Fable 5's biology safeguards](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards). Consequência para arquitetura: **salvaguarda é parâmetro vivo** — a fronteira do que roteia muda por recalibração de classificador, sem release de modelo. Reavalie a política de roteamento também quando o vendor recalibrar salvaguardas, não só quando lançar modelo.

#### Marcação de conteúdo gerado (watermarking) — modelos lançados a partir de 02/ago/2026

A Anthropic assinou o Code of Practice do **Artigo 50(2) do EU AI Act** (transparência de conteúdo gerado por IA) e passou a marcar o que o Claude gera, com anúncio público em 11/ago/2026. Dois mecanismos complementares:

| Mecanismo | Como funciona | Escopo |
|-----------|---------------|--------|
| **Watermark embutido no texto** | Marca estatística imperceptível, tecida no próprio texto no **nível do modelo**; não altera significado nem legibilidade; sobrevive a copy-paste e "pode persistir através de alguma edição" | Todo texto gerado por modelos lançados a partir de 02/ago/2026, em todas as superfícies (API, Claude, Claude Code, Cowork, Tag) e cloud partners |
| **Metadados de proveniência assinados** | Padrão aberto **C2PA**, anexado a arquivos suportados (.svg, .png, .jpg); permite detectar adulteração | Onde o produto suporta processamento de arquivos; pode não estar disponível em toda plataforma |

Aplicação **mundial**, não restrita à União Europeia. Modelos anteriores a 02/ago/2026 estão em período de transição, com suporte a marcação em desenvolvimento. Ferramentas de detecção para usuários e terceiros foram prometidas em documentação técnica futura. Fonte: [How Claude marks AI-generated content](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) (Help Center oficial, 11/ago/2026).

> ⚠️ **Limitação que decide casos de uso: a marca prova *processamento*, não *autoria*.** Texto humano que o Claude revisou, traduziu ou reformatou sai marcado. E ausência de marca não prova ausência de IA: edição pesada, paráfrase, trechos curtos, conversão de formato ou remoção de metadados degradam ou eliminam o sinal. Política de RH, jurídico ou compliance que trate detecção de marca como prova de autoria por IA está errada por construção — nos dois sentidos.

> **Como o watermark funciona (14/ago/2026, segunda camada):** é uma versão do **SynthID-Text** (Google DeepMind, *Nature*, 2024, [doi 10.1038/s41586-024-08025-4](https://www.nature.com/articles/s41586-024-08025-4)), numa família que remonta à proposta de Scott Aaronson em 2022. Não adiciona nada ao texto: **troca a fonte da aleatoriedade** usada para escolher entre palavras igualmente boas. Custo zero em tokens, preço e velocidade. Não identifica usuário, organização nem conversa. **Código e passagens factuais ficam pouco marcados**, porque exatidão não deixa escolha livre para o sinal; comentários de código carregam marca. Tradução leva watermark integral, e revisão leve de texto humano quase não marca. **API de detecção em private preview desde 01/set/2026**, para organizações elegíveis sob a lei europeia (reguladores, imprensa, checadores, pesquisadores, educação, sociedade civil) e para empresas obrigadas a verificar marcação. Fontes: [How Claude's text watermark works](https://www.anthropic.com/news/claude-text-watermark) · [anúncio do Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1).

> 🧭 **Leitura durável (Inv. 3, corrigida em 01/out):** dois padrões sobrevivem a esta rodada. Primeiro, **proveniência de conteúdo virou camada de infraestrutura**, não feature de produto — a marca nasce no modelo e viaja com o conteúdo, o que significa que qualquer pipeline que consuma saída de LLM herda a marca sem escolher. Segundo, é o **efeito Bruxelas por atrito arquitetural**: a obrigação europeia (Art. 50) produziu comportamento global, e a razão declarada pela Anthropic não é cálculo de custo, é limitação técnica. Nas palavras da fonte, a marca é aplicada globalmente "because we don't yet have a durable way to scope it by region", com a promessa de reavaliar. A arquitetura do modelo não separa jurisdição no ponto de geração, e isso é provisório. A decisão que dura: trate proveniência como propriedade do dado, catalogue onde sua operação gera, consome e reemite conteúdo marcado, e nunca use marca como juiz de autoria.

> 🧭 **Leitura durável (o que este número diz sobre o padrão — Inv. 3):** dois movimentos aqui sobrevivem à rodada específica. Primeiro, **surgiu um tier de fronteira acima do topo anterior** — a hierarquia de capacidade/custo se estende para cima, não só para os lados. Segundo, **o acesso a modelos de fronteira migra de "incluído na assinatura" para "crédito medido"** — sinal de que capacidade de ponta tende a ser precificada por consumo, não por assinatura plana. A decisão que dura não é "qual o preço do Fable"; é a **política de roteamento**: reserve o tier de fronteira para julgamento e problemas difíceis, mande produção/bulk para o balanceado, e escreva essa regra antes de a fatura chegar. O número muda; a disciplina de roteamento é o Invariante 4 operando sobre o Invariante 3.

---

#### Cobrança deixou de ser só por token (reconferência de 01/set e 18/set)

| Dimensão | Regra oficial | Consequência |
|----------|---------------|--------------|
| **Runtime de sessão (Managed Agents)** | **US$ 0,08 por session-hour**, medido ao milissegundo e acumulado **só com status `running`**; `idle`, `rescheduling` e `terminated` não contam. Substitui a cobrança por hora de container do code execution. Sem desconto de Batch API e sem preço de cloud parceira. | A unidade de custo de agente passou a incluir o **tempo de vida da sessão**. Um agente que pensa barato mas fica vivo por muito tempo tem custo que planilha de token não captura. |
| **Residência de dados** | `inference_geo: "us"` aplica **1,1×** sobre todas as categorias de token (input, output, escrita e leitura de cache), para Claude 4.6 em diante; padrão `global` a preço normal. Mesmo 1,1× no US Data Zone Standard do Microsoft Foundry. Modelos anteriores retornam erro 400. | Soberania de dados ganhou preço explícito, 10%, o que importa ao leitor brasileiro. |
| **Web search** | US$ 10 por 1.000 buscas, mais os tokens do conteúdo retornado. | Resultado de busca conta como input na rodada e nas seguintes. |
| **Web fetch** | Sem custo adicional, só tokens. Página média de 10 kB, cerca de 2.500 tokens; PDF de paper de 500 kB, cerca de 125.000 tokens. | |
| **Code execution** | Grátis junto de web search ou web fetch. Fora disso, 1.550 horas grátis por organização por mês, depois US$ 0,05 por hora por container, mínimo de 5 minutos por execução. | Cobra mesmo sem chamada da ferramenta quando há arquivos pré-carregados. |
| **Computer use e browser use** | O toolset `computer_toolset_20260801` adiciona cerca de 4.500 tokens de input por requisição; `browser_toolset_20260801`, cerca de 6.600. | Custo fixo por chamada só para declarar a ferramenta. |
| **Fast mode** | Indisponível no Opus 4.7 (erro) e no Opus 4.6 (roda em velocidade padrão e cobra padrão, sem erro). | Falha ruidosa num caso, silenciosa no outro. Não existe Fast mode para Fable. |

Fonte de todo o bloco: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing), consultada em 01/set e reconferida em 01/out/2026.

> 🧭 **Leitura durável (Inv. 3):** o movimento estrutural não é só "de assinatura para crédito medido". O seguinte é maior: **a unidade de cobrança deixou de ser exclusivamente o token e passou a incluir o tempo de vida do agente**. Para workload agêntico, o modelo mental de orçamento por milhão de tokens passou a ser metade da conta. Modele custo de agente em duas dimensões, tokens e horas de sessão, e meça as duas.

#### Geração 5.1 / 5.5: o que mudou entre 12/ago e 01/out

| Data | Evento | Fonte |
|------|--------|-------|
| 01/set/2026 | **Fable 5.1 e Mythos 5.1** em GA (Fable) e acesso restrito (Mythos). Preço de lista inalterado; cache read cai para US$ 0,25. | [anúncio](https://www.anthropic.com/claude-fable-and-mythos-5-1) · [docs](https://platform.claude.com/docs/en/models/fable-5-1/overview) |
| 22/set/2026 | **Opus 5.5**: US$ 4/20 (Opus 5 era US$ 5/25), cache read US$ 0,20, Batch US$ 2/10, Fast mode US$ 8/40. | [anúncio](https://www.anthropic.com/claude-opus-5-5) · [docs](https://platform.claude.com/docs/en/models/opus-5-5/overview) |
| 28/set/2026 | **Sonnet 5.5**: preço igual ao do Sonnet 5, 512 tokens de cache mínimo (era 1.024). | [docs](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) |
| a anunciar | **Haiku 5.5**: "nas próximas semanas" segundo a página do Opus 5.5. Haiku 4.5 segue sendo o tier pequeno. | [anúncio Opus 5.5](https://www.anthropic.com/claude-opus-5-5) |

**Datas de retirada documentadas:** Fable 5.1 não antes de 01/set/2027; Opus 5.5 não antes de 22/set/2027; Sonnet 5.5 não antes de 28/set/2027. Nenhuma deprecação do Opus 5 ou do Sonnet 5 foi anunciada nas páginas consultadas.

**Janela de contexto e saída:** 1M de tokens de contexto e 128K de saída nos três modelos 5.x (300K de saída em Batch API beta no Opus 5.5 e no Sonnet 5.5). Knowledge cutoff de junho de 2026 para a geração 5.x; Haiku 4.5 mantém fevereiro de 2025.

**Preço relativo:** o Opus 5.5 custa 40% do Fable 5.1 no input e no output. A razão input:output de 1:5 se mantém em todos os tiers (Fable 10:50, Opus 4:20, Sonnet 2:10, Haiku 1:5). O que deixou de valer é a ideia de que "cada degrau dobra ou divide por dois": a distância Fable para Opus agora é de 2,5×, e Opus 5.5 para Sonnet 5.5 é de 2×.

#### Breaking changes de API da geração 5.x (o que muda a sua arquitetura, não só a sua fatura)

| Mudança | Aplica-se a | Consequência prática |
|---------|-------------|----------------------|
| **Tool use forçado retorna erro 400** (`tool_choice` `any` ou `tool`) | Fable 5.1, Opus 5.5, Sonnet 5.5 | Migrar para `auto` com `strict: true` ou structured outputs. Pipelines que dependiam de "sempre chamar esta ferramenta" quebram. |
| **Thinking não pode ser desligado** no Opus 5.5 | Opus 5.5 (e Fable 5.1, sempre ligado) | O controle passa a ser só o `effort`. No Sonnet 5.5 o modo mínimo é `between_tools`. |
| **Effort recalibrado** | Opus 5.5 e Sonnet 5.5 | O mesmo nível não gasta o mesmo thinking que na geração anterior. Refazer varredura de effort antes de fixar custo. Padrões: Opus 5.5 `medium`, Sonnet 5.5 `high`, Fable 5.1 `high`. |
| **Blocos de thinking presos a modelo e conversa** | Toda a geração | Histórico precisa ser append-only; editar system, tools ou turnos anteriores invalida os blocos seguintes. O Sonnet 5.5 não lê thinking do Opus 5, Opus 5.5 nem Fable/Mythos. |
| **Texto entre tool calls vira bloco de thinking** | Opus 5.5 e Sonnet 5.5 | Com `display: "omitted"` (padrão), apps que mostram progresso ficam mudos. Usar `display: "text"` ou `updates`. |
| **Nova ferramenta de computer use** `computer_toolset_20260801` | Opus 5.5 e Sonnet 5.5 (Claude API e Google Cloud) | A `computer_20251124` deixa de ser aceita nessas superfícies; Bedrock ainda aceita. |
| **Advisor tool** | Sonnet 5.5 como executor | Passa a exigir Mythos, Fable, Opus 5 ou 5.5, ou Sonnet 5.5 como advisor. Opus 4.8 e Sonnet 5 saem da lista. |
| **Categorias de recusa em `stop_details`** | Geração 5.x | `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`. No Sonnet 5, o fallback server-side cobre só `cyber` e `frontier_llm`. |

Fontes: [what's new Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) · [what's new Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5) · [what's new Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1).

> 🧭 **Leitura durável (Inv. 3 e 4):** a mudança que mais custa em migração não é o preço, é o **contrato de comportamento**. Quando o modelo deixa de aceitar tool use forçado e passa a decidir quanto pensar, o seu sistema perde um ponto de controle determinístico e ganha outro, o `effort`. O padrão que dura: trate a escolha de modelo como configuração versionada com suíte de avaliação própria, e rode a suíte a cada release, mesmo quando o preço fica igual ou cai.

#### Betas de API da geração 5.x

| Recurso | Header ou parâmetro | Observação |
|---------|---------------------|------------|
| Compact on demand | `compact-2026-09-04` | Compactação de contexto sob demanda. |
| Tools definidas na mensagem | `inline-tools-2026-09-15` | Definição completa de ferramenta no meio da conversa. |
| Effort por mensagem | `mid-conversation-output-config-2026-07-01` | Muda a profundidade de raciocínio sem quebrar o prompt cache. |
| Mensagem de sistema com escopo de turno | `mid-conversation-system-clear-at-2026-08-21` | Instrução válida só até a próxima mensagem do usuário. |
| Progress updates | `thinking-display-updates-2026-08-18` | Mostra atualizações legíveis entre tool calls sem expor o raciocínio. |
| Controles de binding de thinking | `thinking-binding-controls-2026-08-01` | Reporta blocos descartados em `input_transformations`. |

Betas mudam sem aviso longo. Confira no console antes de depender.

#### Salvaguardas como produto (set/2026)

- **Life Sciences Verification Program (17/set/2026):** acesso a Mythos, Opus e Sonnet com salvaguardas de biologia mais permissivas, em dois níveis. **Standard**, renovação anual, cobre a maior parte de P&D, manufatura e desenvolvimento clínico. **High-risk**, renovação semestral, remove as salvaguardas de vida-ciências em projetos específicos (hoje limitado para Mythos). O bloqueio em tempo real dá lugar a monitoramento offline com retenção de 30 dias. Salvaguardas de cyber seguem ativas. Disponível via API, Enterprise e Team; planos Pro e Max individuais ainda não. Fonte: [anthropic.com/news/life-sciences-verification-program](https://www.anthropic.com/news/life-sciences-verification-program).
- **Enterprise Frontier Safeguards (01/set/2026):** combina retenção zero de dados com detecção de uso indevido. Os dados de monitoramento ficam na nuvem do cliente (AWS, Azure ou Google Cloud), com chaves gerenciadas pelo cliente, e os alertas vão direto ao time de segurança do cliente. A Anthropic não cobra pelo recurso; a nuvem cobra armazenamento. Disponibilidade em fases a partir do outono de 2026, com acesso interino de retenção zero nos modelos Fable 5 e 5.1. Fonte: [anthropic.com/news/enterprise-frontier-safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards).
- **Divergência a resolver antes de publicar:** a documentação do Fable 5.1 diz que exige retenção de 30 dias, sem opção de retenção zero, enquanto o anúncio do EFS fala em retenção zero interina no Fable 5.1. Tratar como **desconhecido** até a Anthropic reconciliar as duas páginas.
- **Fallback do Fable 5.1:** o anúncio diz que usos dual-use (teste de intrusão, geração de exploit, biologia de nível pesquisa) são redirecionados a modelos Opus. A redução de falsos positivos de cyber é de cerca de 60% frente ao Fable 5. Não confirmei qual Opus (5 ou 5.5) recebe cada categoria; verificar no doc de refusals and fallback.
- **Anti-destilação com efeito em integração (01/set):** contas de API criadas a partir de 01/set não podem editar contexto anterior do Claude em conversa multi-turn preservando o transcript de thinking; contas existentes ainda não são afetadas, e a Anthropic diz que a regra se estenderá em releases futuros. É mudança de política de plataforma com impacto em código de integração, sem mudança de preço. Fonte: [anúncio do Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1).
- **Effort por superfície:** segundo o anúncio, o Fable 5.1 usa effort High por padrão no Claude Code e Medium no Cowork e no Claude.ai; em Low ou Medium a Anthropic afirma resultado igual ou melhor que o do Fable 5 a custo bem menor. O mesmo modelo custa diferente por superfície sem escolha do usuário.
- **Cache read abaixo do Opus:** com US$ 0,25 por MTok no Fable 5.1 contra US$ 0,50 no Opus 5 (US$ 0,20 no Opus 5.5), o Fable 5.1 lê cache por metade do preço do Opus 5 e fica próximo do Opus 5.5. Para agente com contexto pesado, a política de roteamento por preço de headline deixa de refletir o custo real.
- **Proveniência de conteúdo:** a página do Fable 5.1 confirma watermark estatístico de texto em toda saída e Content Credentials C2PA assinadas para imagem, vídeo e áudio gerados via Files API.

> 🧭 **Leitura durável (Inv. 3):** salvaguarda virou **produto com tiers, contrato e auditoria**. Isso muda a pergunta de compras: não basta perguntar "qual modelo", é preciso perguntar "com qual regime de retenção, monitoramento e verificação". Escreva isso no contrato antes de a primeira requisição bloqueada acontecer em produção.

#### Model Hardware Standard (27/ago/2026, research preview)

Especificação compartilhada para agentes de IA operarem dispositivos físicos por meio de drivers padronizados com primitivas de leitura e escrita, compatível com MCP e agnóstica de modelo. Parceiros citados: Genentech, Baker Lab e Pinglay Lab (UW), Carnegie Mellon, HHMI Janelia, QuEra, Tetsuwan Scientific; apoio de AWS, Danaher, QIAGEN, Tecan, Universal Robots e outros. Ainda não é open source; avaliações de segurança em andamento. Fonte: [anthropic.com/news/model-hardware-standard-research-preview](https://www.anthropic.com/news/model-hardware-standard-research-preview). Leitura durável: a fronteira de risco de agentes deixa de ser só dado e código e passa a incluir atuação física, o que puxa governança para o nível de dispositivo.

#### Outros anúncios do produto (12/ago a 01/out)

| Data | Item | Fonte |
|------|------|-------|
| 14/ago | "How Claude's text watermark works" | [anthropic.com/news](https://www.anthropic.com/news) |
| 25/ago | Memory expandida em Cowork e chat, com gestão por "Topics" e opção de excluir temas sensíveis | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 06/ago | Escaneamento de segurança de skills e plugins de terceiros para Enterprise | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 10/set | Smart reports (beta) para Enterprise, análise do uso do time | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 15/set | Plugin Salesforce (beta) com 37 skills de vendas | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 18/set | Parceria com a Accenture em avaliação embutida | [anthropic.com/news](https://www.anthropic.com/news) |
| 01/out | Barclays escala o Claude em operações | [anthropic.com/news](https://www.anthropic.com/news) |

#### Usage credits e tokenizer: reconferência de 01/out

Os release notes de 12/ago a 01/out não registram mudança em usage credits nem em modelo default por plano. O tokenizer da geração 4.7 em diante (cerca de 30% mais tokens) segue documentado no pricing oficial, que agora inclui Fable 5.1 e Mythos 5.1. O Sonnet 5.5 usa tokenizer idêntico ao do Sonnet 5. **O tokenizer do Opus 5.5 e do Fable 5.1 frente ao Opus 5 não está documentado nas páginas consultadas: tratar como desconhecido e medir no seu próprio tráfego.** Defaults de plano (Max com Opus 5, Free e Pro com Sonnet 5) **não foram reconfirmados** nesta rodada.

---

### 1.2 — OpenAI — Família GPT

**Status:** ativa, com tier premium e variantes reduzidas (mini, nano).
**Posicionamento estratégico:** força relativa em raciocínio matemático competitivo e em *computer use*.
**Fonte primária:** [platform.openai.com — models](https://platform.openai.com/docs/models) · [openai.com/news](https://openai.com/news).

> **Números desta família:** consulte o **L1-APX-J (Trilha do Número)**, a camada única de números multi-vendor da série, com preço, janela, release e fonte primária por linha. Decisão editorial (v0.4): este apêndice mantém populamento numérico apenas da família Claude; duplicar números entre os dois apêndices criaria dois pontos de manutenção que inevitavelmente divergiriam.

---

### 1.3 — Google DeepMind — Família Gemini

**Status:** ativa, com tier premium (Pro) e variante de produção em volume (Flash).
**Posicionamento estratégico:** força relativa em multimodal (vídeo, imagem, áudio) e em contexto longo; pricing premium frequentemente agressivo.
**Fonte primária:** [ai.google.dev/gemini-api/docs/models/gemini](https://ai.google.dev/gemini-api/docs/models/gemini) · [blog.google/technology/ai](https://blog.google/technology/ai).

> **Números desta família:** consulte o **L1-APX-J (Trilha do Número)**, a camada única de números multi-vendor da série, com preço, janela, release e fonte primária por linha. Decisão editorial (v0.4): este apêndice mantém populamento numérico apenas da família Claude; duplicar números entre os dois apêndices criaria dois pontos de manutenção que inevitavelmente divergiriam.

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

> **Números desta família:** consulte o **L1-APX-J (Trilha do Número)**, a camada única de números multi-vendor da série, com preço, janela, release e fonte primária por linha. Decisão editorial (v0.4): este apêndice mantém populamento numérico apenas da família Claude; duplicar números entre os dois apêndices criaria dois pontos de manutenção que inevitavelmente divergiriam.

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

> **Líderes por benchmark:** consulte a Seção 2 do **L1-APX-J (Trilha do Número)**, que mantém a tabela de líderes com score, data de captura e fonte por linha. Decisão editorial (v0.4): uma única tabela de líderes na série — manter duas atualizações paralelas do mesmo número é o erro que este apêndice existe para evitar.

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

| Tier | Referência corrente na família Claude (por MTok, 2026-10-01) | Cuidado de leitura |
|------|--------------------------------------------------------------|--------------------|
| Fronteira (Mythos-class) | Fable 5.1 · $10 / $50 (cache read $0,25) — o mais caro da lista | Reserve para julgamento e horizonte longo; cobrança tende a *usage credits* na assinatura |
| Premium | Opus 5.5 · $4 / $20 (40% do Fable 5.1); Opus 5 e Opus 4.8 seguem a $5 / $25 | Quase-fronteira; fallback de dual-use do Fable. Refaça a varredura de effort antes de comparar custo por tarefa |
| Balanceado | Sonnet 5.5 · $2 / $10 (mesmo preço do Sonnet 5; aumento de set/2026 cancelado) | Cavalo de batalha de produção; confira o default de Free/Pro no seu plano |
| Pequeno / velocidade | Haiku 4.5 · $1 / $5 | Um décimo do Fable; volume e latência |
| Runtime de sessão (Managed Agents) | US$ 0,08 por session-hour em `running`, fora do eixo de token | Segundo eixo de custo de agente; sem Batch e sem cloud parceira |
| Open weights self-hosted | TCO varia por hardware | Comparar com proprietário **incluindo** ops |

> Padrão a reter (não o número): a família mantém uma razão **input:output de 1:5** em todos os tiers, no eixo de token; existe agora um segundo eixo (runtime de sessão). A proporcionalidade também **quebrou no cache read**: US$ 0,25 no Fable 5.1, US$ 0,50 no Opus 5, US$ 0,20 no Opus 5.5. A regra antiga de que cada degrau dobra ou divide por dois **deixou de valer** com o Opus 5.5 (degrau Fable para Opus de 2,5×). É a *forma* da curva de custo — não o valor absoluto — que informa a arquitetura.

Fontes oficiais de pricing (consultar diretamente):
- [Anthropic pricing](https://www.anthropic.com/pricing)
- [OpenAI pricing](https://openai.com/api/pricing/)
- [Google AI Studio pricing](https://ai.google.dev/pricing)
- [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)

---

## SEÇÃO 6 — REGULAÇÃO E MERCADO BR (camada de Apêndice Vivo)

| Tema | Status corrente | Fonte primária |
|------|-----------------|----------------|
| LGPD aplicada a IA | Em vigor. ANPD foi transformada em agência pela MP aprovada no Senado em fev/2026 (200 cargos). Nenhum ato novo sobre IA encontrado desde ago/2026, exceto a metodologia de testagem do Sandbox Regulatório (19/ago, CIAAM/USP, seis ciclos em três blocos). Número da lei de conversão (Lei nº 15.352/2026) **a confirmar no Planalto** | [gov.br/anpd](https://www.gov.br/anpd/pt-br) · [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2026/02/24/senado-aprova-mp-que-transforma-a-anpd-em-agencia-e-cria-200-cargos) |
| PL de IA brasileiro | PL 2338/2023 em Comissão Especial na Câmara, regime de prioridade. Último ato na ficha: **02/set/2026**, Mesa apensou proposições (37 apensadas). Situação oficial **"Aguardando Parecer do(a) Relator(a)"** (consultada em 01/set, 18/set e 01/out); apensações pela Mesa em 01/set (PL 3060/2026) e 02/set (PL 1542/2026); última ação anterior em 17/06/2026. O parecer de maio citado em material anterior **não consta como apresentado** na ficha. Adiamento para depois das eleições é declaração reportada por imprensa, não fato de tramitação. Sem data de votação. Retorna ao Senado após a Câmara | [ficha da Câmara](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) |
| AI Act (União Europeia) | Aplicação geral desde 02/ago/2026 (Art. 50 incluído; watermarking do Claude é materialização direta). High-risk Annex III adiado para 02/dez/2027 e Annex I para 02/ago/2028 pelo Omnibus; sistemas já no mercado antes de 02/ago/2026 têm até 02/dez/2026 para o Art. 50(2). Número do regulamento (UE) 2026/1744 e data de publicação **a reconfirmar no Jornal Oficial** | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) · [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) |
| NIST AI RMF | Referencial voluntário, com aplicação crescente | [nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| ISO/IEC 42001 | Padrão de sistema de gestão de IA | [iso.org/standard/81230.html](https://www.iso.org/standard/81230.html) |

---

## CONTROLE DE VERSÃO DESTE APÊNDICE

| Versão | Data | O que mudou | Quem atualizou |
|--------|------|-------------|----------------|
| v0.1 | 2026-05-31 | Criação inicial; estrutura definida; fontes mapeadas; populamento numérico pendente | Conselho Editorial |
| v0.2 | 2026-07-05 | Família Claude populada: lineup + preços por MTok (Fable 5, Mythos 5, Opus 4.8, Sonnet 5, Haiku 4.5); tokenizer novo; **modelo de precificação por usage credits** (corte do Fable em 07/jul); tier de fronteira Mythos-class acima de Opus. Fonte oficial por linha. | Editor executivo |
| v0.3 | 2026-08-03 | **Claude Opus 5** adicionado (GA 24/jul, $5/$25, default do Max); fallback do Fable ajustado (bio → Opus 5, cyber → Opus 4.8); *automatic fallbacks* na API (beta); tokenizer quantificado (~30%); demais preços reconferidos sem alteração. | Editor executivo |
| v0.4 | 2026-08-12 | **Sonnet 5 consolidado em $2/$10** (aumento de 01/set/2026 **cancelado** pela Anthropic; preço de lançamento virou padrão); recalibração das salvaguardas de biologia do Fable 5 (07/ago: fallbacks bio −85%, roteamento bio → Opus 5 restrito a dual-use); **marcação de conteúdo gerado** (watermark embutido no texto + metadados C2PA em arquivos, modelos ≥ 02/ago/2026, aplicação mundial, Art. 50(2) do EU AI Act); placeholders de famílias concorrentes e benchmarks substituídos por referência cruzada ao L1-APX-J (fonte única de números da série); Seção 6 atualizada (Reg. UE 2026/1744). | Editor executivo |
| v0.5 | 2026-10-01 | **Geração 5.1/5.5**: Fable 5.1 (01/set), Opus 5.5 (22/set, $4/$20) e Sonnet 5.5 (28/set); tabela de lineup e Seção 5 reescritas; breaking changes de API (tool use forçado, thinking, computer use, advisor); betas de API; salvaguardas como produto (LSVP, EFS); Model Hardware Standard; anúncios de produto; reconferência de usage credits e tokenizer (sem mudança); Seção 6 revisada (EU Omnibus, PL 2338, ANPD). Pendências sinalizadas no texto. | Editor executivo (proposta, aguarda aprovação) |
| v0.6 | (próxima) | Haiku 5.5 (lançamento), tokenizer do Opus 5.5 e do Fable 5.1, reconciliação retenção 30 dias versus retenção zero, defaults de plano, detecção de marcas, scores auditados | Autor + revisão |

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
