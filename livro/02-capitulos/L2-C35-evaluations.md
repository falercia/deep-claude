# CAPÍTULO 35
## EVALUATIONS

---

> *"Sem medição, toda mudança de prompt é fé. Sem critério, toda avaliação é gosto. Sem regressão, toda melhoria é sorte. Eval é o que separa engenharia de adivinhação sofisticada."*

---

> 🧭 **Por que este capítulo é a aplicação do Invariante 7 — Termômetro**
>
> O Invariante 7 afirma que sem medição você não opera: adivinha. Sistemas probabilísticos como modelos de linguagem não têm comportamento fixo — a mesma entrada em condições ligeiramente diferentes pode produzir saídas distintas, e qualquer mudança de prompt, modelo ou pipeline que você fizer amanhã pode degradar silenciosamente algo que funcionava hoje. Eval é o termômetro que converte "parece que melhorou" em "melhorou 12 pontos em precisão e não regrediu em cobertura". Sem ele, qualquer afirmação sobre desempenho do sistema é anedota, não evidência.
>
> O framework estrutural de hierarquias de eval está em **[L1-F8 — Pirâmide da Avaliação](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md)** (Livro 1). Este capítulo é a aplicação concreta desse framework no contexto de sistemas Claude: os tipos de critério, o método de construir golden sets honestos, a decisão sobre quando confiar no LLM-as-judge, e os sinais de que seu eval está medindo o que é fácil em vez do que importa.

---

## 35.1 — O CONCEITO INTUITIVO

Toda organização que coloca um sistema de IA em produção enfrenta, cedo ou tarde, a mesma questão: como saber se está funcionando? A resposta óbvia — "testamos antes de subir" — esconde um problema estrutural. Testar uma vez, antes do deploy, diz como o sistema se comportou em uma janela de tempo com um conjunto de casos. Não diz nada sobre o que vai acontecer quando o prompt mudar, quando o modelo for atualizado pelo fornecedor, quando o volume de dados reais começar a divergir dos casos de teste, ou quando uma regressão silenciosa aparecer três semanas depois de uma mudança aparentemente inócua.

O problema é que sistemas probabilísticos não têm contrato fixo. Um software determinístico — um compilador, uma função matemática, um parser — se você rodar a mesma entrada amanhã, recebe a mesma saída. Modelos de linguagem não têm essa garantia. Temperatura, versão de modelo, formulação ligeiramente diferente do prompt, contexto diferente na janela — tudo isso pode mudar o resultado. Isso não é um defeito: é a natureza de um sistema que generaliza. Mas significa que qualidade, nesse contexto, não é uma propriedade que você estabelece uma vez. É uma propriedade que você mede continuamente.

Eval é o mecanismo que torna possível essa medição contínua. Um eval bem construído responde a perguntas específicas: meu sistema classifica sentimento corretamente em pelo menos X% dos casos? Quando recupero documentos via RAG e gero uma resposta, a resposta é fiel ao documento recuperado? Quando o usuário fornece um número financeiro incorreto no input, o sistema aponta o erro em vez de calcular sobre ele? Cada uma dessas perguntas tem uma resposta verificável — e verificar sistematicamente é o que distingue operação de esperança.

A Anthropic coloca isso de forma direta em sua documentação de desenvolvimento: construir uma aplicação bem-sucedida baseada em LLM começa por definir critérios de sucesso claros e depois desenhar avaliações para medir desempenho contra eles. Esse ciclo — critério, medição, iteração — é o núcleo da engenharia de prompt. O que a maioria das equipes faz é o inverso: iteração de prompt sem critério explícito, avaliação por sensação, e surpresa quando o sistema regride num caso que "sempre funcionou".

---

## 35.2 — ANALOGIA: O TERMÔMETRO DO PROCESSO INDUSTRIAL

Uma refinaria de petróleo processa fluxos de temperatura, pressão e composição química em centenas de pontos do processo. Os operadores não decidem se o processo está "bom" com base em impressão visual da fumaça ou no cheiro do produto final. Cada ponto crítico tem um sensor, cada sensor tem uma faixa de operação, e o painel de controle mostra — em tempo real — o que está dentro do envelope e o que está saindo.

O termômetro não torna o processo mais inteligente. O operador continua sendo quem decide o que fazer quando a temperatura sobe. Mas sem o termômetro, o operador não sabe que a temperatura subiu até o produto estar fora da especificação, a corrida estar contaminada, ou a planta estar em situação de risco. A intervenção que teria custado uma hora de ajuste passa a custar uma parada completa.

Eval funciona exatamente assim. O sistema de IA continua sendo operado por engenheiros que tomam decisões sobre prompt, modelo e pipeline. O eval é o painel de controle que diz, antes que o problema chegue ao usuário final: isso saiu do envelope. A diferença entre uma equipe que descobre regressões por reclamação de usuário e uma equipe que descobre regressões no CI antes do merge é a existência de termômetros confiáveis.

A propriedade mais importante de um termômetro não é precisão absoluta: é consistência. Um termômetro que sempre mede dois graus acima da temperatura real é utilizável — você aprende o offset e opera. Um termômetro que ora mede certo, ora mede aleatoriamente, é inútil — e perigoso, porque dá falsa segurança. O mesmo vale para evals: consistência do método importa mais do que perfeição do critério.

---

## 35.3 — A TÉCNICA: CONSTRUINDO EVALS QUE MEDEM O QUE IMPORTA

### 35.3.1 — Anatomia de um eval

Todo eval tem três componentes que precisam estar explícitos antes de você escrever uma linha de código:

**Conjunto de casos representativos.** Uma coleção de inputs que reflete a distribuição real de uso do sistema — não os casos fáceis que você usou durante o desenvolvimento, não casos hipotéticos construídos a partir do que você esperava que o usuário enviaria, mas casos que capturam o que de fato chega ao sistema. Isso inclui os casos típicos (alta frequência, relativamente fáceis), os casos de borda (baixa frequência, mas onde falha é custosa), e os casos adversariais (inputs que testam comportamentos que o sistema nunca deve ter). Um conjunto de casos não é estático: precisa ser revisado periodicamente à medida que o perfil de uso real evolui.

**Critério de sucesso explícito.** A definição operacional de "certo" e "errado" para aquele conjunto. Critérios vagos — "a resposta deve ser boa", "o tom deve ser adequado" — produzem avaliações inconsistentes que não geram sinal comparável. Critérios operacionais — "o campo de CNPJ deve ser validado antes do cálculo", "a resposta não deve conter o nome do cliente no terceiro parágrafo", "o score de satisfação atribuído deve coincidir com o score humano em pelo menos 80% dos casos" — podem ser aplicados consistentemente por diferentes avaliadores, incluindo LLMs.

**Método de pontuação.** Como você vai medir a distância entre a saída real do sistema e o critério de sucesso. Isso é separável do critério: o mesmo critério pode ser verificado por exact match em campos estruturados ou por LLM-as-judge em texto livre. A escolha do método de pontuação tem consequências diretas em custo, velocidade, cobertura e confiabilidade do eval.

![Diagrama 35.1 — Os três componentes de um eval e seus pontos de falha](imagens/cap-35-img-01-anatomia-eval.svg)

A Anthropic estabelece três princípios de design de eval que sintetizam bem essa anatomia: ser específico para a tarefa (o eval deve refletir a distribuição real de uso, incluindo edge cases), automatizar quando possível (estruture questões para pontuação automática), e priorizar volume sobre qualidade individual de cada caso (mais casos com sinal ligeiramente menor é superior a poucos casos com avaliação humana perfeita). Esse terceiro princípio é contraintuitivo mas robusto: a variância de avaliação humana em casos individuais é alta o suficiente para que cinquenta casos com LLM-judge calibrado geralmente oferecem melhor discriminação estatística do que dez casos revisados por especialista.

### 35.3.2 — Tipos de critério: da determinística ao julgamento

Existem três grandes famílias de método de pontuação, e a decisão sobre qual usar não é de gosto — é de adequação ao critério de sucesso.

**Exact match e regras programáticas.** Para saídas onde há uma resposta correta verificável — um campo estruturado com valor esperado, um formato que deve seguir um schema, um trecho que deve ou não deve aparecer na saída — comparação determinística é o método correto. É o mais barato, o mais rápido, o mais confiável, e o mais escalável. A Anthropic recomenda explicitamente essa camada como a primeira a implementar: `output == golden_answer` para exact match, `key_phrase in output` para string match, schema validation para campos estruturados. Essa camada cobre regressões grosseiras — formato quebrado, campo faltante, número ausente — com custo próximo de zero por execução.

O limite do método determinístico é claro: para texto livre onde há múltiplas formulações corretas, ou para dimensões de qualidade que não são redutíveis a regras, exact match não discrimina. Um resumo executivo "correto" pode ser escrito de dezenas de maneiras igualmente válidas; nenhuma delas vai bater no exact match.

**LLM-as-judge.** Para dimensões de qualidade semântica — coerência, relevância, fidelidade ao documento fonte, tom adequado, completude da análise — o método prático em escala é usar um modelo de linguagem como avaliador. O princípio é o mesmo que uma rubrica de prova discursiva: você define critérios explícitos e o avaliador aplica esses critérios com consistência.

A documentação da Anthropic estabelece três diretrizes para LLM-as-judge eficaz. Primeiro, rubricas detalhadas e claras: em vez de "avalie se a resposta é boa", "a resposta deve sempre mencionar o nome do produto no primeiro parágrafo — se não mencionar, classifique como 'incorreto'". Segundo, output empírico ou específico: instruir o modelo a produzir 'correto' ou 'incorreto', ou uma escala de 1 a 5, não uma avaliação qualitativa aberta que é difícil de agregar. Terceiro, encorajar raciocínio antes do veredito: pedir que o judge pense passo a passo antes de dar a nota melhora a qualidade da avaliação em tarefas de julgamento complexo, e o raciocínio pode ser descartado após o veredito.

**Humano no loop.** A camada mais cara e mais precisa. Necessária onde LLM-as-judge não captura nuances do domínio — casos clínicos que exigem raciocínio médico, textos jurídicos com implicações de interpretação, análises financeiras onde a tese de risco precisa de contexto do mercado local. Conforme o L1-F8, essa camada cobre tipicamente 5% a 15% da carga, por amostra, e serve também como calibração periódica do judge LLM: se a correlação entre o judge e o especialista humano cair abaixo de um limiar acordado, o juiz precisa ser recalibrado.

![Diagrama 35.2 — A hierarquia de métodos de pontuação por custo, velocidade e aplicação](imagens/cap-35-img-02-metodos-pontuacao.svg)

### 35.3.3 — Eval offline vs. eval online

Esses dois modos de avaliação medem coisas diferentes e são complementares — não substitutos.

**Eval offline** (também chamado de dataset golden ou eval de bancada) opera em um conjunto fixo de casos controlados, fora do fluxo de produção. Você roda o sistema contra o dataset, computa as métricas, e compara com o baseline da versão anterior. Esse é o gate que protege a produção: antes de qualquer mudança de prompt, modelo ou pipeline ser promovida, ela precisa passar pelo eval offline. É também o único modo que permite testar casos adversariais de forma sistemática — você não espera que um usuário tente injetar prompts no sistema de produção para testar se ele resiste.

A propriedade fundamental do eval offline é a reprodutibilidade: o mesmo dataset, o mesmo critério, execuções diferentes do sistema devem produzir métricas comparáveis. Isso requer que o dataset golden seja versionado como código, que o método de pontuação seja determinístico ou tenha variância controlada, e que a política de bloqueio (qual delta de regressão bloqueia um merge) seja definida explicitamente antes de precisar dela.

**Eval online** opera sobre o tráfego real de produção — seja por amostragem de interações reais para avaliação humana ou por LLM-as-judge aplicado ao fluxo ao vivo, seja por métricas de negócio que são proxies de qualidade (taxa de escalação para suporte humano, taxa de rejeição de resposta pelo usuário, tempo para conclusão de tarefa). Eval online captura o que eval offline sistematicamente perde: a distribuição real de inputs que difere do dataset golden, sazonalidades, mudanças de comportamento do usuário, e efeitos de longo prazo que só aparecem em escala.

A tensão prática entre os dois modos é inevitável: eval offline é controlado mas não reflete produção perfeitamente; eval online é real mas ruidoso e difícil de isolar causalidade. A resposta não é escolher um — é instrumentar os dois e usar cada um para o que é bom. Offline para gate de release; online para detecção de drift e para alimentar novos casos ao dataset golden.

### 35.3.4 — A pirâmide de evals e a hierarquia de cobertura

O L1-F8 define uma hierarquia de três camadas que determina quanto investir em cada nível de avaliação em função do risco da tarefa. Este capítulo não vai replicar esse framework — a decisão de como montar a pirâmide de cobertura por camada está lá, com os anti-padrões e o exemplo completo. O que este capítulo acrescenta é a aplicação prática da hierarquia ao contexto de sistemas Claude:

A **base determinística** é a primeira camada a implementar, sempre. Schema validation, exact match em campos críticos, verificação de presença de elementos obrigatórios. Cobertura de 100% das chamadas, custo próximo de zero, implementação em dias. Detecta regressões grosseiras antes que cheguem ao usuário. Qualquer sistema Claude em produção sem essa camada está operando sem termômetro de emergência.

A **camada de golden set com LLM-as-judge** é onde a maioria dos times precisa investir mais e investe menos. Requer construir um dataset golden honesto (ver seção 35.3.5), definir uma rubrica calibrada contra humano, e rodar o judge em cobertura parcial da carga. O retorno é alto: captura regressão de qualidade semântica que a base determinística não vê.

O **topo com revisão humana especialista** fecha o ciclo de calibração. Sem ele, o LLM-as-judge pode derivar sistematicamente da qualidade real ao longo do tempo sem que você perceba — o judge continua pontuando consistentemente, mas a consistência é em relação a um critério que divergiu do critério humano real.

A **faixa transversal adversarial** é separada das três camadas verticais porque mede comportamentos que as camadas verticais não cobrem por design: resistência a jailbreak, ausência de sycophancy em análise de risco, honestidade de citação, calibração de incerteza. A política de bloqueio aqui é a mais rígida: qualquer passagem em adversarial de segurança bloqueia merge.

### 35.3.5 — Como construir um golden set honesto

Um golden set desonesto — e a maioria é, mesmo sem intenção — é o anti-padrão mais caro em avaliação de sistemas de IA. Ele dá a sensação de rigor sem o rigor: você roda o sistema, as métricas ficam altas, e o sistema falha em produção em casos que "nunca apareceram nos testes".

Existem quatro fontes de desonestidade no golden set que valem nomear:

**Viés de seleção otimista.** O dataset foi construído com casos que o sistema resolve bem — porque você usou os mesmos casos com que iterou o prompt durante o desenvolvimento. O resultado é um eval que mede quão bem você treinou o sistema para esses casos específicos, não quão bem ele generaliza para o uso real.

**Gabarito fabricado.** A resposta esperada foi escrita por alguém que tinha em mente o que o sistema deveria produzir, não o que de fato seria correto para um usuário real. Isso cria circulação: o eval mede proximidade ao gabarito, e o gabarito mede proximidade à intuição de quem construiu o sistema.

**Falta de casos de borda e adversariais.** O dataset cobre o fluxo feliz — inputs bem formados, contexto claro, sem ambiguidade. Os casos onde o sistema mais provavelmente vai falhar — inputs malformados, contexto conflitante, usuário tentando contornar restrições — não estão representados.

**Staleness sem revisão.** O dataset foi construído há seis meses e desde então a distribuição de uso real mudou significativamente, mas o dataset não foi atualizado. As métricas continuam altas no dataset; a qualidade real em produção caiu.

A receita para um golden set honesto tem quatro passos: (1) construir o dataset inicial a partir de logs de produção reais, não de casos hipotéticos — se o sistema ainda não está em produção, use casos de uso reais coletados com usuários, não casos inventados pelo time; (2) incluir explicitamente casos de borda e adversariais que vieram de incidentes anteriores ou de literatura de segurança; (3) escrever o gabarito com critério explícito e, sempre que possível, ter o gabarito revisado por alguém que não construiu o sistema; (4) versionar o dataset e definir uma cadência de revisão trimestral, alimentada por casos novos vindos de produção.

O L1-F8 recomenda como baseline para golden sets iniciais: 30 a 50 casos com gabarito, cobrindo os tipos de tarefa com maior volume em produção, os subgrupos onde regressão seria mais custosa, os edge cases de incidentes anteriores, e os casos onde o modelo falha atualmente. Esse último ponto é contraintuitivo: incluir deliberadamente casos onde o sistema falha hoje garante que o eval detecte melhoras reais, não apenas mantém o nível em casos já resolvidos.

### 35.3.6 — Regressão e CI de prompts

Eval offline conecta com o processo de desenvolvimento através do CI de prompts — a integração contínua aplicada a mudanças de prompt, modelo e pipeline. O princípio é o mesmo do CI de código: antes de qualquer mudança ser promovida para produção, ela passa por um gate automatizado que verifica se as métricas de qualidade mantiveram ou melhoraram o baseline.

A implementação prática requer três componentes que precisam ser decididos antes do primeiro merge: o dataset golden versionado, as métricas e seus baselines correntes, e a política de bloqueio — qual delta de regressão bloqueia merge, qual delta gera alerta mas deixa passar, qual delta é irrelevante. A política de bloqueio não pode ser decidida no momento do incidente; ela precisa estar documentada antes de precisar dela.

Um detalhe operacional que muitas equipes aprendem da forma difícil: a temperatura do modelo afeta a variância do eval. Evals com temperatura zero são reprodutíveis; evals com temperatura alta têm variância que pode fazer uma mudança inócua parecer regressão. Para gates de CI, temperatura zero ou ensemble de múltiplas rodadas é o padrão.

---

## 35.4 — CRITÉRIO DE DECISÃO: TRÊS PERGUNTAS ANTES DE CONFIAR NO EVAL

A seção mais importante deste capítulo não é sobre como construir evals — é sobre como evitar confiar em evals que medem o que é fácil em vez do que importa.

![Diagrama 35.3 — Árvore de decisão de eval](imagens/cap-35-img-03-decisao-eval.svg)

| Pergunta | O que indica | Ação se "não" |
|----------|-------------|----------------|
| O critério de sucesso pode ser verificado por alguém que não construiu o sistema? | Critério objetivo vs. critério dependente de contexto interno | Reescrever o critério como rubrica verificável por terceiro |
| O dataset golden contém casos onde o sistema falha hoje? | Dataset honesto vs. dataset otimista | Incluir deliberadamente casos de falha real e adversariais |
| O método de pontuação discrimina entre "ótimo" e "aceitável" na dimensão que mais importa para o negócio? | Eval que mede o que importa vs. eval que mede o que é fácil | Identificar a dimensão de qualidade mais custosa quando falha e checar se ela tem cobertura |
| O LLM-judge foi calibrado contra humano especialista em pelo menos 30 casos? | Judge confiável vs. judge com viés não mapeado | Calibrar antes de confiar nas métricas para decisão |
| As métricas têm tendência estável ao longo do tempo, sem drift inexplicável? | Eval estável vs. eval com problema de implementação | Investigar variância antes de interpretar mudança de métricas como sinal de qualidade |

**Quando LLM-as-judge é confiável.** O judge é confiável quando a rubrica é suficientemente explícita para que o próprio judge possa explicar por que deu aquela nota, quando a correlação com avaliadores humanos foi verificada em pelo menos 30 casos do domínio específico (não de domínio genérico), quando o judge é um modelo diferente do modelo gerador (evita viés de auto-confirmação), e quando o output é categórico ou ordinal — não uma narrativa aberta.

**Quando LLM-as-judge é perigoso.** O judge é perigoso quando a rubrica é vaga o suficiente para que o judge preencha com seus próprios critérios não declarados, quando não foi calibrado no domínio específico (um judge calibrado em textos de marketing pode ter comportamento completamente diferente em análises técnicas), quando o judge é o mesmo modelo que gerou a saída avaliada (auto-validação inflada), e quando é usado para avaliar dimensões que o próprio judge modela mal — como raciocínio matemático formal, nuances jurídicas locais, ou precisão de citação de fontes que o judge não tem acesso para verificar.

**Sinais de eval enganoso (Goodhart).** A Lei de Goodhart afirma que quando uma medida se torna um alvo, ela deixa de ser uma boa medida. Aplicada a evals de IA, os sintomas são reconhecíveis: o time itera o prompt especificamente nos casos do eval, as métricas sobem consistentemente mas o comportamento em produção não melhora, os casos do eval começam a vazar para o processo de desenvolvimento (o time "sabe" quais casos vão aparecer no teste), e o eval passou a ser visto como obstáculo a vencer, não como termômetro a consultar. A solução estrutural para Goodhart é separar o conjunto de desenvolvimento do conjunto de eval — o time não deve ter acesso aos casos exatos do dataset golden durante a iteração de prompt.

---

## 35.5 — EXEMPLO MEMORÁVEL: TRIAGEM DE LAUDOS MÉDICOS EM HOSPITAL DE MÉDIO PORTE

*Cenário ilustrativo brasileiro.* Um hospital de médio porte no interior de São Paulo implantou um sistema Claude para triagem preliminar de laudos de imagem — o modelo lia o laudo textual, classificava urgência (emergência, prioritário, eletivo) e extraía os achados principais para o médico plantonista. O benefício esperado era reduzir o tempo de revisão do plantonista em 60%.

**O problema com o primeiro eval.** A equipe de TI construiu o primeiro eval com 40 casos: laudos que eles mesmos escreveram como exemplos durante o desenvolvimento, todos bem formatados, com achados claros, sem ambiguidade. O sistema atingiu 94% de acurácia nesses casos. Em produção, a acurácia real observada por feedback dos plantonistas estava próxima de 70% — e os erros eram exatamente nos laudos atípicos: laudos de radiologistas que escreviam em estilo telegráfico, laudos com abreviações locais não padrão, laudos que descreviam múltiplas condições com urgências diferentes.

**O redesenho do eval.** A equipe reconstruiu o dataset a partir de laudos reais anonimizados dos últimos seis meses, selecionados com três critérios: maior volume por tipo de exame, maior custo quando a triagem errava (laudos de AVC e IAM), e casos onde o plantonista tinha discordado da triagem do sistema. O novo dataset tinha 120 casos, com distribuição real de urgência e com gabarito validado por três plantonistas independentes (correlação entre eles: 0,88).

O método de pontuação foi redesenhado com critério binário para a dimensão mais crítica — "a classificação de urgência é igual ou mais conservadora que o gabarito humano?" — mais LLM-as-judge para a qualidade da extração de achados. O judge foi calibrado contra os três plantonistas em 30 casos, atingindo correlação de 0,81. A política de bloqueio: qualquer regressão na dimensão binária de urgência bloqueia deploy, independentemente da melhora em outras métricas.

**Resultado.** Depois de dois ciclos de iteração guiados pelo novo eval, o sistema atingiu 91% na dimensão de urgência (sem sub-triagens), 85% na extração de achados, e o tempo de revisão do plantonista caiu 55% — próximo da meta. Mais importante: o eval passou a detectar regressões em 48 horas sempre que uma atualização de modelo introduzia desvio — semanas antes de qualquer plantonista reclamar.

---

## 35.6 — NA PRÁTICA: TRÊS APLICAÇÕES REPLICÁVEIS

O exemplo anterior mostra o redesenho de um eval desonesto; esta seção entrega o roteiro para construir o primeiro eval honesto. Três aplicações progressivas em complexidade. A forma é *situação → o que fazer → o ponto de julgamento*.

**Aplicação 1 — Base determinística para qualquer sistema em produção.**
*Situação:* o time colocou um sistema Claude em produção sem nenhum eval formal. Mudanças de prompt são testadas "na sensação". *O que fazer:* identifique os três comportamentos obrigatórios do sistema — o que ele sempre deve fazer e o que nunca deve fazer. Codifique esses comportamentos como verificações determinísticas: presença de elemento obrigatório no output (`campo_cnpj` em resposta de análise de contrato), ausência de padrão proibido (nome do cliente no terceiro parágrafo), ou conformidade de formato (JSON válido com campos obrigatórios). Rode essas verificações em 100% das chamadas em produção. *O ponto de julgamento:* se qualquer uma dessas verificações falha mais de 1% das vezes, o problema não é de eval — é do sistema. Corrija o sistema antes de adicionar camadas mais sofisticadas de eval.

**Aplicação 2 — Golden set honesto com LLM-as-judge calibrado.**
*Situação:* a base determinística está rodando, mas o time quer saber se a qualidade semântica do output está estável após mudanças de prompt. *O que fazer:* construa o golden set em três passos: (a) colete 30 a 50 casos de logs de produção reais — não hipotéticos; (b) inclua deliberadamente os casos onde o sistema falhou (incidentes, feedbacks negativos, edge cases conhecidos); (c) escreva o gabarito com critério verificável por terceiro, não dependente de contexto interno. Para o judge: escreva uma rubrica com dois a três critérios objetivos, instrua o judge a raciocinar antes do veredito, use um modelo diferente do gerador, e calibre a correlação do judge contra avaliador humano em pelo menos 20 casos antes de confiar nas métricas. *O ponto de julgamento:* a correlação do judge com o humano precisa ser acima de 0,75 no seu domínio específico (não em domínio genérico). Se não atingir, a rubrica está vaga — reescreva até o judge conseguir explicar por que deu aquela nota.

**Aplicação 3 — CI de prompt com política de bloqueio.**
*Situação:* o time itera prompts com frequência e quer um gate automático que bloqueie mudanças que regridem qualidade. *O que fazer:* versione o golden set como código no repositório. Configure o pipeline de CI para rodar a base determinística e o LLM-as-judge no golden set a cada mudança de prompt candidato. Defina a política de bloqueio antes de precisar dela: qual delta de regressão bloqueia merge (recomendação: qualquer regressão na dimensão mais crítica bloqueia; regressões menores de 3 a 5 pontos em dimensões secundárias geram alerta mas não bloqueiam). Documente quem pode aprovar exceções à política de bloqueio. *O ponto de julgamento:* a política de bloqueio deve estar documentada e acordada com o time antes da primeira vez que precisar bloquear um merge. Política decidida no momento do incidente não é política — é discussão sob pressão.

> 🔧 **EXERCÍCIO**
> Escolha o sistema Claude que você opera ou planeja operar. Escreva em uma frase o critério de sucesso mais importante: o que o sistema deve sempre fazer ou nunca fazer? Agora codifique esse critério como uma verificação programática — uma função que recebe o output e retorna verdadeiro ou falso. Rode essa função em dez casos reais. Se a função retorna falso em mais de um dos dez, o problema está no sistema, não no eval. Se retorna verdadeiro em todos os dez, você tem o embrião da base determinística do seu eval. O passo seguinte é expandir para 50 casos e adicionar as dimensões semânticas que a verificação programática não cobre.

---

## 35.7 — CAMADA VIVA

Nomes de ferramentas de eval, versões de SDKs de testing, preços de APIs de LLM-as-judge e benchmarks correntes de correlação juiz-humano ficam no [Apêndice J — Apêndice Vivo](../04-apendices/L2-APX-J-apendice-vivo.md). O método descrito neste capítulo — anatomia do eval, hierarquia de métodos, construção honesta de golden set, política de bloqueio — é estrutural e sobrevive a atualizações de ferramentas. O que muda são as ferramentas que implementam o método, não o método.

---

## 35.8 — LIMITAÇÕES E CONEXÕES

**Limitação 1: Goodhart institucionalizado.** Quando o eval é visível para o time que itera o prompt, a pressão para melhorar as métricas é legítima mas pode produzir overfitting ao eval. A solução estrutural é separar o dataset de desenvolvimento do dataset de gate — mas isso exige disciplina organizacional que vai além da técnica.

**Limitação 2: Viés do judge não mapeado.** LLM-as-judge tem vieses sistemáticos conhecidos: preferência por respostas mais longas, preferência por linguagem assertiva, sycophancy quando o input contém a resposta esperada, e viés de posição em comparações lado a lado. Nenhuma calibração elimina esses vieses inteiramente — ela os mapeia e os controla. Um judge não calibrado os amplifica sem que o time perceba.

**Limitação 3: O eval mede o sistema em uma janela de tempo.** Um golden set construído em março pode não representar bem a distribuição de uso de setembro. Sem revisão periódica do dataset e sem alimentação de casos novos vindos de produção, o eval envelhece enquanto o sistema continua sendo medido contra ele.

**Conexões.**

- **Capítulo 25 — Engenharia de Prompt Avançada:** eval é o que fecha o ciclo de iteração de prompt. Sem eval, você itera por intuição; com eval, você itera por evidência. O critério de aceitação que o Capítulo 25 exige que você defina antes de escrever o prompt é a especificação do eval. Os dois capítulos são o mesmo processo visto de lados opostos.

- **Capítulo 28 — RAG:** sistemas RAG têm dois pontos de falha distintos — a recuperação e a geração — e eles precisam ser avaliados separadamente. O Capítulo 28 explica por que confundi-los é o erro de calibração mais caro: um pipeline de RAG com recuperação ruim e geração boa produz respostas confiantes baseadas no documento errado. O eval de RAG precisa de métricas de recuperação (precision, recall de chunks) e métricas de geração (faithfulness ao documento recuperado) operando em paralelo.

- **LLMOps (capítulo seguinte — Observabilidade e Operações):** eval offline é o gate antes do deploy; monitoramento de produção é o termômetro depois. Os dois formam o ciclo completo de qualidade: CI de prompt bloqueia regressões antes de chegar ao usuário; monitoramento detecta drift depois que chegou. Sem o capítulo de LLMOps, o eval offline é condição necessária mas não suficiente para operar um sistema de IA com confiança.

---

## 35.9 — RESUMO DO CAPÍTULO 35

Eval não é uma fase de projeto — é uma disciplina contínua que torna possível operar um sistema probabilístico com evidência em vez de fé. Os elementos centrais:

- Todo eval tem três componentes que precisam ser explícitos: casos representativos, critério de sucesso verificável, e método de pontuação adequado ao critério.
- Os métodos de pontuação formam uma hierarquia por custo e cobertura: determinístico (rápido, limitado), LLM-as-judge (escalável, dependente de calibração), humano especialista (preciso, caro). A escolha certa não é a mais sofisticada — é a mais adequada ao critério.
- Eval offline protege a produção com um gate de regressão antes do deploy. Eval online detecta drift depois que o sistema está em produção. Os dois são complementares, não substitutos.
- Um golden set honesto é construído a partir de casos reais — não hipotéticos — e inclui deliberadamente casos onde o sistema falha hoje.
- LLM-as-judge é confiável quando a rubrica é explícita, o judge é diferente do gerador, e a calibração contra humano foi verificada no domínio específico. É perigoso quando qualquer dessas condições não é atendida.
- Sinais de Goodhart: métricas sobem mas produção não melhora, o time itera nos casos do eval, o eval virou obstáculo a vencer. A solução é separar o dataset de desenvolvimento do dataset de gate.
- A pirâmide completa de eval — base determinística, golden set com LLM-judge, topo humano, faixa adversarial — está detalhada no **L1-F8 — Pirâmide da Avaliação** (Livro 1). Este capítulo é a aplicação concreta ao contexto Claude; o framework estrutural fica lá.

---

☐ **UAU do capítulo:** você consegue articular, em uma frase, o critério de sucesso do sistema Claude que você opera ou planeja operar — e dizer como verificaria se uma mudança de prompt melhorou ou piorou esse critério? Se não consegue responder essa pergunta sem hesitar, o eval ainda não existe.

---

> *"A diferença entre um sistema de IA que aprende com o tempo e um que apenas acumula histórico de uso é, invariavelmente, a presença de um eval honesto no loop. Sem termômetro, não há aprendizado — há apenas mudança."*
