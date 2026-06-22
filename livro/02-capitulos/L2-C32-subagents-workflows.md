# CAPÍTULO 32
## SUBAGENTS E WORKFLOWS

---

> *"Quando uma tarefa cresce além do que um único agente faz bem, dividir entre subagentes especializados muda o que se torna possível. É o padrão das equipes que entregam o que antes parecia inviável."*

---

> 🧭 **Por que este capítulo é a aplicação do Invariante 6 — Autonomia Proporcional**
>
> Subagentes só fazem sentido com observabilidade proporcional à autonomia que recebem. Sem tracing e sem rollback, sub-rotina vira loop opaco com custo composto crescente. O F3 — AGENTE-PROP define os níveis de delegação por capacidade de rastrear e reverter.

---

## 32.1 — O CONCEITO INTUITIVO

Existe um ponto na complexidade de tarefas em que um único agente Claude, mesmo o mais capaz, começa a falhar. O contexto inflado prejudica atenção, a variedade de tools necessárias confunde a decisão sobre qual usar, a longa sequência de passos acumula erros que se compõem, a especialização em diferentes domínios é demandada simultaneamente. Para essas tarefas, a resposta arquitetural é Subagents: distribuir o trabalho entre múltiplos agentes especializados, com um agente principal orquestrando o conjunto.

Subagents é capacidade nativa do Claude em 2026, disponível em Claude Code e em fluxos avançados: o agente principal invoca subagentes com objetivos delimitados, contexto isolado, conjunto próprio de tools e Skills específicas. Cada subagente trabalha em sua especialidade sem ser distraído por considerações fora do seu escopo, e o agente principal consolida os resultados em entrega final coerente. A analogia próxima do mundo profissional é a de gerente de projeto coordenando especialistas, em vez de tentar fazer tudo sozinho.

Para fluxos complexos que envolvem pesquisa profunda, análise estruturada, redação cuidadosa, validação técnica, o padrão multi-agente entrega resultado qualitativamente superior ao que agente único conseguiria. É o padrão que separa equipes maduras das que operam em fluxos simples.

---

## 32.2 — ANATOMIA DA ORQUESTRAÇÃO


![Diagrama 32.1 — Subagents em ação: decomposição, especialização, consolidação](imagens/cap-32-img-01-subagents.svg)


O **agente principal** recebe o objetivo geral do usuário, faz decomposição em subtarefas que mapeiam para especializações disponíveis, invoca cada subagente apropriado com instruções específicas, e consolida os resultados em entrega final ao usuário. É o papel de coordenação, com visão de conjunto que cada subagente individual não precisa ter.

Cada **subagente** opera com contexto próprio, separado do agente principal. Isso é importante porque significa que o subagente não recebe a totalidade do contexto da conversa principal, apenas o que é relevante para sua tarefa específica. Com isso, o contexto fica focado, a atenção calibrada e a resposta de qualidade superior. Cada subagente pode usar conjunto próprio de tools, Skills específicas, modelos diferentes (Opus para tarefas que pedem profundidade, Sonnet para as mais comuns, Haiku para as mais simples).

A **especialização** pode seguir várias dimensões. Por domínio (subagente jurídico, subagente financeiro, subagente técnico). Por etapa do processo (subagente de pesquisa, subagente de análise, subagente de redação). Por modelo (subagente de raciocínio profundo em Opus, subagente de processamento em volume em Haiku). A escolha de como dividir depende da natureza da tarefa.

A **comunicação** entre agente principal e subagentes é estruturada. O principal envia objetivo claro com critério de sucesso, o subagente executa e retorna resultado em formato estruturado; o principal aprova ou solicita refinamento. Não é conversa livre, é interface programática.

---

## 32.3 — QUANDO USAR SUBAGENTS

Subagents rendem em alguns contextos e atrapalham em outros — a distinção é operacionalmente importante.

**Rendem em tarefas complexas com múltiplas especializações**, em que o resultado depende de competências distintas executadas em coordenação. Pesquisa profunda multi-domínio, análise estratégica integrando dados financeiros, técnicos e de mercado, geração de proposta comercial que precisa de pesquisa, análise e redação.

**Rendem em tarefas com paralelismo natural**, em que subtarefas podem ser executadas independentemente. Análise simultânea de várias fontes, processamento de lotes, varredura de múltiplos sistemas em paralelo.

**Rendem em tarefas longas que se beneficiam de contexto isolado**, em que um único agente acumularia contexto grande demais. Refatoração de base de código grande, due diligence ampla, pesquisa de mercado profunda.

**Atrapalham em tarefas simples**, em que dividir adiciona overhead sem ganho. Para perguntas simples, agente único é mais rápido e barato.

**Atrapalham quando a coordenação custa mais que a especialização rende**, ou seja, quando o agente principal precisa fazer trabalho desproporcional para integrar resultados que poderiam ter sido produzidos diretamente.

---

## 32.4 — EXEMPLO MEMORÁVEL: A PROPOSTA DE 8 PÁGINAS EM 25 MINUTOS

Uma agência de consultoria estratégica brasileira, com cerca de 30 consultores, recebia regularmente RFPs (Request for Proposals) de potenciais clientes corporativos. Cada proposta de qualidade exigia entre 12 e 20 horas de trabalho consolidado de pesquisa, análise, formatação, customização. Em meio a múltiplos deals em curso, isso virava gargalo.

Em fevereiro de 2026, uma sócia construiu um fluxo multi-agente em Claude Code para preparar primeira versão de propostas. A arquitetura final ficou assim.

**Subagente Pesquisador** recebia nome da empresa cliente e setor, fazia varredura web e em bases internas, produzia briefing de 2 páginas sobre a empresa, contexto setorial, desafios típicos, decisões recentes. Usava Opus com Web Search ativo, com Skill de pesquisa corporativa.

**Subagente Analista** recebia o briefing e o escopo do RFP, identificava qual oferta da consultoria melhor encaixava, identificava casos similares anteriores na base, propunha abordagem com cronograma e equipe, identificava riscos. Usava Opus com Knowledge Base da casa carregada.

**Subagente Redator** recebia briefing e análise, gerava primeira versão da proposta seguindo template padrão da casa, com tom e estrutura calibrados pela Skill de escrita corporativa. Usava Sonnet por velocidade, com Skill de proposta comercial.

**Subagente Revisor** recebia a proposta gerada, fazia checagem contra critérios de qualidade, identificava lacunas, propunha melhorias específicas. Usava Opus em modo extended thinking, com check-list de revisão da casa.

**Agente Principal** orquestrava tudo. Recebia o RFP do usuário, disparava os subagentes em sequência apropriada, consolidava os resultados, entregava proposta final de 8 páginas com pontos de atenção marcados.

O resultado, depois de duas semanas de refinamento dos prompts e Skills, foi notável. **Tempo médio para primeira versão de proposta caiu de 16 horas para 25 minutos.** Qualidade da primeira versão melhorou em testes cegos comparativos com versões manuais, principalmente pelo trabalho do Subagente Revisor que aplicava checklist consistente que humanos esqueciam.

A revisão humana subsequente continuava existindo, com um consultor sênior dedicando 1 a 2 horas para polir, customizar para nuances específicas do cliente, validar números, ajustar tom. **O trabalho total caiu de 16 horas para cerca de 2 horas humanas, com qualidade superior.** Em três meses, a vazão de propostas qualificadas quintuplicou, sem aumento de pessoal.

A lição estrutural é que **tarefas que pareciam exigir muitas horas humanas frequentemente são compostas de subtarefas especializáveis, e quando especializadas em subagentes coordenados, viram fração do esforço original**. Esse padrão se aplica a praticamente toda tarefa cognitiva complexa em organizações de conhecimento, e quem domina arquitetura multi-agente capta vantagem desproporcional sobre quem ainda opera com agente único genérico.

---

## 32.5 — WORKFLOWS, PADRÕES DE ORQUESTRAÇÃO

Subagents pode ser orquestrado em padrões que valem ser conhecidos.

**Pipeline sequencial** é o padrão mais simples, com subagentes executando em sequência, cada um recebendo input do anterior. Ideal para fluxos lineares como o exemplo da proposta acima.

**Paralelismo** dispara múltiplos subagentes simultaneamente para subtarefas independentes, com agente principal consolidando ao final. Reduz tempo total mas exige tarefas verdadeiramente independentes.

**Orquestrador com especialistas** tem agente central que decide dinamicamente qual subagente invocar para cada parte da tarefa, em vez de sequência fixa. Mais flexível mas mais complexo.

**Hierarquia** tem múltiplos níveis de subagentes, com subagente principal que por sua vez invoca subagentes próprios. Útil em tarefas verdadeiramente grandes. Limite prático recomendado: não mais que dois níveis de hierarquia antes de testar o comportamento exaustivamente — cada nível adicional multiplica a superfície de falha e o custo de debug.

**Debate** tem subagentes adversariais discutindo, com agente principal sintetizando o melhor de cada posição. Para decisões com trade-offs onde múltiplas perspectivas importam. O risco específico deste padrão: loop de refinamento sem convergência, onde os subagentes continuam produzindo posições sem que o principal consiga sintetizar. Adicione limite de rodadas de debate e critério explícito de resolução antes de ativar.

---

## 32.6 — GOVERNANÇA DE SUBAGENTS: O QUE A ABERTURA PROMETEU E O CORPO PRECISA ENTREGAR

A abertura deste capítulo afirma que "sem tracing e sem rollback, sub-rotina vira loop opaco com custo composto crescente". Esta seção entrega o método para evitar exatamente isso.

Subagents sem governança têm quatro pontos de falha típicos que aparecem em produção:

**1. Custo acumulado invisível.** Cadeia de subagentes pode consumir tokens em volume muito acima do estimado, especialmente quando subagentes chamam outros subagentes ou quando qualquer deles entra em loop. Configure alertas de custo por execução e por janela de tempo antes de colocar fluxo multi-agente em produção. Em Claude Code, a configuração `--max-turns` limita o número de turnos por subagente; use-a.

**2. Falha silenciosa de subagente.** Subagente que retorna resultado vazio ou malformado pode não interromper o fluxo — o agente principal pode continuar com input degradado e entregar resultado aparentemente correto mas incorreto. Implemente validação de schema no output de cada subagente antes de passar para o próximo. Se o output não passa na validação, o fluxo interrompe e reporta o ponto de falha.

**3. Erro com ferramenta destrutiva sem rollback.** Subagente com acesso a tools de escrita (criar arquivo, enviar mensagem, modificar banco de dados) pode executar ação irreversível antes que você perceba que o contexto estava errado. Para qualquer subagente com ferramentas destrutivas: (a) adicione passo de confirmação humana antes da ação, ou (b) implemente dry-run que mostra o que seria feito sem executar, ou (c) use pattern de staging onde a ação é reversível por um período definido.

**4. Debug impossível sem tracing.** Quando um fluxo de 4 subagentes entrega resultado errado, sem tracing você não sabe em qual subagente o erro entrou. Cada subagente deve logar: input recebido, output produzido, tools chamadas, tempo de execução. Em Claude Code, o arquivo `.claude/` registra a sessão; para fluxos multi-agente em produção, considere logging explícito no prompt de cada subagente.

### O pré-flight check antes de colocar multi-agente em produção

Antes de ativar qualquer cadeia de subagentes em contexto que afeta outros ou custa recurso real:

| Check | Pergunta | Se "não": |
|-------|----------|-----------|
| **Custo** | Você tem limite configurado de gasto máximo por execução? | Configure `--max-turns` e alerta de custo |
| **Fallback** | Se um subagente falhar, o fluxo interrompe e reporta? | Implemente validação de output |
| **Reversão** | Actions destrutivas têm dry-run ou confirmação humana? | Adicione antes de ativar |
| **Tracing** | Você consegue ver qual subagente produziu qual output? | Adicione logging por subagente |
| **Limite de hierarquia** | A cadeia tem mais de dois níveis? | Teste exaustivamente ou simplifique |

---

## 32.7 — NA PRÁTICA: TRÊS APLICAÇÕES REPLICÁVEIS

O exemplo anterior mostra o resultado de uma arquitetura madura; esta seção entrega o roteiro de entrada. Três aplicações progressivas, da mais simples à mais complexa. A forma é *situação → o que fazer → o ponto de julgamento*.

**Aplicação 1 — Pipeline sequencial para tarefa com três especialidades.**
*Situação:* você executa regularmente uma tarefa que combina pesquisa, análise e redação — e o resultado sofre quando as três fases competem pelo mesmo contexto. *O que fazer:* decomponha em três subagentes sequenciais com contexto isolado; o primeiro recebe o brief e retorna pesquisa estruturada; o segundo recebe apenas a pesquisa e retorna análise com conclusões; o terceiro recebe análise e brief e redige o output final. Antes de ativar em produção, preencha o pré-flight check da seção 32.6: custo máximo configurado, validação de output de cada subagente, nenhum deles com ação destrutiva. *O ponto de julgamento:* quando o segundo subagente recebe a pesquisa do primeiro, o output faz sentido isolado — sem contexto da conversa original? Se não fizer, o contrato de interface entre subagentes está mal definido.

**Aplicação 2 — Paralelismo para análise de múltiplas fontes independentes.**
*Situação:* a tarefa exige analisar cinco documentos ou fontes distintas e sintetizar o melhor de cada um. Sequencial é lento; as análises são verdadeiramente independentes entre si. *O que fazer:* dispare cinco subagentes em paralelo, cada um recebendo apenas o documento que lhe compete; defina o schema de saída que cada um deve respeitar; o agente principal recebe os cinco outputs e sintetiza. Configure timeout individual por subagente — se um demorar mais que o dobro dos outros, é sinal de falha, não de trabalho extra. *O ponto de julgamento:* a síntese do agente principal deve ser coerente mesmo se um dos subagentes retornar output parcial ou vazio. Se o agente principal travar quando qualquer subagente falha, o isolamento de falha não foi implementado.

**Aplicação 3 — Orquestrador com padrão de debate para decisão com trade-offs.**
*Situação:* a decisão tem dimensões que se contradizem — custo vs. velocidade, risco vs. oportunidade — e você quer perspectivas adversariais antes de sintetizar. *O que fazer:* construa dois subagentes com papéis opostos (defensor e crítico); cada um recebe o mesmo brief e o output do outro; o agente principal recebe as duas posições com critério explícito de resolução. Defina no sistema do agente principal o número máximo de rodadas de debate (duas a três) e o critério de como resolver quando as posições persistirem. *O ponto de julgamento:* o critério de resolução do agente principal deve ser declarado antes de rodar, não inferido. Se o principal não consegue decidir sem rodar mais uma rodada, o critério está vago — reescreva o critério até o principal conseguir decidir com o que tem.

> 🔧 **EXERCÍCIO**
> Identifique uma tarefa complexa que você ou o time executa com Claude hoje, que envolve ao menos duas especialidades distintas (ex.: pesquisa + redação, análise técnica + comunicação executiva). Desenhe a decomposição em subagentes: quantos, o que cada um recebe, o que cada um devolve, em qual formato. Preencha o pré-flight check da seção 32.6 para a arquitetura desenhada. Se algum dos cinco checks retornar "não", escreva o que precisaria construir antes de ativar. Sem os cinco checks respondidos afirmativamente, o fluxo é protótipo, não produção.

---

## 32.8 — RESUMO E CONEXÕES

🔗 **Conexões:** [Agentes (Cap 12)](../../Livro-1-Os-Invariantes/02-capitulos/L1-C12-agentes.md) · [MCP (Cap 13)](../../Livro-1-Os-Invariantes/02-capitulos/L1-C13-mcp.md) · [Claude Code (Cap 24)](L2-C09-claude-code.md) · [Skills (Cap 30)](L2-C31-skills.md)

| Conceito | Síntese |
|----------|---------|
| **Subagents** | Agentes especializados invocados por agente principal |
| **Especialização** | Por domínio, etapa do processo ou modelo |
| **Contexto isolado** | Cada subagente opera com contexto próprio focado |
| **Padrões** | Pipeline, paralelismo, orquestrador, hierarquia, debate |
| **Quando usa** | Tarefas complexas com múltiplas especializações, paralelismo natural, contexto que inflaria demais |
| **Quando evita** | Tarefas simples, coordenação custa mais que especialização rende |
| **Governança obrigatória** | Limite de custo, validação de output, dry-run em actions destrutivas, tracing por subagente |

## 32.9 — EXERCÍCIOS

| # | Exercício | O que desenvolve |
|---|-----------|-----------------|
| 1 | **Mapeie um fluxo candidato.** Identifique uma tarefa complexa que você faz com Claude e que tem múltiplas especializações (pesquisa + análise + redação, por exemplo). Desenhe quais subagentes existiriam, o que cada um recebe e o que entrega. | Visão de arquitetura multi-agente |
| 2 | **Identifique três fluxos que NÃO se beneficiam de subagentes.** Para cada um, escreva por quê: tarefas simples demais, coordenação mais cara que o ganho, contexto não inflado o suficiente. O critério reverso é tão importante quanto o critério positivo. | Julgamento de quando multi-agente é overhead |
| 3 | **Aplique o pré-flight check.** Para o fluxo candidato do exercício 1, preencha os 5 checks da tabela de governança (seção 32.6). Para cada "não": o que você precisaria construir antes de ativar? Isso decide se o fluxo está pronto para produção ou ainda é protótipo. | Governança de Autonomia Proporcional em prática |

🔗 **Próximo capítulo:** [Capítulo 33 — Computer Use](L2-C33-computer-use.md)

---

> *"Tarefas complexas dividem em subtarefas especializáveis. Quem entende isso constrói arquiteturas que entregam o que parecia inviável."*
