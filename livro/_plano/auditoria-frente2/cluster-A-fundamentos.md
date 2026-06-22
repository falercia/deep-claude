# AUDITORIA EDITORIAL — CLUSTER A: FUNDAMENTOS
Banca Editorial Adversarial · Deep Claude (Livro 2) · 2026-06-17

Capítulos auditados: L2-C01 (Executivos), L2-C02 (Entendendo o Claude), L2-C04 (Modelos Claude)
Régua: Livro 1 Os Invariantes · Risco mortal monitorado: "manual de botão"

---

## C01 — CLAUDE PARA EXECUTIVOS
Nota: 5/10 · Veredito: C · "Manual de botão"? MÉDIO

### Os 7 elementos

1. **Abertura ancorada**: ⚠️ — Declara Invariantes 8 e 9 com box "🧭 Por que…", mas a justificativa é fraca. Dizer que "Inv. 8 garante dono identificável" e "Inv. 9 lembra que IA amplifica" é decorativa, não demonstrada. O capítulo nunca volta explicitamente a esses invariantes na análise dos usos ou dos anti-padrões. O Framework F1-DECID-IA é mencionado mas nunca explicado — é etiqueta sem conteúdo. Qualquer leitor que pule o box lê o capítulo inteiro sem saber qual método está sendo aplicado.

2. **Conceito intuitivo + analogia memorável**: ❌ — Seção 1.1 enuncia o problema ("uso estratégico vs. casual vs. técnico") mas não oferece analogia. Nenhuma imagem mental que fixe o conceito. O Teste da Joana falha: "amplificador de capacidades executivas" é frase genérica que poderia descrever qualquer assessor humano ou ferramenta de produtividade. Não há âncora intuitiva que distinga Claude de, digamos, um bom ERP bem configurado.

3. **Quando usar / quando EVITAR**: ⚠️ — Seção 1.4 ("O que evitar") existe e é a parte mais forte do capítulo. Lista 5 anti-padrões reais. Mas "quando usar" é totalmente ausente como critério de decisão — a seção 1.3 lista usos mas não oferece condições de acionamento ("use briefing quando a reunião for X mas não quando for Y"). A fronteira entre "uso maduro" e "uso prematuro" nunca é traçada. Um executivo que leu isso não tem critério para decidir quando NÃO usar — apenas sabe que existe uso.

4. **Profundidade técnica real**: ❌ — Gravíssima lacuna. O capítulo descreve resultados ("empresa lançou 3 iniciativas") mas nunca explica *como* as ferramentas mencionadas funcionam. "Briefing automatizado às 6h45" — como se configura? Qual é o mecanismo de Scheduled Task que produz isso? "Research profundo" — qual é a diferença técnica entre Research e busca comum? "Voz mobile" — o que especificamente Claude faz que outro assistente de voz não faz? Cada item na seção 1.3 é ponto de entrada para conteúdo técnico que não vem. O capítulo refere extensamente a caps 20, 22, 27, 28, 29 — mas não entrega nenhuma mecânica própria. Resultado: capítulo de 100% de promessas, 0% de entrega técnica.

5. **Exemplo memorável brasileiro**: ✅ — Seção 1.5 (CEO de empresa de tecnologia, ~600 funcionários) é o melhor trecho do capítulo. Tem contexto, trajetória temporal (antes/depois de outubro 2025), métrica concreta (uma hora/dia), consequência estratégica (3 iniciativas desbloqueadas, +22% receita) e lição estrutural explícita. Falta apenas rótulo explícito "cenário ilustrativo" para blindar o texto de questionamentos factuais.

6. **Camada Viva**: ⚠️ — O capítulo menciona "Web Search ativo" (seção 1.4) e "Research profundo" sem pinning ao Apêndice Vivo. "Plano Pro pessoal" e "Team com DPA formal" na seção 1.4 são termos de produto que podem mudar — deveriam ser apontados ao Apêndice. Os links de Conexões (seção 1.6) apontam para caps do próprio livro e do L1 mas não para o Apêndice Vivo. Positivo: nenhum preço ou benchmark numérico no corpo — o risco é menor aqui que no C04.

7. **Exercícios + autoavaliação + conexões**: ⚠️ — Tem checklist de validação (seção 1.7, 5 itens) e tabela de conexões. Não tem exercícios práticos (nenhum), nenhuma pergunta de revisão, e o checklist é de "articular" e "defender" — mais apresentação do que aplicação. Não há exercício que force o leitor a *construir* algo. Contraste gritante com C02 e C04, que têm exercícios práticos e projeto do capítulo.

### 5 testes

- **Joana**: REPROVADO — lê o capítulo e sabe que Claude "amplifica capacidade executiva" mas não consegue montar uma rotina funcional sozinha; as peças (briefing, Research, scheduled tasks) são citadas mas não operadas.
- **Durabilidade**: MÉDIO — os anti-padrões (1.4) e o conceito de amplificador vs. substituto (1.1) duram bem. Os usos específicos da seção 1.2 são atados a produtos que podem mudar de nome.
- **Diferenciação**: COMMODITY — a tese "CEO usou IA e ganhou tempo para estratégia" está em dezenas de conteúdos de produtividade no mercado. Nada aqui é exclusivo ao Claude; poderia ser reescrito com ChatGPT ou Gemini sem perder substância.
- **Memorização**: FRACO — sem analogia e sem estrutura mnemônica além de "cinco usos". A rotina semanal (1.2) tem potencial mas está em prosa corrida, não em estrutura visual ou conceitual fixável.
- **Transformação**: BAIXO — o leitor termina com a sensação de que "deveria usar Claude mais", mas sem mapa claro de como começar amanhã. A transformação de comportamento requer critério de decisão que este capítulo não entrega.

### Top lacunas (priorizadas, com seção)

- **[CRÍTICO] Ausência total de mecânica técnica** (seções 1.2 e 1.3): cada produto mencionado (Briefing via Scheduled Task, Research, Projects, Voice) é citado mas não explicado minimamente. O capítulo deveria ou entregar a mecânica ou explicitamente dizer "veja Cap X para o como" com uma frase de por quê isso importa para o executivo.
- **[CRÍTICO] Analogia ausente** (seção 1.1): o conceito intuitivo não fixa. Precisa de âncora visual ou metáfora — algo como "amplificador de instrumento musical" ou "piloto automático de aviação executiva".
- **[ALTO] Framework F1-DECID-IA fantasma** (abertura): mencionado mas nunca operado. Ou entregar o framework visualmente (matriz de decisão Invariante 8/9 → ação) ou remover a menção — fantasma é pior que ausência.
- **[ALTO] Critério de "quando usar" ausente** (seção 1.3): transformar cada um dos 5 usos em critério binário ("use X quando a reunião tiver mais de 3 participantes externos" etc.).
- **[MÉDIO] Falta rótulo "cenário ilustrativo"** (seção 1.5): o exemplo é excelente mas pode ser lido como estudo de caso verificável — blindar com nota de rodapé.
- **[MÉDIO] Exercícios ausentes**: é o único dos três capítulos sem nenhum exercício prático. Desequilíbrio didático visível na série.

### Maior força a preservar

- Seção 1.4 (anti-padrões) é bem específica, acionável e honesta. A distinção "amplificador vs. substituto de julgamento" é conceitualmente sólida e diferenciadora — precisa de amplificação, não substituição.

---

## C02 — ENTENDENDO O CLAUDE
Nota: 7/10 · Veredito: B · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada**: ✅ — Box de abertura mapeia explicitamente Modelos → Inv. 4, Projects → Inv. 2+3, Skills → Inv. 3+9, Code → Inv. 6+9, Subagents → Inv. 6, Enterprise → Inv. 8. A ancoragem é estrutural, não decorativa: posiciona o capítulo como "porta de entrada" de toda a Parte e justifica por que o contexto da Anthropic é pré-requisito. Apêndice Vivo referenciado diretamente na abertura — bom modelo para os outros caps.

2. **Conceito intuitivo + analogia memorável**: ✅ — Seção 2.2 (banco vs. cooperativa de crédito) é a melhor analogia do cluster. Joana entende imediatamente: "não é só o produto, é o DNA da decisão". A analogia sustenta o argumento técnico que vem depois (CAI como manifestação do DNA) e é brasileira de contexto (brasileiros conhecem cooperativas de crédito). Nota de qualidade: a analogia poderia ser ligeiramente estendida para mostrar *quando* essa diferença de DNA importa na prática — hoje ela explica o "o quê" mas não o "e daí para mim".

3. **Quando usar / quando EVITAR**: ⚠️ — Este é o ponto mais fraco do C02. O capítulo argumenta bem *por que* a Anthropic é diferente, mas não traduz isso em critério de decisão. Quando escolher Claude vs. GPT-5 vs. Gemini? Há uma menção (seção 2.3.4) de "empresas com requisitos altos de segurança e qualidade", e o box "Para Executivos" (seção 2.4) aponta domínios regulados — mas isso é sugestão, não framework. O capítulo deixa a decisão implícita onde deveria ser explícita: "escolha Claude quando seu caso tem [condição A, B ou C]; prefira GPT quando [D, E]; prefira Gemini quando [F]."

4. **Profundidade técnica real**: ✅ — Seção 2.3.2 (Constitutional AI em 3 passos) é o melhor momento técnico do capítulo. Explica RLHF, aponta as limitações honestas de RLHF, descreve CAI com precisão (constituição → self-critique → RLAIF), e inclui crítica honesta de CAI (transfere viés para a redação da constituição). Isso é profundidade real, não "veja a doc". Seção 2.3.3 sobre personalidade observável também entrega: lista marcadores concretos e admite quando a personalidade é desvantagem. A limitação é que a seção 2.3.1 (linha do tempo) inclui datas e versões que pertencem ao Apêndice Vivo — ver item 6.

5. **Exemplo memorável brasileiro**: ✅ — Seção 2.4 (empresa de seguros, avaliação de subscrição) é forte: setup claro, teste controlado com caso-limite deliberado, resultado paradoxal (recusa como vantagem), quantificação (três anos sem incidente), lição estrutural explícita. Tem o marcador "Para Executivos" no final. Falta rótulo explícito "cenário ilustrativo".

6. **Camada Viva**: ⚠️ — Problema real na seção 2.3.1: linha do tempo com datas específicas ("março de 2024", "setembro de 2025", "fevereiro de 2025"), versões específicas ("Opus 4.6 e 4.7, Sonnet 4.5 e 4.6, Haiku 4.5"), benchmarks ("77,2% no SWE-bench") e produtos ("Claude Skills, Subagents, Cowork Mode") estão no corpo do texto. Quando esses dados mudarem (e vão mudar), o capítulo fica inconsistente internamente. A seção 2.3.4 tem números de receita ("US$ 5 bilhões", "US$ 4 bilhões" de investimento Amazon) e participação de mercado que também pertencem ao Apêndice. A abertura aponta o Apêndice Vivo, mas não o usa na prática. Seção 2.3.3 tem benchmark de preferência em escrita (47%/29%/24%) — corpo errado para esse dado.

7. **Exercícios + autoavaliação + conexões**: ✅ — Tem 4 exercícios práticos (teste de personalidade, teste de limites, leitura da constituição, análise estratégica), 5 perguntas de revisão, projeto do capítulo (documento "Por que Claude, para nós"), checklist (7 itens), validação UAU (5 critérios com orientação de remediação por faixa). Conexões explícitas com L1 e outros caps do L2. É o capítulo mais completo do cluster nesta dimensão.

### 5 testes

- **Joana**: APROVADO COM RESERVA — entende a diferença Anthropic/OpenAI/Google, entende por que CAI importa, consegue usar o exemplo da seguradora em conversa. Não sai com critério claro de quando escolher Claude.
- **Durabilidade**: BOM — os conceitos de CAI, RLAIF, PBC, e os três princípios públicos duram. Os dados específicos da seção 2.3.1 e 2.3.4 são perecíveis e estão no lugar errado.
- **Diferenciação**: DIFERENCIADO — a explicação técnica de CAI e a leitura estratégica da estrutura legal PBC são acima da média do mercado. O argumento da "recusa como vantagem" é genuinamente original.
- **Memorização**: MÉDIO — a analogia banco/cooperativa fixa. A estrutura de 3 passos de CAI fixa. Os "três princípios públicos" (2.5) são memoráveis. A linha do tempo (2.3.1) é longa demais para ser memorizada e não deveria estar no corpo.
- **Transformação**: MÉDIO-ALTO — o leitor sai com razões reais para escolher Claude em domínios regulados e com framework mental sobre o DNA do produto. Falta o critério explícito de seleção de provedor.

### Top lacunas (priorizadas, com seção)

- **[CRÍTICO] Dados perecíveis no corpo** (seção 2.3.1, 2.3.3, 2.3.4): linha do tempo com versões, benchmarks e receitas estão no corpo e deveriam ir ao Apêndice Vivo ou ser convertidos em referências estáveis ("versões correntes no Apêndice J").
- **[ALTO] Ausência de framework de decisão de provedor** (capítulo inteiro): o capítulo convence que a Anthropic é diferente mas não entrega matriz de decisão. Precisa de seção explícita "quando Claude, quando não Claude" — o capítulo C04 tem isso para modelos, o C02 deveria ter para provedores.
- **[MÉDIO] Analogia banco/cooperativa não fecha o loop prático** (seção 2.2): excelente para explicar o DNA, mas a analogia morre antes de chegar a "e portanto quando você vai escolher entre eles, aqui está o critério".
- **[MÉDIO] Rótulo "cenário ilustrativo" ausente** (seção 2.4): o exemplo da seguradora é poderoso; proteger de questionamentos factuais.
- **[BAIXO] Seção 2.5 (três princípios) é boa mas não está conectada de volta aos Invariantes do L1**: os princípios (safety, scaling responsável, transparência) mapeiam naturalmente para Invariantes — essa conexão tornaria a seção estruturalmente mais densa.

### Maior força a preservar

- A explicação de Constitutional AI (seção 2.3.2) com RLHF → limitações → CAI → crítica honesta é o melhor trecho técnico dos três capítulos. Raro encontrar essa honestidade crítica em material executivo. Preservar integralmente, incluindo a crítica sobre transferência de viés.

---

## C04 — TODOS OS MODELOS CLAUDE
Nota: 6/10 · Veredito: B- · "Manual de botão"? ALTO

### Os 7 elementos

1. **Abertura ancorada**: ✅ — Box declara Invariante 4 (Encaixe) com F2-ENCAIXE-5, acrescenta Inv. 3 (Camada Dupla) para justificar durabilidade, e aponta Apêndice Vivo na abertura. É o box mais completo do cluster em termos de mecânica dos invariantes. Porém: o texto do capítulo nunca mais menciona "Encaixe" ou "Invariante 4" — a ancoragem fica no box, não penetra no argumento. O leitor que pula o box não sabe que está aplicando um método.

2. **Conceito intuitivo + analogia memorável**: ✅ — Seção 4.2 (carpinteiro e suas ferramentas: serra circular/Opus, tico-tico/Sonnet, formão/Haiku) é eficaz e concreta. Joana visualiza imediatamente. A analogia sustenta bem o argumento de roteamento (o carpinteiro não usa a serra circular para madeira balsa). Pequena crítica: a analogia é genérica demais para ser exclusiva do Claude — o mesmo argumento serve para qualquer família de modelos de qualquer provedor.

3. **Quando usar / quando EVITAR**: ✅ — Seção 4.4 (framework de decisão) entrega um algoritmo real com três perguntas binárias. "Exige raciocínio profundo? → Opus. Volume gigantesco simples? → Haiku. Senão? → Sonnet." É o melhor framework de decisão do cluster. Seção 4.6 (padrões de uso profissional) complementa com cinco padrões concretos. Nota negativa: falta o critério de quando *não* usar roteamento — há casos (protótipos, times pequenos sem engenharia) em que a complexidade do roteamento custa mais que o benefício. Esse "quando EVITAR o roteamento" está ausente.

4. **Profundidade técnica real**: ⚠️ — A seção 4.3.1 lista especificações (benchmarks, preços, velocidade), mas isso é tabela de specs, não mecânica. A seção 4.3.2 (extended thinking) é razoável mas superficial: diz "o modelo gera tokens de pensamento" mas não explica em que cenários o ganho de qualidade é real vs. marginal, nem como o custo de tokens de raciocínio é cobrado na prática. Seção 4.3.3 (janela de contexto) é genuinamente útil ("janela compartilhada entre input e output" é informação não óbvia). O grande buraco: os limites reais de cada modelo além de custo não são articulados. Quando Haiku falha em raciocínio multi-etapa? Quando Sonnet começa a perder para Opus em análise estratégica? Quais categorias de tarefa a diferença de 80,8% vs. 77,2% em SWE-bench se manifesta no dia a dia? A profundidade técnica real exigiria responder essas perguntas.

5. **Exemplo memorável brasileiro**: ✅ — Seção 4.5 (empresa de logística, 800 motoristas, 12 mil chamadas/hora) é o exemplo mais operacionalmente rico do cluster. Tem arquitetura detalhada (classificador Haiku → Sonnet → Opus em extended thinking), métricas precisas (custo de US$ 18k → US$ 8k, taxa de escalonamento de 12% → 3%), e lição estrutural explícita sobre portfolio coordenado. Falta rótulo "cenário ilustrativo". O exemplo ensina engenharia de roteamento implicitamente — isso é valor real.

6. **Camada Viva**: ❌ — Este é o pior capítulo do cluster nesta dimensão. A seção 4.3.1 tem todos os preços no corpo do texto (US$ 15/75 por M tokens para Opus, US$ 3/15 para Sonnet, US$ 0,80/4 para Haiku), benchmarks específicos com porcentagens (80,8%, 64,3%, 77,2%), versões de modelos ("Opus 4.6 e 4.7", "Sonnet 4.5 e 4.6", "Haiku 4.5"), nomes de modelos concorrentes ("GPT-5.4", "Gemini 3.1 Pro"). O resumo executivo (4.8) repete os preços em tabela. O box "Para Executivos" (4.5) cita "30% a 60% do orçamento" como cifra. A abertura aponta o Apêndice Vivo, mas toda a seção 4.3.1 contradiz essa instrução ao colocar os dados perecíveis exatamente onde o leitor vai consultá-los — no corpo. Quando esses dados mudarem (trimestre que vem), o capítulo inteiro fica desatualizado. Este é o problema estrutural mais grave do cluster.

7. **Exercícios + autoavaliação + conexões**: ✅ — Tem 4 exercícios práticos (teste comparativo, cálculo de economia, teste de extended thinking, esboço de roteador), 5 perguntas de revisão, projeto do capítulo (implementação de roteamento real), checklist (6 itens), validação UAU com remediação. Conexões explícitas com L1 e L2. O projeto do capítulo é o melhor do cluster por ser implementável ("execute em paralelo por duas semanas, meça"). Ponto fraco: exercício 2 ("cálculo de economia") usa os preços do corpo do texto — se os preços mudarem, o exercício produz respostas erradas.

### 5 testes

- **Joana**: APROVADO — entende a analogia das ferramentas, consegue aplicar o framework de 3 perguntas, e entende o caso da logística. É o capítulo mais acessível do cluster para não-técnicos em termos de framework de decisão.
- **Durabilidade**: BAIXO — a estrutura tripartite (Opus/Sonnet/Haiku) e o princípio de roteamento duram. Todos os dados específicos (preços, benchmarks, versões, nomes de concorrentes) expiram a cada trimestre. O capítulo ficará desatualizado antes do livro ser lançado se os dados não forem movidos ao Apêndice.
- **Diferenciação**: COMMODITY em seção 4.3.1 (tabela de specs é encontrável na documentação oficial), DIFERENCIADO em seção 4.5 (caso da logística com arquitetura detalhada é genuinamente acima da média). O framework de 4.4 é razoável mas qualquer guia de modelos tem algo equivalente.
- **Memorização**: MÉDIO — a analogia do carpinteiro fixa, o framework de 3 perguntas fixa. Os benchmarks específicos não deveriam ser memorizados — e o capítulo os apresenta como se devessem ser.
- **Transformação**: MÉDIO — leitor sai com critério real para roteamento. Mas o capítulo não empurra o leitor a questionar quando roteamento não vale a pena (equipes sem engenharia, protótipos).

### Top lacunas (priorizadas, com seção)

- **[CRÍTICO] Todos os dados perecíveis no corpo** (seção 4.3.1, 4.8, boxes): preços, benchmarks, versões e nomes de concorrentes devem sair do corpo e ir ao Apêndice Vivo. O corpo deve conter apenas o princípio ("Opus custa aproximadamente 20x mais que Haiku — ver Apêndice J para valores correntes"). Esta é a falha estrutural mais grave do capítulo.
- **[ALTO] Ausência de limites reais dos modelos** (seção 4.3): quando Haiku falha? Quando Sonnet é insuficiente? Quais categorias de tarefa a diferença de capacidade se manifesta com maior clareza? O capítulo descreve vantagens de cada tier mas não os failure modes — conhecer quando cada modelo quebra é profundidade técnica real.
- **[ALTO] Ausência de critério para quando NÃO implementar roteamento** (seção 4.4): para equipes sem engenharia suficiente, protótipos em fase inicial, ou orçamentos que não justificam a complexidade de um classificador, roteamento pode custar mais do que economiza. Esse critério está ausente.
- **[MÉDIO] "Manual de botão" em seção 4.6** (padrões de uso): os cinco padrões (Haiku como classificador, Sonnet como motor, Opus para o que importa, extended thinking seletivo, prompt caching consistente) descrevem *o quê* sem explicar *o mecanismo* de por que esse padrão funciona. Parece receita sem raciocínio.
- **[MÉDIO] Ancoragem de Invariante 4 não penetra o texto** (capítulo inteiro): a palavra "Encaixe" aparece apenas no box de abertura. O framework de decisão (4.4) deveria ser explicitamente nomeado como instância do F2-ENCAIXE-5.
- **[MÉDIO] Exercício 2 acoplado a dados perecíveis** (seção 4.11): se os preços do corpo mudarem, o exercício de cálculo de economia produz resultados errados. Referenciar Apêndice no exercício.

### Maior força a preservar

- Seção 4.5 (caso da logística) com a arquitetura de roteamento detalhada (Haiku classificador → Sonnet → Opus extended thinking) é pedagógica em nível de engenharia. É o único trecho do cluster que ensina arquitetura real, não apenas conceito. Preservar com a mesma especificidade operacional.

---

## PADRÃO COMUM — SÍNTESE TRANSVERSAL

**Padrão de lacuna dominante nos três capítulos**: os Invariantes são declarados na abertura mas não voltam no argumento. Os capítulos abrem com box de ancoragem e fecham a conexão — o meio do texto opera como se os Invariantes não existissem. Isso não é integração de método, é decoração de método. Para um leitor que não leu o L1, os boxes são ruído; para quem leu o L1, são promessas não cumpridas.

**Segundo padrão**: dados perecíveis fora do Apêndice Vivo. C04 é o mais grave (preços, benchmarks, versões todas no corpo), C02 tem problema significativo (linha do tempo com versões e benchmarks), C01 é o mais limpo. A abertura de todos os capítulos aponta o Apêndice Vivo, mas nenhum dos três o usa sistematicamente no corpo.

**Terceiro padrão**: ausência de critério de "quando não usar / quando evitar a ferramenta". C01 tem anti-padrões mas não critério de não-uso. C02 não tem framework de não-escolher-Claude. C04 não tem critério de não-implementar-roteamento. Este é o elemento 3 da régua e é a falha nº1 identificada na auditoria — confirmada em todos os três capítulos.

---

## LINHAS-TRACKER

```
C01|5/10|MÉDIO|Ausência total de mecânica técnica nas ferramentas citadas (Briefing/Research/Tasks) + analogia ausente + Framework F1-DECID-IA fantasma
C02|7/10|BAIXO|Dados perecíveis no corpo (linha do tempo, benchmarks, receitas) + ausência de framework de decisão de provedor
C04|6/10|ALTO|Preços/benchmarks/versões no corpo do texto em vez do Apêndice Vivo + limites reais dos modelos ausentes
```

---

*Auditoria gerada em 2026-06-17 · Banca Editorial Adversarial · Deep Claude Cluster A*
