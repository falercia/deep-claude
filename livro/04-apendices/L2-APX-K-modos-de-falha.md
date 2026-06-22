# APÊNDICE K — OS 9 MODOS DE FALHA
## Um modo de falha por Invariante violado

---

> *"Modelos passam. Método fica. Quando algo falha numa operação de IA, a pergunta correta raramente é 'qual modelo usou?'. É 'qual Invariante foi violado?' A falha é sempre de método — o modelo apenas executou o que o método autorizou."*

---

Este apêndice é um glossário de antipadrões. Para cada um dos 9 Invariantes do Livro 1, documenta o modo de falha correspondente: como ele aparece na superfície, qual é a causa-raiz estrutural, um exemplo composto e o antídoto — o critério que, aplicado, evita a recorrência.

O propósito não é culpar retrospectivamente, mas criar reconhecimento prospectivo. Um profissional que conhece os 9 modos de falha consegue identificar o padrão antes que o custo se materialize.

---

## Modo de Falha 1 — A CONFIANÇA DO FLUENTE

**Invariante violado:** Inv. 1 — Plausibilidade

**Nome do modo:** Confiança do Fluente

*Sintoma:* O output parece correto — está bem redigido, é coerente internamente, tem o tom certo, cita fontes plausíveis — e o profissional o usa sem verificação. A falha aparece mais tarde, quando alguém com domínio do assunto lê e identifica o erro factual que estava escondido atrás da fluência.

*Causa-raiz:* Modelos de linguagem produzem outputs convincentes mesmo quando o conteúdo está errado. A qualidade da forma não garante a qualidade do conteúdo. Fluência é sinal de treinamento linguístico, não de acesso privilegiado à verdade. Quem trata a ausência de gaguejo como proxy de correção está medindo a coisa errada.

*Exemplo:* Um analista usa Claude para redigir um memorando com dados de mercado. O memorando cita crescimento setorial de 18% em dois anos. O número é plausível dado o contexto — a linguagem ao redor é precisa — mas é uma fabricação estatística. O memorando vai ao board sem verificação porque "pareceu certo". A correção no dia seguinte custa mais do que teria custado a verificação.

*Antídoto:* Todo dado quantitativo, toda afirmação factual verificável e toda referência bibliográfica produzida por modelo de linguagem é hipótese até ser verificada na fonte primária. A regra operacional: o Claude redige; você verifica. A fluência do output não altera esse protocolo.

---

## Modo de Falha 2 — A JANELA QUE ESQUECE

**Invariante violado:** Inv. 2 — Extremidades

*Sintoma:* A conversa começa com contexto rico e produz outputs de alta qualidade. Após muitas trocas, o modelo começa a contradizer instruções dadas no início, a repetir o que já foi resolvido, a perder o fio de decisões anteriores. O profissional percebe que está "treinando o modelo de novo" no meio do trabalho.

*Causa-raiz:* A janela de contexto de qualquer modelo de linguagem é finita. Quando ela se aproxima do limite — ou quando o contexto acumulado se torna denso demais — o modelo começa a comprimir ou descartar o que estava no início para dar espaço ao que chegou por último. As extremidades da janela (início e fim) recebem atenção privilegiada; o meio é o que se perde primeiro. Profissionais que não modelam esse comportamento culpam o modelo quando a culpa está no design da sessão.

*Exemplo:* Uma equipe jurídica usa uma única sessão longa para redigir um contrato completo de 40 cláusulas. Nas últimas cláusulas, o Claude começa a usar terminologia inconsistente com o que foi definido nas primeiras páginas. Ninguém percebe até a revisão final, quando o cliente aponta a inconsistência.

*Antídoto:* Projetar sessões com segmentação consciente. Usar Projects para contexto curado e persistente. Começar sessões novas com resumo explícito das decisões críticas. Para trabalhos longos: dividir em blocos, com handoff formal de contexto entre blocos. Checar coerência nas extremidades, não apenas no output imediato.

---

## Modo de Falha 3 — O NÚMERO IMPRESSO

**Invariante violado:** Inv. 3 — Camada Dupla

*Sintoma:* A organização cita, em decisões internas ou externas, dados sobre modelos de IA — preços, benchmarks, janelas de contexto, disponibilidade de features — que estavam corretos quando o livro ou o relatório foi escrito, mas que foram superados por lançamentos subsequentes. A decisão é tomada com base em uma fotografia velha.

*Causa-raiz:* Qualquer fonte que mistura padrões estruturais com números voláteis no mesmo corpo tem prazo de validade curto. Quem lê o número no corpo do texto — seja de um livro, seja de um relatório interno — tende a tratá-lo como válido sem verificar a data. O modelo de linguagem que produziu o documento não vai avisar que o número ficou obsoleto.

*Exemplo:* Uma empresa decide usar modelo A em vez do modelo B baseada em comparativo de custo publicado em um relatório de arquitetura do ano anterior. No momento da decisão, os preços foram rebalanceados pelo fornecedor e a vantagem se inverteu. O contrato é assinado com o modelo mais caro para a carga de trabalho.

*Antídoto:* Separar padrão de número. Padrão (o critério de decisão, a lógica de roteamento, o framework de governança) vai no corpo permanente. Número (preço, versão, benchmark, disponibilidade) vai em camada viva com data de snapshot e fonte verificável. Consultar a camada viva antes de qualquer decisão que dependa de número — não o corpo do documento.

---

## Modo de Falha 4 — A FERRAMENTA ERRADA NO PROBLEMA CERTO

**Invariante violado:** Inv. 4 — Encaixe

*Sintoma:* A equipe usa um modelo de fronteira para tarefas que não exigem raciocínio profundo, ou usa automação determinística onde a tarefa pede julgamento sobre ambiguidade. Em ambos os casos, o resultado decepcionante é atribuído ao "modelo que não prestou" quando o verdadeiro diagnóstico é encaixe incorreto entre tarefa e ferramenta.

*Causa-raiz:* A escolha de ferramenta é frequentemente feita por familiaridade, por momentum de adoção ou por entusiasmo com a capacidade máxima de um modelo — e não por análise do perfil da tarefa. Usar Claude para classificação binária de alto volume é caro e desnecessário. Usar automação de regra para análise de contratos ambíguos é insuficiente e perigoso. O custo do encaixe errado é pago em dois sentidos: dinheiro a mais ou qualidade a menos.

*Exemplo:* Uma empresa de e-commerce implementa Claude para rotear 200 mil tickets de suporte por mês entre categorias predefinidas. A tarefa pede correspondência de padrão, não raciocínio — qualquer modelo menor ou regra de classificação resolveria com a mesma precisão a fração do custo. O orçamento mensal de IA fica insustentável; a justificativa para cortes recai sobre "IA não entrega ROI".

*Antídoto:* Aplicar os seis critérios de encaixe (Cap. 5b) antes de comprometer qualquer ferramenta em produção: profundidade de raciocínio exigida, ecossistema de integração, governança do dado, custo e latência, reversibilidade do erro, maturidade do caso. O encaixe correto é resultado de análise, não de preferência.

---

## Modo de Falha 5 — O CUSTO QUE NÃO APARECE NA PLANILHA

**Invariante violado:** Inv. 5 — Custo Composto

*Sintoma:* O custo de API parece baixo na análise inicial. Três meses depois, o orçamento de IA explodiu sem que o volume de uso tenha crescido proporcionalmente. A investigação revela prompts redundantes, contextos duplicados, tokens de raciocínio ativados desnecessariamente e retentativas não controladas.

*Causa-raiz:* O custo de operar modelos de linguagem em produção tem múltiplas dimensões que não aparecem na linha de custo por chamada: tokens de input redundante que poderiam ser cacheados, tokens de raciocínio estendido ativados onde não agregam, chamadas de retry após erro que consomem o dobro do esperado, contextos de sessão que crescem sem controle. Profissionais que monitoram apenas custo por chamada não veem o custo composto.

*Exemplo:* Uma equipe de desenvolvimento usa Claude Code para assistência em código. O system prompt tem 8 mil tokens e é reenviado a cada chamada. Ninguém implementa prompt caching. Em três meses de uso intenso, o custo de tokens de input supera o custo de tokens de output em 4 para 1 — e o contexto estável do system prompt é responsável por 70% disso.

*Antídoto:* Instrumentar o custo por dimensão, não apenas por chamada total. Separar o que é estável (candidato a cache) do que é volátil (input dinâmico por chamada). Ativar extended thinking com medição de ganho de qualidade vs. custo incremental — não por padrão. Monitorar crescimento de janela de contexto em sessões longas. O custo composto é controlável; o pré-requisito é que ele seja visível.

---

## Modo de Falha 6 — A AUTONOMIA SEM ÂNCORA

**Invariante violado:** Inv. 6 — Autonomia Proporcional

*Sintoma:* Um agente ou workflow automatizado executa ações de alto impacto sem ponto de revisão humana. Quando algo dá errado — uma ação irreversível executada incorretamente, uma sequência de decisões que foi razoável passo a passo mas desastrosa no conjunto — não há onde intervir nem quem o tenha visto acontecer.

*Causa-raiz:* Autonomia sem âncora é o caso onde a delegação ao modelo foi além da proporção justificada pelo risco da tarefa. O Invariante 6 não é contra autonomia — é a favor de autonomia proporcional: a extensão da delegação deve crescer com a evidência de confiabilidade e encolher com o risco da ação. Delegar ação irreversível sem ponto de aprovação humana não é eficiência; é transferência de risco sem controle.

*Exemplo:* Uma equipe configura um agente para gerenciar campanhas de marketing automaticamente — ajustar lances, pausar anúncios, redirecionar orçamento. O agente, otimizando uma métrica intermediária, redistribui 90% do orçamento de um produto em crescimento para um produto maduro em 72 horas. A ação foi coerente com a métrica instruída; foi desastrosa para a estratégia. Não havia checkpoint de aprovação para redistribuições acima de determinado percentual.

*Antídoto:* Mapear o raio de impacto de cada ação que o agente pode executar. Estabelecer limiares de autonomia — ações abaixo de X impacto executam sem aprovação; acima de X, pedem confirmação. Começar com autonomia restrita e expandir com base em evidência de confiabilidade, não em confiança prévia. Em ações irreversíveis: aprovação humana sempre, sem exceção.

---

## Modo de Falha 7 — O TERMÔMETRO QUE NINGUÉM LÊ

**Invariante violado:** Inv. 7 — Termômetro

*Sintoma:* A equipe sabe que o modelo produz erros, mas não sabe com que frequência, em quais tipos de tarefa, com que impacto. A resposta padrão a falhas é "o modelo às vezes erra" — sem métrica, sem diagnóstico, sem melhoria estrutural.

*Causa-raiz:* Operar IA probabilística sem sistema de avaliação contínua é equivalente a operar um processo industrial sem controle de qualidade: você só descobre a variância quando ela chega ao cliente. Modelos de linguagem não têm comportamento determinístico; a qualidade do output varia por input, por modelo, por prompt. Sem medição sistemática, essa variância é invisível — e invisível significa não-gerenciável.

*Exemplo:* Um banco usa Claude para rascunhar respostas a reclamações de clientes. A equipe revisa todos os rascunhos antes de enviar — mas sem registro de quantos rascunhos são aprovados, quantos são editados substancialmente e quantos são descartados. Seis meses depois, ninguém sabe se o modelo melhorou, piorou ou ficou estável. Não há dado para justificar expansão de uso nem para detectar degradação.

*Antídoto:* Instrumentar avaliação antes de colocar em produção, não depois. Definir critérios de qualidade mensuráveis (não "a resposta foi boa" — mas "a resposta continha X, não continha Y, foi aprovada sem edição substancial"). Monitorar distribuição de qualidade ao longo do tempo. Tratar degradação detectada como sinal de mudança de modelo ou de prompt, não como ruído.

---

## Modo de Falha 8 — A RESPONSABILIDADE TERCEIRIZADA

**Invariante violado:** Inv. 8 — Responsabilidade Indelegável

*Sintoma:* Quando o output do modelo causa dano — um conselho incorreto, uma afirmação falsa publicada, uma decisão com base em análise equivocada — a organização ou o profissional tenta atribuir responsabilidade ao modelo ou ao fornecedor. O resultado é, além do dano original, um dano reputacional adicional por falta de accountability.

*Causa-raiz:* Modelos de linguagem não têm responsabilidade legal, moral ou reputacional. O profissional que usa o output — sem verificação ou com verificação insuficiente — é o responsável pelo efeito do output no mundo. A delegação de geração não transfere a responsabilidade pela saída. Tratar o modelo como coautor que divide culpa é uma ficção que não resiste a qualquer análise jurídica ou ética.

*Exemplo:* Uma consultoria entrega um relatório de due diligence com análise financeira gerada por Claude. O relatório contém uma projeção incorreta que influencia a decisão de aquisição do cliente. A consultoria argumenta que "a IA gerou o número". O cliente argui que a consultoria assinou o relatório. A responsabilidade é da consultoria — integralmente.

*Antídoto:* O protocolo de revisão humana não é opcional em outputs que alimentam decisões de consequência. Estabelecer explicitamente, em cada workflow com IA, quem é o revisor responsável, qual é o critério de aprovação e o que constitui output adequado para liberar. "O modelo gerou" não aparece como justificativa válida em nenhum protocolo de governança que resista ao escrutínio.

---

## Modo de Falha 9 — O OPERADOR AUSENTE

**Invariante violado:** Inv. 9 — Operador

*Sintoma:* O modelo é implantado sem configuração deliberada de contexto, restrições ou objetivos. O comportamento resultante é genérico — útil para o caso médio, inadequado para o contexto específico da organização, do setor ou do usuário. Reclamações frequentes são "o Claude não entende nosso negócio" ou "as respostas são muito genéricas".

*Causa-raiz:* O Invariante 9 define o papel do operador: quem implanta o modelo em um contexto específico é responsável por configurar esse contexto com precisão. Um model de linguagem sem system prompt é um modelo configurado para o caso genérico, não para o caso específico. A lacuna entre "o que o modelo faz por padrão" e "o que a organização precisa que ele faça" não é fechada pelo modelo — é fechada pelo operador.

*Exemplo:* Uma empresa de saúde implementa Claude como assistente interno para equipes administrativas, sem system prompt, sem restrições de domínio, sem contexto organizacional. O assistente responde bem a perguntas gerais, mas dá respostas inadequadas a contextos clínicos (onde não deveria responder), ignora políticas internas (que não foram instruídas) e usa terminologia inconsistente com a da organização. A equipe conclui que "IA não funciona para o nosso contexto" — mas o contexto nunca foi fornecido.

*Antídoto:* Todo deployment de modelo em contexto organizacional começa com design deliberado do system prompt: qual é o papel do modelo, quais são os limites do domínio, quais são as políticas que devem ser respeitadas, qual é o tom e a terminologia da organização. O system prompt é a configuração do operador — e configuração ausente não é neutralidade, é abandono de controle.

---

## QUADRO CONSOLIDADO DOS 9 MODOS

| # | Invariante | Nome do Modo de Falha | Sinal de Alerta | Antídoto em Uma Frase |
|---|---|---|---|---|
| 1 | Plausibilidade | Confiança do Fluente | Output persuasivo usado sem verificação factual | Fluência não é verdade — verifique na fonte primária |
| 2 | Extremidades | Janela que Esquece | Instruções iniciais ignoradas em sessões longas | Projete segmentação de sessão e handoff explícito de contexto |
| 3 | Camada Dupla | Número Impresso | Decisão tomada com dado obsoleto do corpo do documento | Padrão no corpo; número na camada viva com data e fonte |
| 4 | Encaixe | Ferramenta Errada no Problema Certo | Custo alto sem ganho proporcional de qualidade | Aplique os 6 critérios de encaixe antes de comprometer ferramenta |
| 5 | Custo Composto | Custo que Não Aparece na Planilha | Orçamento de IA cresce sem crescimento proporcional de uso | Instrumente custo por dimensão; cache o que é estável |
| 6 | Autonomia Proporcional | Autonomia sem Âncora | Ação irreversível executada sem checkpoint humano | Mapeie raio de impacto; estabeleça limiares de aprovação |
| 7 | Termômetro | Termômetro que Ninguém Lê | Variância de qualidade invisível sem métrica | Instrumentar avaliação antes de produção, não depois |
| 8 | Responsabilidade Indelegável | Responsabilidade Terceirizada | Dano atribuído ao modelo quando o profissional assinou o output | Revisão humana não é opcional em outputs de consequência |
| 9 | Operador | Operador Ausente | Respostas genéricas, contexto organizacional ignorado | System prompt é configuração do operador — ausência não é neutralidade |

---

> *"Os 9 modos de falha não são catálogo de erros alheios — são espelho de método próprio. Quem os conhece não os evita por sorte. Evita por critério."*
