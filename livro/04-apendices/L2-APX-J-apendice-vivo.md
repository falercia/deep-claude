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

**Versão v0.8 — 2026-11-25.**
Estado da família Claude em 25 de novembro de 2026, conferido nas fontes oficiais. **O topo baixou de preço pela primeira vez:** o Fable 5.2 e o Mythos 5.2, lançados em 09/nov, custam US$ 8/40 por MTok, 20% abaixo do Fable 5.1, com leitura de cache a US$ 0,20 e, pela primeira vez no tier de fronteira, Fast mode (US$ 16/80). Na mesma janela: o Fast mode do Opus 4.8 é removido em 30/nov, o Sonnet 4.5 sai da API em 30/nov, o Opus 4.5 foi depreciado em 23/nov com saída em 22/jan/2027, e a página de deprecações passou a publicar piso de retirada para Fable 5, Opus 4.8, Opus 5 e Sonnet 5. No produto: Claude Sheets e Whiteboards em beta e Claude Data em GA (10/nov), e Claude Meetings em beta no Google Meet para Team e Enterprise (12/nov). Fora do preço: marca d'água estendida a sete modelos anteriores (03/nov e 16/nov), Linked billing em beta (17/nov), Enterprise Frontier Safeguards em beta com retenção zero para organizações elegíveis (23/nov) e Managed Agents auto-hospedado (12/nov). Opus 5.5, Sonnet 5.5, Haiku 5.5, Sonnet 5, Opus 5 e Haiku 4.5 sem mudança de preço. Fontes: [pricing](https://platform.claude.com/docs/en/about-claude/pricing), [visão geral de modelos](https://platform.claude.com/docs/en/about-claude/models/overview), [deprecações](https://platform.claude.com/docs/en/about-claude/model-deprecations), [notas de versão](https://platform.claude.com/docs/pt-BR/release-notes/overview), [anúncio do Fable 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) e [Help Center](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan) e [artigo de produto de 10/nov](https://claude.com/resources/articles/sheets-whiteboards-data), todos lidos em 25/nov/2026.

**Histórico v0.7 — 2026-11-01.**
Reconferência mensal contra as fontes oficiais, cobrindo 09/out a 01/nov. **Sem mudança de preço, de lineup ou de mecanismo de cobrança na família Claude.** Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, Sonnet 5, Opus 5 e Haiku 4.5 conferem linha a linha com a [página oficial de pricing](https://platform.claude.com/docs/en/about-claude/pricing) e com a [visão geral de modelos](https://platform.claude.com/docs/en/about-claude/models/overview); nenhum modelo novo, e Fable 5.1 segue como o de numeração mais alta. Multiplicadores de cache reconfirmados (0,025× no Fable 5.1 e no Mythos 5.1, 0,05× no Opus 5.5 e no Sonnet 5.5, 0,1× nos demais). A página de pricing atribui o tokenizer novo (cerca de 30% mais tokens) aos "Claude 4.7 e posteriores", o que inclui Opus 5.5 e Fable 5.1 e encerra essa pendência pela leitura do texto, sem número específico por modelo. Não há janela introdutória listada. Posts do período sem efeito na tabela, segundo o [newsroom](https://www.anthropic.com/news): acordo com a GSA (27/10, desconto de 40% para parceiros governamentais em Claude Enterprise, Claude for Government e API, que não altera os preços públicos), protocolo do S-1 (26/10), defesas contra destilação (12/10) e atualização sobre avaliadores independentes (15/10). Concorrentes e regulação: ver L1-APX-J. **Pendentes (declaradas):** conteúdo dos posts de 06/10 e 08/10 (Cyber Verification Program, Usage Policy 2026, Cyber Mission), usage credits no Help Center e a página de deprecações, que não foram lidos nesta rodada.

**Histórico v0.6 — 2026-10-09.**
Reconferência mensal contra as fontes oficiais, cobrindo 01/out a 09/out. Dois movimentos e uma correção: (1) **Haiku 5.5 lançado em 07/10/2026**, `claude-haiku-5-5`, US$ 0,10/0,50 até 100k tokens de prompt e US$ 0,50/2,50 acima, cache read US$ 0,01 e US$ 0,05, contexto de 1M, retirada não antes de 07/10/2027; é o primeiro Haiku com effort ajustável e com o tokenizer novo (cerca de 30% mais tokens que o Haiku 4.5); (2) novos posts de política e segurança da Anthropic (Cyber Verification Program ampliado em 06/10, Usage Policy 2026 e Cyber Mission em 08/10), cujo conteúdo ainda não foi lido; (3) **correção:** o cache read do Sonnet 5.5 é US$ 0,10 (0,05× do input), e não US$ 0,20 como constava na v0.5. Fable 5.1, Opus 5.5, Sonnet 5.5, Sonnet 5 e Haiku 4.5 reconferidos, sem mudança de preço. Usage credits: sem registro novo em anthropic.com/news; Help Center não reconferido nesta rodada.

**Histórico v0.5 — 2026-10-01.**
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

#### Lineup e preços correntes (snapshot 2026-11-25)

Preços em USD por milhão de tokens (MTok). "Cache read" = leitura de cache (o multiplicador varia por modelo; ver nota abaixo da tabela). Janela de contexto de 1M tokens no padrão para os modelos de fronteira e Sonnet 5; Haiku 4.5 opera em janela menor; o Haiku 5.5 tem 1M. Fonte da tabela: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing) e [visão geral de modelos](https://platform.claude.com/docs/en/about-claude/models/overview), lidas em 2026-11-25. A Anthropic recomenda o Opus 5.5 como ponto de partida para a maioria das cargas e o Fable 5.2 para raciocínio difícil e trabalho agêntico de horizonte longo.

| Modelo | ID de API | Input | Output | Batch (in/out) | Cache read | Papel no encaixe (Inv. 4) |
|--------|-----------|-------|--------|----------------|-----------|---------------------------|
| **Fable 5.2** | `claude-fable-5-2` | $8 | $40 | $4 / $20 | $0,20 | Fronteira geral (09/nov/2026): raciocínio exigente e agentes de horizonte longo. Primeiro corte de preço do tier, 20% abaixo do Fable 5.1. Cache read a 0,025× do input. **Fast mode a $16/$80**, até 2,5× mais rápido, com `speed: "fast"` e sem cabeçalho beta. Effort padrão `high`, thinking adaptativo sempre ligado. Exige retenção de 30 dias, salvo autorização expressa (ver Enterprise Frontier Safeguards). |
| **Mythos 5.2** *(restrito: Cyber Verification Program, Life Sciences Verification Program ou Claude Security no Enterprise)* | `claude-mythos-5-2` | $8 | $40 | $4 / $20 | $0,20 | Mesmo modelo do Fable 5.2, com salvaguardas ajustadas para organizações verificadas. Fast mode a $16/$80 só para essas organizações. |
| **Fable 5.1** *(geração anterior)* | `claude-fable-5-1` | $10 | $50 | $5 / $25 | $0,25 | Fronteira da geração anterior (01/set/2026), agora 25% mais cara que o Fable 5.2. Retirada não antes de 01/set/2027. |
| **Mythos 5.1** *(geração anterior, restrito)* | — | $10 | $50 | $5 / $25 | $0,25 | Mesma classe do Fable 5.1 com salvaguardas de cyber e vida-ciências ajustadas para parceiros verificados. Hoje limitado a organizações dos EUA. |
| **Opus 5.5** | `claude-opus-5-5` | $4 | $20 | $2 / $10 | $0,20 | Topo do tier Opus (GA 22/set/2026) e **modelo recomendado como ponto de partida**. Segundo a Anthropic, rende como o Fable 5.1 na maioria das tarefas e gera saída mais de 30% mais rápido que o Opus 5. Thinking sempre ligado, effort padrão `medium`. Fast mode (research preview, só Claude API) a $8/$40. |
| **Sonnet 5.5** | `claude-sonnet-5-5` | $2 | $10 | $1 / $5 | $0,10 | Equilíbrio velocidade/inteligência (GA 28/set/2026), mesmo preço do Sonnet 5, tokenizer idêntico ao do Sonnet 5, effort padrão `high`. Sem retirada antes de 28/set/2027. |
| **Fable 5** *(geração anterior)* | `claude-fable-5` | $10 | $50 | $5 / $25 | $1 | Fronteira de jun/2026 (geração anterior). Mesmo preço de lista do Fable 5.1, com cache read quatro vezes mais caro: não há motivo de custo para manter carga nova aqui. Retirada não antes de 09/jun/2027. |
| **Mythos 5** *(restrito — [Glasswing](https://anthropic.com/glasswing))* | — | $10 | $50 | $5 / $25 | $1 | Mesmo modelo do Fable, salvaguardas de cyber removidas. Ciberdefesa de fronteira; acesso só a parceiros aprovados. |
| **Opus 5** *(geração anterior)* | `claude-opus-5` | $5 | $25 | $2,50 / $12,50 | $0,50 | Tier Opus de julho/2026. Recebe a resposta das requisições de **biologia** bloqueadas no Fable, e de um pequeno conjunto de temas de P&D em IA no Fable 5.2. Fast mode a $10/$50 (research preview). Retirada não antes de 24/jul/2027. |
| **Opus 4.8** | `claude-opus-4-8` | $5 | $25 | $2,50 / $12,50 | $0,50 | Tier Opus da geração anterior; continua recebendo a resposta das requisições de **cyber** bloqueadas no Fable, inclusive no 5.2 (biologia vai ao Opus 5). **Fast mode depreciado, removido em 30/nov/2026**; a migração indicada é o Opus 5.5. Retirada do modelo não antes de 28/mai/2027. |
| **Sonnet 5** *(geração anterior)* | `claude-sonnet-5` | $2 | $10 | $1 / $5 | $0,20 | Cavalo de batalha de produção; **default de Free e Pro**. Roteie bulk/coding aqui. O preço de lançamento ($2/$10) virou **padrão** em ago/2026: o aumento programado para $3/$15 em 01/set/2026 **foi cancelado** pela Anthropic. |
| **Haiku 5.5** | `claude-haiku-5-5` | $0,10 (≤100k) / $0,50 (>100k) | $0,50 / $2,50 | $0,05 / $0,25 (≤100k) | $0,01 (≤100k) / $0,05 | Tier pequeno (GA 07/10/2026): volume e latência, primeiro Haiku com effort ajustável. Preço escalonado pelo tamanho do prompt (input, cache reads e writes), por requisição. Contexto de 1M, saída de 128K, thinking adaptativo com effort padrão `medium`. Retirada não antes de 07/10/2027. |
| **Haiku 4.5** *(geração anterior)* | `claude-haiku-4-5` | $1 | $5 | $0,50 / $2,50 | $0,10 | Volume alto, latência baixa. A página de deprecações lista o modelo como ativo com piso "not sooner than" 15/out/2026, data já vencida: não há aposentadoria anunciada, mas trate a migração para o Haiku 5.5 como planejada, não opcional. |

> **Multiplicadores de cache** (sobre o input base): escrita de 5 min = 1,25×; escrita de 1 h = 2×; leitura (hit) = 0,1×, **exceto no tier de fronteira**: Fable 5.2 e Mythos 5.2 leem a 0,025× (US$ 0,20 por MTok), Fable 5.1 e Mythos 5.1 também a 0,025× (US$ 0,25). Opus 5.5 lê a US$ 0,20 e o Sonnet 5.5 a US$ 0,10, ambos 0,05× do input. Na prática, a regra de 10% vale hoje só para a geração anterior. Fonte: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing), lida em 25/nov/2026.

#### Tokenizer novo (afeta contagem de tokens e, logo, custo)

Os modelos da geração 4.7 em diante — incluindo toda a geração 5.x, do Haiku 5.5 ao Fable 5.2 — usam um **tokenizer novo**: o mesmo texto passa a mapear para **aproximadamente 30% mais tokens**, variando com o tipo de conteúdo (número oficial da Anthropic). Consequência prática: um custo comparado modelo-a-modelo *por token* subestima o custo real *por tarefa* nesses modelos. A Anthropic calibrou o preço de lançamento do Sonnet 5 (convertido em preço padrão em ago/2026) para que a migração a partir do Sonnet 4.6 seja aproximadamente custo-neutra. Fonte: [nota de rodapé do anúncio do Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5).

#### O modelo de precificação por *usage credits* (mudança estrutural, não só de número)

A novidade que mais importa para orçamento não é um preço — é um **mecanismo de cobrança**. Para os modelos de fronteira (Fable 5, 5.1 e 5.2), a Anthropic passou a **desacoplar o acesso da inclusão fixa na assinatura**, movendo-o para *usage credits* (crédito de uso medido):

| Plano / superfície | Como os modelos Fable são cobrados (estado em 25/nov/2026) |
|--------------------|--------------------------|
| Max, Ultra, seats *premium* de Team e de Enterprise seat-based | Fable 5, 5.1 e 5.2 fazem **parte padrão do plano**: até 50% dos limites semanais sem custo extra, descontados do limite normal (que o Fable consome mais rápido), **sem data de término**. Acima disso, usage credits ou troca de modelo. Fonte: [Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan). |
| Pro e seats *standard* de Team | Segundo o Help Center, os modelos Fable **não entram nos limites do plano**: usage credits desde o início. A promoção do Fable 5 terminou em 19/jul/2026; houve crédito único só para o Fable 5, **sem equivalente para o 5.1 nem para o 5.2**. **Divergência declarada:** o anúncio do Fable 5.2 diz que o Fable está incluído até 50% dos limites semanais em Pro e seats standard de Team. Para orçamento, vale o Help Center até a Anthropic reconciliar as duas páginas. Mesma fonte · [anúncio](https://www.anthropic.com/claude-fable-and-mythos-5-2). |
| Enterprise *standard* | **Sem franquia**: usage credits desde o dia 1, e sem direito ao crédito promocional. No Enterprise, o Fable 5.2 fica desligado até um admin habilitar; sete dias após o lançamento ele é adicionado aos papéis que já tinham algum Fable, e o default passa ao 5.2 salvo opt-out. |
| API / Enterprise por consumo | Tarifa de API: $8/$40 no Fable 5.2, $10/$50 no 5.1 e no 5. |
| Oferta de lançamento do 5.2 | Por tempo limitado após 09/nov, assinantes elegíveis recebem uso extra de Fable, com uma a três redefinições de limite conforme o tempo de assinatura. A data de fim está num artigo do Help Center não lido nesta revisão. |
| Marketplaces (Claude Platform on AWS, Claude in Microsoft Foundry) | Faturado em **Claude Consumption Units (CCU)**: 100 CCU = US$ 1,00, convertidos das taxas por token. |

> ⚠️ **O que a Anthropic NÃO publicou** (trate como desconhecido, confira no seu dashboard, não modele em cima): o que "50% dos limites semanais" equivale em tokens/mensagens/dólares por plano, e a conversão crédito→dólar depois de 07/jul. O único número confirmado é a taxa por token da API. Fonte da franquia e do corte: [manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) · [post de redeploy](https://www.anthropic.com/news/redeploying-fable-5).

**Linha do tempo do Fable 5 (contexto do porquê houve dois cortes):** lançado 09/jun/2026 → controles de exportação dos EUA em 12/jun (acesso suspenso globalmente) → controles suspensos em 30/jun → **redeploy global em 01/jul** com nova janela → fim da promoção do Fable 5 em Pro e standard em **19/jul** (Max e premium nunca tiveram corte; ver tabela acima). O primeiro corte anunciado (23/jun) nunca ocorreu porque o modelo estava offline. Fonte: [anúncio Fable/Mythos](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [redeploy](https://www.anthropic.com/news/redeploying-fable-5).

**Fallbacks no Fable 5.2 (09/nov/2026):** a consulta bloqueada recebe resposta do Opus 4.8 em cibersegurança e do Opus 5 em biologia, e um pequeno conjunto de temas de P&D em IA cai para o Opus 5 de forma transparente. Nos testes iniciais da Anthropic, o 5.2 gerou cerca de 55% menos bloqueios que o 5.1 (cerca de 60% menos em cyber e 40% menos em biologia), mas continua bloqueando a maior parte das tarefas de cibersegurança. Fonte: [anúncio do Fable 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2).

**Automatic fallbacks na API (beta, desde 24/jul/2026):** requisições flagged pelos classificadores de segurança em Opus 5 ou Fable 5 podem rotear automaticamente para outro modelo em vez de serem bloqueadas — a requisição sempre chega ao melhor modelo disponível. Em Claude.ai, Claude Code e Cowork, o fallback é o comportamento padrão. Fonte: [anúncio Opus 5](https://www.anthropic.com/news/claude-opus-5). Consequência para arquitetura: a política de roteamento deixou de ser só decisão de custo e virou também decisão de *continuidade* — escreva qual modelo aceita como degradação antes de o classificador decidir por você.

**Recalibração das salvaguardas de biologia do Fable 5 (07/ago/2026):** a Anthropic reescreveu a constituição do classificador de biologia do Fable 5 e reduziu os fallbacks relacionados a biologia em **~85%** (queda total de fallbacks por superfície: ~67% no Claude.ai, ~55% no Cowork, ~17% no Claude Code, ~7% na API). O fallback bio → Opus 5 **permanece**, mas restrito a usos dual-use (virologia, toxicologia, design molecular); saúde cotidiana, interpretação de exames, educação e suporte clínico passam a rodar no próprio Fable 5. Fonte: [Improving Fable 5's biology safeguards](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards). Consequência para arquitetura: **salvaguarda é parâmetro vivo** — a fronteira do que roteia muda por recalibração de classificador, sem release de modelo. Reavalie a política de roteamento também quando o vendor recalibrar salvaguardas, não só quando lançar modelo.

#### Marcação de conteúdo gerado (watermarking) — modelos lançados a partir de 02/ago/2026

A Anthropic assinou o Code of Practice do **Artigo 50(2) do EU AI Act** (transparência de conteúdo gerado por IA) e passou a marcar o que o Claude gera, com anúncio público em 11/ago/2026. Dois mecanismos complementares:

| Mecanismo | Como funciona | Escopo |
|-----------|---------------|--------|
| **Watermark embutido no texto** | Marca estatística imperceptível, tecida no próprio texto no **nível do modelo**; não altera significado nem legibilidade; sobrevive a copy-paste e "pode persistir através de alguma edição" | Todo texto gerado por modelos lançados a partir de 02/ago/2026, em todas as superfícies (API, Claude, Claude Code, Cowork, Tag) e cloud partners |
| **Metadados de proveniência assinados** | Padrão aberto **C2PA**, anexado a arquivos suportados (.svg, .png, .jpg); permite detectar adulteração | Onde o produto suporta processamento de arquivos; pode não estar disponível em toda plataforma |

Aplicação **mundial**, não restrita à União Europeia. Os modelos anteriores a 02/ago/2026 entraram em novembro: Mythos 5, Opus 4.7 e Sonnet 4.6 em 03/nov, e Opus 4.6, Opus 4.5, Sonnet 4.5 e Haiku 4.5 em 16/nov, às vésperas do fim da graça do Art. 50(2) em 02/dez/2026. **Ressalva nova:** nesses modelos de 16/nov e no Sonnet 4.6, uma requisição com `temperature`, `top_p` ou `top_k` fora do padrão pode gerar texto sem a marca; a proveniência passou a depender também da configuração de quem chama ([notas de versão](https://platform.claude.com/docs/pt-BR/release-notes/overview)). Ferramentas de detecção para usuários e terceiros foram prometidas em documentação técnica futura. Fonte: [How Claude marks AI-generated content](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) (Help Center oficial, 11/ago/2026).

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
| **Fast mode** | Fable 5.2 e Mythos 5.2 a $16/$80; Opus 5.5 a $8/$40; Opus 5 a $10/$50 (research preview); **Opus 4.8 depreciado, removido em 30/nov/2026** (depois disso, `speed: "fast"` retorna erro). Não combina com Batch. Indisponível no Opus 4.7 (erro) e no Opus 4.6 (roda e cobra em velocidade padrão, sem erro). | Velocidade virou eixo de preço também no tier de fronteira: o mesmo modelo custa 2× para responder mais rápido. Falha ruidosa num caso, silenciosa no outro. |

Fonte de todo o bloco: [pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing), consultada em 01/set e reconferida em 25/nov/2026.

> 🧭 **Leitura durável (Inv. 3):** o movimento estrutural não é só "de assinatura para crédito medido". O seguinte é maior: **a unidade de cobrança deixou de ser exclusivamente o token e passou a incluir o tempo de vida do agente**. Para workload agêntico, o modelo mental de orçamento por milhão de tokens passou a ser metade da conta. Modele custo de agente em duas dimensões, tokens e horas de sessão, e meça as duas.

#### Geração 5.2: o que mudou em novembro de 2026

| Data | Evento | Fonte |
|------|--------|-------|
| 29/out | Usage and Cost Analytics API (beta), em `/v1/organizations/analytics/usage` e `/cost`; a API de uso e custo anterior vira legado | [notas de versão](https://platform.claude.com/docs/pt-BR/release-notes/overview) |
| 30/out | Anúncio da remoção do Fast mode do Opus 4.8 em 30/nov/2026 | idem |
| 02/nov | Message threads (beta, `message-threads-2026-08-12`): a thread expira 5 minutos após a última requisição e é excluída em até 1 hora | idem |
| 03/nov | Marca d'água de texto em Mythos 5, Opus 4.7 e Sonnet 4.6 | idem |
| 09/nov | **Fable 5.2 e Mythos 5.2**, US$ 8/40, Fast mode a US$ 16/80, disponíveis na Claude API, Bedrock, Claude Platform on AWS, Google Cloud e Microsoft Foundry | [anúncio](https://www.anthropic.com/claude-fable-and-mythos-5-2) · idem |
| 12/nov | Claude Managed Agents auto-hospedado | idem |
| 16/nov | Marca d'água em Opus 4.6, Opus 4.5, Sonnet 4.5 e Haiku 4.5, com a ressalva de parâmetros de amostragem | idem |
| 17/nov | Linked billing (beta, `user-profiles-billing-2026-10-01`): o app cobra o uso do Claude direto da organização do cliente, via `billing_policy` por requisição; só para clientes que pagam a Anthropic diretamente | idem |
| 23/nov | Enterprise Frontier Safeguards em beta na Claude Platform, Claude Platform on AWS e Claude Models on Google Cloud: retenção zero para organizações elegíveis nos modelos mais capazes, com cópia criptografada de segurança (Sealed Safety Data) num bucket da conta de nuvem do cliente; webhooks `external_storage.failed` e `.recovered` | idem |
| 23/nov | Opus 4.5 (`claude-opus-4-5-20251101` e `claude-opus-4-5`) depreciado, saída da API em 22/jan/2027, migração indicada para o Opus 5.5 | idem |

**O que o Fable 5.2 muda na integração (além do preço):**

| Mudança | Consequência prática |
|---------|----------------------|
| Verificação de prefixo do thinking vale para **todas** as contas de API | A regra anti-destilação, antes só para contas criadas após 01/set, se estende a toda a base. Histórico append-only deixou de ser boa prática e virou requisito. |
| Blocos de thinking do 5.2 são descartados se a conversa migra para modelo fora do par Fable 5.2 / Mythos 5.2 | Roteamento dinâmico no meio da conversa perde o raciocínio acumulado. |
| Computer use exige `computer_toolset_20260801`; `computer_20251124` retorna 400, exceto no Bedrock | Mesmo padrão da geração 5.5. |
| Advisor: executor 5.2 aceita só Fable 5.2 ou Mythos 5.2 como advisor | Pares de advisor montados na geração anterior quebram. |
| Retenção de 30 dias exigida, sem retenção zero salvo autorização expressa; clientes elegíveis podem usar retenção zero antes de implantar o monitoramento do EFS | Fecha a divergência registrada desde a v0.5: a regra é 30 dias, a exceção é o EFS. |

#### Produto: o Claude virou superfície de trabalho (novembro de 2026)

Em novembro a Anthropic lançou, fora da API, as peças que levam o trabalho do dia a dia para dentro do Claude. Estado em 25/nov/2026:

| Produto | Status e data | Planos e superfícies | O que faz | Limites e governança |
|---------|---------------|----------------------|-----------|----------------------|
| **Claude Sheets** | Beta, 10/nov/2026 | Todos os planos pagos; web, desktop e mobile | Planilha com abas, fórmulas, formatação e listas suspensas gerada a partir de um pedido; cada edição do Claude fica registrada; coedição com o time | A própria Anthropic diz que a funcionalidade ainda é simples; para Excel completo, exportar para .xlsx ou CSV ou usar o Claude for Excel. Ligado por padrão no Team, desligado no Enterprise (Organization settings > Artifacts) |
| **Claude Whiteboards** | Beta, 10/nov/2026 | Todos os planos pagos; web, desktop e mobile | Quadro compartilhado: transforma um plano em linha do tempo com responsáveis e datas, agrupa notas por tema, responde sobre um recorte selecionado, vira documento ou apresentação; exporta para Lucid, Miro e Vani by Zoho | Mesmo padrão de governança do Sheets |
| **Claude Data** (antigo Claude Dashboards) | GA em 10/nov/2026; consultas certificadas e compartilhamento ao vivo seguem em beta | Todos os planos pagos; web, desktop e mobile | Painéis sobre warehouse ou CRM (Redshift, BigQuery, ClickHouse, Snowflake, Salesforce), métricas com selo de certificação do time de dados, histórico com reversão, atualização em cadência configurável | Exige conector de dados. No compartilhamento ao vivo, quem vê não roda consultas com o acesso do autor. Ligado por padrão no Team; no Enterprise, ligado por padrão desde 20/nov/2026 |
| **Conectores interativos** | 10/nov/2026 | Não especificado | Apps de parceiros (Adobe, Atlassian, Box, Notion) abrem dentro do Claude, ao lado da conversa ou em tela cheia | No Enterprise, o admin decide quem usa quais produtos e conectores |
| **Claude Meetings** | Beta em implantação desde 12/nov/2026 | Team e Enterprise; Claude e Claude Desktop | O Claude entra numa chamada do **Google Meet** como participante visível, toma notas, responde perguntas e monta documentos, quadros e slides durante a reunião | Único provedor de vídeo citado: Google Meet. Participante visível, não gravador oculto |

Outros itens de produto do mês, nas notas de versão do Help Center: Personal Finance in Claude (beta, 05/nov, Pro, Max e Ultra, só nos EUA); controles de segurança e administração no Enterprise (05/nov); tags de projeto para rastrear gasto por centro de custo no Enterprise (beta, 06/nov); canal de release no Claude Desktop (17/nov); computer use em beta para Team e Enterprise (20/nov); instalar artifacts como apps no Mac e no Windows e enviar ou salvar arquivos em apps conectados (beta, 24/nov).

Fontes: [Introducing Claude Whiteboards, Claude Sheets, and Claude Data](https://claude.com/resources/articles/sheets-whiteboards-data) · [More ways to work with Claude](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors) · [release notes do Help Center](https://support.claude.com/en/articles/12138966-release-notes), lidos em 25/nov/2026. Nenhum preço específico foi publicado para esses produtos.

> 🧭 **Leitura durável (Inv. 3 e 4):** a disputa saiu do modelo e foi para a superfície de trabalho, o lugar onde o time planeja, decide e registra. Duas consequências que sobrevivem a esta rodada. Primeiro, **o default de governança muda por plano**: o mesmo recurso nasce ligado no Team e desligado (ou ligado com data marcada) no Enterprise, então a decisão de quem acessa qual conector precisa existir antes da data, não depois. Segundo, **dado gerado por IA sem métrica certificada só acelera a discussão sobre qual número está certo**: o recurso mais valioso do Claude Data não é o painel, é o selo do time de dados.

#### Geração 5.1 / 5.5: o que mudou entre 12/ago e 01/out

| Data | Evento | Fonte |
|------|--------|-------|
| 01/set/2026 | **Fable 5.1 e Mythos 5.1** em GA (Fable) e acesso restrito (Mythos). Preço de lista inalterado; cache read cai para US$ 0,25. | [anúncio](https://www.anthropic.com/claude-fable-and-mythos-5-1) · [docs](https://platform.claude.com/docs/en/models/fable-5-1/overview) |
| 22/set/2026 | **Opus 5.5**: US$ 4/20 (Opus 5 era US$ 5/25), cache read US$ 0,20, Batch US$ 2/10, Fast mode US$ 8/40. | [anúncio](https://www.anthropic.com/claude-opus-5-5) · [docs](https://platform.claude.com/docs/en/models/opus-5-5/overview) |
| 28/set/2026 | **Sonnet 5.5**: preço igual ao do Sonnet 5, 512 tokens de cache mínimo (era 1.024). | [docs](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) |
| 07/out/2026 | **Haiku 5.5**: US$ 0,10/0,50 até 100k tokens de prompt, US$ 0,50/2,50 acima. Haiku 4.5 passa a geração anterior. | [anúncio](https://www.anthropic.com/claude-haiku-5-5) · [docs](https://platform.claude.com/docs/en/models/haiku-5-5/overview) |

**Datas de retirada documentadas (piso "not sooner than"):** Fable 5 09/jun/2027; Fable 5.1 01/set/2027; Opus 4.8 28/mai/2027; Opus 5 24/jul/2027; Sonnet 5 30/jun/2027; Opus 5.5 22/set/2027; Sonnet 5.5 28/set/2027; Haiku 5.5 07/out/2027. **Aposentadorias marcadas:** Sonnet 4.5 (`claude-sonnet-4-5-20250929`) em 30/nov/2026, migração para o Sonnet 5.5; Opus 4.5 em 22/jan/2027, migração para o Opus 5.5. A política declarada é aviso mínimo de 60 dias antes da retirada de modelo público. Fonte: [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations), lida em 25/nov/2026.

**Janela de contexto e saída:** 1M de tokens de contexto e 128K de saída em toda a geração 5.x, Fable 5.2 incluído (300K de saída em Batch API beta no Opus 5.5 e no Sonnet 5.5). Knowledge cutoff de junho de 2026 para a geração 5.x; Haiku 4.5 mantém fevereiro de 2025.

**Preço relativo:** o Opus 5.5 custa metade do Fable 5.2 no input e no output. A razão input:output de 1:5 se mantém em todos os tiers (Fable 8:40, Opus 4:20, Sonnet 2:10, Haiku 0,10:0,50). A distância entre degraus mudou duas vezes em dois meses: Fable para Opus foi de 2× (jul) para 2,5× (set, Fable 5.1 contra Opus 5.5) e voltou a 2× (nov, Fable 5.2). A razão entre tiers não é constante, é decisão comercial de cada geração.

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
| **`temperature`, `top_p` e `top_k` não padrão retornam erro 400** | Haiku 5.5 | Omitir os três parâmetros. Blocos de thinking só funcionam na conta que os gerou ou em conta vinculada. Guia: [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide). |
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
- **Retenção, divergência encerrada em novembro:** Fable 5.1 e 5.2 exigem retenção de 30 dias, sem retenção zero salvo autorização expressa; clientes elegíveis podem usar retenção zero antes de implantar o monitoramento do EFS, que entrou em beta em 23/nov/2026. Fonte: [notas de versão](https://platform.claude.com/docs/pt-BR/release-notes/overview) · [anúncio do Fable 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2).
- **Fallback do Fable 5.1 e 5.2:** usos dual-use são redirecionados a modelos Opus; no 5.2, a Anthropic confirma Opus 4.8 para cibersegurança e Opus 5 para biologia (ver bloco de fallbacks acima).
- **Anti-destilação com efeito em integração:** desde 01/set, contas de API novas não podem editar contexto anterior do Claude preservando o transcript de thinking; **com o Fable 5.2 (09/nov), a regra vale para todas as contas de API**, como a Anthropic havia sinalizado. É mudança de política de plataforma com impacto em código de integração, sem mudança de preço. Fonte: [anúncio do Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1).
- **Effort por superfície:** segundo o anúncio, o Fable 5.1 usa effort High por padrão no Claude Code e Medium no Cowork e no Claude.ai; em Low ou Medium a Anthropic afirma resultado igual ou melhor que o do Fable 5 a custo bem menor. O mesmo modelo custa diferente por superfície sem escolha do usuário.
- **Cache read abaixo do Opus:** com US$ 0,25 por MTok no Fable 5.1 contra US$ 0,50 no Opus 5 (US$ 0,20 no Opus 5.5), o Fable 5.1 lê cache por metade do preço do Opus 5 e fica próximo do Opus 5.5. Para agente com contexto pesado, a política de roteamento por preço de headline deixa de refletir o custo real.
- **Proveniência de conteúdo:** a página do Fable 5.1 confirma watermark estatístico de texto em toda saída e Content Credentials C2PA assinadas para imagem, vídeo e áudio gerados via Files API.

> 🧭 **Leitura durável (Inv. 3):** salvaguarda virou **produto com tiers, contrato e auditoria**. Isso muda a pergunta de compras: não basta perguntar "qual modelo", é preciso perguntar "com qual regime de retenção, monitoramento e verificação". Escreva isso no contrato antes de a primeira requisição bloqueada acontecer em produção.

#### Model Hardware Standard (27/ago/2026, research preview)

Especificação compartilhada para agentes de IA operarem dispositivos físicos por meio de drivers padronizados com primitivas de leitura e escrita, compatível com MCP e agnóstica de modelo. Parceiros citados: Genentech, Baker Lab e Pinglay Lab (UW), Carnegie Mellon, HHMI Janelia, QuEra, Tetsuwan Scientific; apoio de AWS, Danaher, QIAGEN, Tecan, Universal Robots e outros. Ainda não é open source; avaliações de segurança em andamento. Fonte: [anthropic.com/news/model-hardware-standard-research-preview](https://www.anthropic.com/news/model-hardware-standard-research-preview). Leitura durável: a fronteira de risco de agentes deixa de ser só dado e código e passa a incluir atuação física, o que puxa governança para o nível de dispositivo.

#### Outros anúncios do produto (12/ago a 25/nov)

| Data | Item | Fonte |
|------|------|-------|
| 14/ago | "How Claude's text watermark works" | [anthropic.com/news](https://www.anthropic.com/news) |
| 25/ago | Memory expandida em Cowork e chat, com gestão por "Topics" e opção de excluir temas sensíveis | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 06/ago | Escaneamento de segurança de skills e plugins de terceiros para Enterprise | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 10/set | Smart reports (beta) para Enterprise, análise do uso do time | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 15/set | Plugin Salesforce (beta) com 37 skills de vendas | [release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 18/set | Parceria com a Accenture em avaliação embutida | [anthropic.com/news](https://www.anthropic.com/news) |
| 01/out | Barclays escala o Claude em operações | [anthropic.com/news](https://www.anthropic.com/news) |
| 06/out | Expanding the Cyber Verification Program (conteúdo não lido nesta rodada) | [anthropic.com/news](https://www.anthropic.com/news) |
| 07/out | Claude Haiku 5.5 | [anúncio](https://www.anthropic.com/claude-haiku-5-5) |
| 08/out | 2026 Usage Policy update (conteúdo não lido nesta rodada) | [anthropic.com/news](https://www.anthropic.com/news) |
| 08/out | Introducing the Anthropic Cyber Mission (conteúdo não lido nesta rodada) | [anthropic.com/news](https://www.anthropic.com/news) |
| 09/nov | Claude Fable 5.2 e Claude Mythos 5.2 | [anúncio](https://www.anthropic.com/claude-fable-and-mythos-5-2) |
| 10/nov a 20/nov | Oferta pública inicial: roadshow (10/nov), precificação (18/nov) e fechamento (20/nov). Sem efeito em preço público | [anthropic.com/news](https://www.anthropic.com/news) |

#### Usage credits e tokenizer: reconferência de 25/nov

Os release notes de 12/ago a 01/out não registram mudança em usage credits nem em modelo default por plano. O tokenizer da geração 4.7 em diante (cerca de 30% mais tokens) segue documentado no pricing oficial, que agora inclui Fable 5.1 e Mythos 5.1. O Sonnet 5.5 usa tokenizer idêntico ao do Sonnet 5. O Haiku 5.5 usa o tokenizer novo, cerca de 30% mais tokens que o Haiku 4.5 (reconferido em 09/out). A página de pricing atribui o tokenizer novo a todos os modelos 4.7 em diante, o que cobre Opus 5.5, Fable 5.1 e Fable 5.2; o anúncio do 5.2 não menciona mudança de tokenizer. A tabela de usage credits foi reescrita em 25/nov a partir do Help Center. Defaults de plano (Max com Opus 5, Free e Pro com Sonnet 5) **não foram reconfirmados** nesta rodada.

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

| Tier | Referência corrente na família Claude (por MTok, 2026-11-25) | Cuidado de leitura |
|------|--------------------------------------------------------------|--------------------|
| Fronteira (Mythos-class) | Fable 5.2 · $8 / $40 (cache read $0,20; Fast mode $16 / $80); Fable 5.1 e Fable 5 seguem a $10 / $50 | Reserve para julgamento e horizonte longo; na assinatura, a cobrança depende do plano (ver usage credits) |
| Premium | Opus 5.5 · $4 / $20 (metade do Fable 5.2); Opus 5 e Opus 4.8 seguem a $5 / $25 | Quase-fronteira; fallback de dual-use do Fable. Refaça a varredura de effort antes de comparar custo por tarefa |
| Balanceado | Sonnet 5.5 · $2 / $10 (mesmo preço do Sonnet 5; aumento de set/2026 cancelado) | Cavalo de batalha de produção; confira o default de Free/Pro no seu plano |
| Pequeno / velocidade | Haiku 5.5 · $0,10 / $0,50 até 100k tokens de prompt, $0,50 / $2,50 acima; Haiku 4.5 segue a $1 / $5 | Um centésimo do input do Fable na faixa curta; o preço depende do tamanho do prompt, e o tokenizer novo infla a contagem em cerca de 30% frente ao Haiku 4.5 |
| Runtime de sessão (Managed Agents) | US$ 0,08 por session-hour em `running`, fora do eixo de token | Segundo eixo de custo de agente; sem Batch e sem cloud parceira |
| Open weights self-hosted | TCO varia por hardware | Comparar com proprietário **incluindo** ops |

> Padrão a reter (não o número): a família mantém uma razão **input:output de 1:5** em todos os tiers, no eixo de token; existe agora um segundo eixo (runtime de sessão). A proporcionalidade **quebrou no cache read**: US$ 0,20 no Fable 5.2 e no Opus 5.5, US$ 0,50 no Opus 5, US$ 0,10 no Sonnet 5.5, de modo que o topo e o premium leem cache pelo mesmo preço. O degrau de lista Fable para Opus foi de 2,5× em setembro e voltou a 2× em novembro: **a razão entre tiers não é constante, é decisão comercial de cada geração**, e não deve ser codificada em planilha de custo. É a *forma* da curva de custo — não o valor absoluto — que informa a arquitetura. Com o Haiku 5.5, a razão 1:5 continua, mas o preço passou a ser função do tamanho do prompt (faixa até 100k e acima), mais um caso de preço que deixou de ser um número.

Fontes oficiais de pricing (consultar diretamente):
- [Anthropic pricing](https://www.anthropic.com/pricing)
- [OpenAI pricing](https://openai.com/api/pricing/)
- [Google AI Studio pricing](https://ai.google.dev/pricing)
- [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)

---

## SEÇÃO 6 — REGULAÇÃO E MERCADO BR (camada de Apêndice Vivo)

| Tema | Status corrente | Fonte primária |
|------|-----------------|----------------|
| LGPD aplicada a IA | Em vigor. ANPD foi transformada em agência pela MP aprovada no Senado em fev/2026 (200 cargos). Nenhum ato novo sobre IA encontrado desde ago/2026, exceto a metodologia de testagem do Sandbox Regulatório (19/ago, CIAAM/USP, seis ciclos em três blocos). Número da lei de conversão (Lei nº 15.352/2026) **a confirmar no Planalto**. Em 25/11/2026 a lista de notícias da ANPD seguia carregando dinamicamente e não pôde ser lida | [gov.br/anpd](https://www.gov.br/anpd/pt-br) · [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2026/02/24/senado-aprova-mp-que-transforma-a-anpd-em-agencia-e-cria-200-cargos) |
| PL de IA brasileiro | PL 2338/2023 em Comissão Especial na Câmara, regime de prioridade. Situação oficial em 25/11/2026: **"Aguardando Parecer do(a) Relator(a)"**, com **45 proposições apensadas** (eram 37 em setembro e 40 em outubro). Últimas ações: apensações pela Mesa em 11/11, 12/11 e 13/11/2026. O parecer de maio citado pela imprensa **não consta como apresentado** na ficha. Sem data de votação. Retorna ao Senado após a Câmara | [ficha da Câmara](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) |
| AI Act (União Europeia) | Aplicação geral desde 02/ago/2026 (Art. 50 incluído; watermarking do Claude é materialização direta). High-risk Annex III adiado para 02/dez/2027 e Annex I para 02/ago/2028 pelo Omnibus; sistemas já no mercado antes de 02/ago/2026 têm até 02/dez/2026 para o Art. 50(2). Número do regulamento (UE) 2026/1744 e vigência em 27/07/2026 confirmados no EUR-Lex; data de publicação no Jornal Oficial **a confirmar**. **Próximo marco: 02/dez/2026**, fim da graça do Art. 50(2), que explica a extensão da marca d'água do Claude a modelos anteriores em novembro | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) · [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) |
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
| v0.6 | 2026-10-09 | **Haiku 5.5** (GA 07/10, US$ 0,10/0,50 até 100k e 0,50/2,50 acima); correção do cache read do Sonnet 5.5 (US$ 0,10); breaking change de parâmetros do Haiku 5.5; Seção 5 e anúncios atualizados; tokenizer do Haiku 5.5 registrado; Seção 6 reconferida (PL 2338, ANPD, AI Act) sem mudança de fato. | Editor executivo (aprovado pelo autor) |
| v0.7 | 2026-11-01 | Reconferência mensal: preços, lineup e multiplicadores de cache da família Claude sem mudança; tokenizer 4.7 em diante confirmado na página de pricing (cobre Opus 5.5 e Fable 5.1); posts de 09/10 a 01/11 registrados (GSA, S-1, destilação, avaliadores independentes). Pendências declaradas. | Editor executivo (aprovado pelo autor) |
| v0.8 | 2026-11-25 | **Fable 5.2 e Mythos 5.2** ($8/$40, cache read $0,20, Fast mode $16/$80); Fast mode do Opus 4.8 removido em 30/nov; pisos de retirada e aposentadorias (Sonnet 4.5 em 30/nov, Opus 4.5 em 22/jan/2027); bloco novo da geração 5.2 (eventos de novembro e mudanças de integração); usage credits reescritos pelo Help Center, com divergência do anúncio declarada; retenção de 30 dias versus EFS reconciliada; anti-destilação estendida a todas as contas; marca d'água estendida a sete modelos anteriores; bloco novo de produto (Sheets, Whiteboards, Data, conectores interativos, Meetings); Seções 5 e 6 reescritas. | Editor executivo (aprovado pelo autor) |
| v0.9 | (próxima) | Ler Usage Policy 2026, Cyber Verification Program e Cyber Mission; data de fim da oferta de lançamento do 5.2; lista de modelos com ZDR no EFS; status do Haiku 4.5; defaults de plano; scores auditados | Autor + revisão |

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
