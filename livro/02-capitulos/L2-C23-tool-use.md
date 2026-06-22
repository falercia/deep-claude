# CAPÍTULO 23
## TOOL USE

---

> *"O modelo raciocina. A ferramenta age. Quem entende essa divisão de trabalho nunca mais confunde 'Claude respondeu' com 'Claude fez'."*

---

> 🧭 **Por que este capítulo é a aplicação do Invariante 6 — Autonomia Proporcional**
>
> Dar uma ferramenta ao modelo é um ato de delegação. Não de conversação. Quando você expõe uma função — consultar um banco de dados, enviar uma mensagem, criar um arquivo — você está dizendo ao modelo: "use isso para agir no mundo em meu nome." Toda ação tem consequência; toda ferramenta amplia o raio de impacto de um erro. O Invariante 6 diz que autonomia delegada só é ativo quando observabilidade e reversibilidade proporcionais a acompanham. Tool use é onde essa equação se materializa.

---

## 23.1 — O CONCEITO INTUITIVO

Há uma fronteira fundamental que a maioria das pessoas que usa IA nunca torna explícita: a diferença entre um modelo que **responde** e um modelo que **age**.

Quando você pede a Claude "qual a capital da Austrália?", ele responde a partir do que sabe. Nenhum sistema externo é tocado. O modelo consultou a memória treinada e devolveu texto — linguagem em, linguagem fora.

O mundo profissional raramente se contenta com isso. Você quer que o modelo consulte o banco de dados de clientes atual, verifique o preço de um ativo neste minuto, grave um registro, dispare um processo. Para isso, o modelo precisa de **ferramentas** — funções externas que ele pode invocar quando o raciocínio exige ação.

Tool use (ou *function calling*, como o padrão ficou conhecido nas versões iniciais das APIs) é o mecanismo que torna isso possível. A ideia central é simples: você descreve ao modelo quais funções existem e o que cada uma faz. O modelo decide quando chamar cada uma. **Você executa a chamada.** O resultado volta ao modelo, que continua raciocinar. O ciclo se repete até a tarefa estar concluída.

A distinção que o capítulo inteiro reforça: **o modelo pede a chamada. Você decide se executa.** Esse momento — entre o pedido do modelo e a execução da função — é o ponto de governança mais importante de toda a engenharia de agentes.

---

## 23.2 — ANALOGIA: O ESPECIALISTA COM O CATÁLOGO DE SERVIÇOS

Imagine um consultor sênior extremamente qualificado, mas que nunca sai da sala de reuniões. Ele raciocina, analisa, sintetiza, redige. O que não pode fazer sozinho: consultar o ERP da empresa, ligar para um cliente, assinar um documento. Para essas ações, ele usa um catálogo de serviços que a empresa disponibiliza — uma lista de sistemas que ele pode acionar, com instruções de quando usar cada um.

Quando o consultor precisa de um número do financeiro, ele não inventa: requisita o serviço "consultar_saldo_conta". Você — o assistente que coordena o trabalho — recebe a requisição, executa, e devolve o resultado. O consultor processa o número e continua o raciocínio.

O consultor nunca tem acesso direto ao ERP. Ele **pede**, e alguém entre ele e o sistema decide se a requisição faz sentido e a executa. Esse alguém é o seu código — e é nesse ponto que governança acontece.

Essa analogia captura o que tool use é: um sistema de raciocínio que pede ações, e uma camada de execução que decide realizá-las, com você controlando quais ações existem, como são chamadas, e o que retornam.

---

## 23.3 — EXPLICAÇÃO TÉCNICA

### 23.3.1 — O ciclo agentico: como o loop funciona na prática

O ciclo de tool use é um loop, não um disparo único. Entender esse loop é o que separa quem usa tool use de quem usa tool use bem.

![Diagrama 23.1 — O ciclo agentico de tool use](imagens/cap-23-img-01-ciclo-agentico.svg)

A sequência canônica, conforme documentada na API da Anthropic:

1. Você envia a mensagem do usuário ao modelo junto com o array `tools` — a lista de ferramentas disponíveis.
2. Claude avalia a mensagem e decide se precisa de uma ferramenta para responder.
3. Se decidir chamar uma ferramenta, Claude para e devolve `stop_reason: "tool_use"` com um ou mais blocos `tool_use` no conteúdo — cada bloco contém o nome da ferramenta e os parâmetros em JSON.
4. **Seu código** extrai os parâmetros, executa a operação (consulta SQL, chamada de API, escrita em arquivo), e formata o resultado como bloco `tool_result`.
5. Você envia de volta uma nova mensagem de usuário contendo os `tool_result`s.
6. Claude lê os resultados e continua raciocinar. Se precisar de mais ferramentas, retorna ao passo 3. Quando tem tudo que precisa, devolve `stop_reason: "end_turn"` com a resposta final.

O loop termina quando `stop_reason` é qualquer coisa diferente de `"tool_use"` — seja `"end_turn"` (concluiu), `"max_tokens"` (atingiu o limite) ou `"refusal"` (recusou por política).

Esse design tem uma consequência arquitetural importante: **seu código é o executor**. Claude nunca acessa diretamente nenhum sistema — emite uma requisição estruturada. Você intercepta, valida, executa e devolve. A camada de execução está sempre na sua aplicação, nunca no modelo.

*Nota sobre ferramentas de servidor:* A Anthropic oferece ferramentas cujos efeitos colaterais são executados na infraestrutura deles — `web_search`, `web_fetch`, `code_execution`. Para essas, você não gerencia o loop: a execução já aconteceu quando a resposta chega. Os blocos `server_tool_use` mostram o que rodou e o que retornou. Ferramentas que tocam seus sistemas, sua lógica de negócio, seus dados, sempre serão do tipo cliente (você executa). Disponibilidade e preço no [Apêndice J](../04-apendices/L2-APX-J-apendice-vivo.md).

### 23.3.2 — Definindo ferramentas: schema, descrição e parâmetros

Uma ferramenta em Claude é definida por três campos obrigatórios:

| Campo | O que faz | Por que importa |
|-------|-----------|-----------------|
| `name` | Identificador único da ferramenta | O modelo refere-se a ela por esse nome; deve ser descritivo e sem espaços |
| `description` | Texto em linguagem natural explicando o que a ferramenta faz, quando usá-la, e o que retorna | É o principal sinal que Claude usa para decidir se e quando chamar a ferramenta |
| `input_schema` | JSON Schema descrevendo os parâmetros, seus tipos, e quais são obrigatórios | Define o contrato da ferramenta; Claude deve gerar JSON válido contra esse schema |

O campo mais subestimado é `description`. A Anthropic é explícita: descrições são "by far the most important factor in tool performance." Uma descrição vaga produz chamadas erradas ou ausentes. Uma descrição precisa, com exemplos de quando usar e quando não usar, produz roteamento correto e consistente.

Exemplo de schema ilustrativo (não para produção):

```json
{
  "name": "consultar_contrato",
  "description": "Consulta os dados de um contrato de fornecedor pelo seu ID. Use quando precisar de informações sobre vigência, valor, cláusulas de rescisão, ou partes do contrato. Não use para criar ou modificar contratos — apenas para leitura. Retorna um objeto JSON com os campos: id, fornecedor, valor_mensal, data_inicio, data_fim, clausulas.",
  "input_schema": {
    "type": "object",
    "properties": {
      "contrato_id": {
        "type": "string",
        "description": "O identificador único do contrato, no formato CTR-XXXXXX"
      },
      "campos": {
        "type": "array",
        "items": {"type": "string"},
        "description": "Lista opcional de campos a retornar. Se omitido, retorna todos."
      }
    },
    "required": ["contrato_id"]
  }
}
```

Três práticas que a documentação oficial reforça e a experiência confirma:

**Consolide ferramentas relacionadas.** Em vez de `criar_ticket`, `atualizar_ticket`, `fechar_ticket`, considere `gerenciar_ticket` com parâmetro `acao`. Menos ferramentas reduzem a ambiguidade de seleção.

**Use namespacing quando o conjunto crescer.** `github_list_prs`, `slack_send_message`, `crm_consultar_cliente`. O prefixo resolve ambiguidade sem precisar de heurísticas na descrição.

**Retorne apenas o que o modelo precisa.** Respostas que retornam campos irrelevantes inflam o contexto e confundem o raciocínio. Retorne o subconjunto de dados necessário para o próximo passo.

### 23.3.3 — Tool use paralelo: quando Claude chama múltiplas ferramentas de uma vez

Uma capacidade que economiza latência e permanece subutilizada: Claude pode emitir múltiplas chamadas de ferramenta num único turno quando as operações são independentes entre si.

![Diagrama 23.2 — Tool use sequencial vs paralelo](imagens/cap-23-img-02-sequencial-paralelo.svg)

Quando Claude chama `get_weather` para São Paulo e Rio de Janeiro no mesmo turno, a resposta contém dois blocos `tool_use`. Seu código executa ambos — em paralelo real, com `asyncio.gather` ou `Promise.all` — e devolve os dois `tool_result`s **numa única mensagem de usuário**. Esse é o detalhe crítico: resultados paralelos precisam voltar juntos, não em mensagens separadas. Mensagens separadas ensinam o modelo a sequencializar nas próximas chamadas.

Claude 4 em diante tem paralelismo forte por padrão. Para estimulá-lo, a documentação oficial recomenda instrução explícita no system prompt: "Quando múltiplas operações são independentes, invoque todas em paralelo no mesmo turno."

Para desabilitar quando a ordem importa (operação B depende do resultado de A), use `disable_parallel_tool_use: true` no parâmetro `tool_choice`. Na maioria dos casos — análise de dados, consultas independentes, buscas paralelas — o paralelismo é ganho puro de performance.

### 23.3.4 — A fronteira de execução: onde a governança mora

Este é o ponto que justifica o Invariante 6 neste capítulo.

A documentação da Anthropic articula o princípio com precisão: *"The model never executes anything on its own. It emits a structured request, your code (or Anthropic's servers) runs the operation, and the result flows back into the conversation."*

Claude nunca executa nada diretamente. Ele pede. Você faz.

Essa arquitetura cria um ponto de interceptação natural entre o raciocínio do modelo e qualquer efeito no mundo. É onde governança acontece:

- **Validar parâmetros antes de executar.** O `contrato_id` existe? O valor de `acao` está dentro dos permitidos? Validação previne erros que o modelo pode cometer com confiança.

- **Requerer confirmação humana para ações de alto impacto.** Claude pediu `enviar_email` com 500 destinatários? Seu código intercepta, exibe para aprovação, e só executa após confirmação.

- **Implementar dry-run para ferramentas destrutivas.** `deletar_registros` roda primeiro em modo simulado, mostra o que seria deletado, e só executa com flag explícito.

- **Logar cada chamada.** Toda chamada de ferramenta — parâmetros, quem originou, resultado — pode ser registrada antes de qualquer execução. Audit trail nativo.

- **Negar a execução.** Se a chamada viola política, seu código retorna `tool_result` com `is_error: true` e mensagem explicativa. Claude recebe o erro e decide o que fazer — geralmente, tenta outra abordagem ou informa o usuário.

Esse ponto de interceptação não é detalhe de implementação — é o fundamento de toda segurança em sistemas com tool use. Um sistema que executa cegamente todo `tool_use` não tem governança: tem obediência irrestrita. Em sistemas que enviam mensagens, modificam bancos ou deletam arquivos, obediência irrestrita não é eficiência — é risco delegado sem controle.

![Diagrama 23.3 — A fronteira de execução como ponto de governança](imagens/cap-23-img-03-fronteira-governanca.svg)

---

## 23.4 — CRITÉRIO DE DECISÃO

### Quando dar uma ferramenta vs. resolver no prompt

Essa pergunta aparece toda vez que alguém está desenhando um sistema com Claude. A resposta tem três eixos:

**Primeiro eixo: o modelo pode responder sem a ferramenta?**
Se a informação existe no treinamento, está no contexto ou pode ser inferida, uma ferramenta adiciona latência e complexidade sem ganho. Resumir texto, traduzir um parágrafo, redigir um e-mail — nenhuma precisa de ferramenta. A pergunta diagnóstica: *você estaria escrevendo regex para extrair uma decisão da saída do modelo?* Se sim, essa decisão deveria ser uma chamada de ferramenta.

**Segundo eixo: a tarefa tem efeito colateral ou precisa de dado externo?**
Enviar e-mail, gravar registro, consultar preço atual, verificar status de pedido — essas operações exigem ferramenta por natureza. O modelo não pode inventar um preço com credibilidade; precisa da consulta real.

**Terceiro eixo: a saída precisa ter formato garantido?**
Quando você precisa que o modelo produza JSON com campos e tipos definidos, use ferramenta com schema. O schema força o formato — `strict: true` no tool definition garante aderência total. Prosa que "parece JSON" mas pode variar é menos confiável que schema estrito.

### Como desenhar ferramentas seguras

| Princípio | O que significa | Exemplo concreto |
|-----------|-----------------|------------------|
| **Princípio de menor privilégio** | A ferramenta expõe apenas o que a tarefa requer | `consultar_saldo` retorna o saldo de uma conta específica, não acesso ao extrato de todas as contas |
| **Separar leitura de escrita** | Ferramentas que leem e ferramentas que modificam devem ser distintas | `buscar_cliente` (só leitura) separada de `atualizar_cliente` (requer autorização extra) |
| **Parâmetros explícitos, não amplos** | Evite parâmetros como `query: string` que aceitam qualquer coisa | Prefira enumerações explícitas: `status: "ativo" | "inativo" | "suspenso"` |
| **Retorno mínimo necessário** | Não retorne campos que o modelo não precisa para a próxima decisão | Se o modelo precisa saber se o pagamento aprovado, retorne `{aprovado: true}` não o objeto de pagamento completo |
| **Validação antes da execução** | Valide parâmetros no seu código antes de tocar o sistema | Verifique se o ID existe, se o usuário tem permissão, se o valor está no range esperado |
| **Dry-run para destrutivas** | Ferramentas que deletam, enviam, ou modificam dados em massa devem ter modo de simulação | `deletar_registros(dry_run=True)` mostra o que seria deletado sem executar |

### O que nunca expor como ferramenta automática

Há classes de ação que não devem existir como ferramentas executadas automaticamente — sem confirmação humana explícita no fluxo.

| Classe de ação | Por quê não automatizar | Alternativa |
|----------------|------------------------|-------------|
| **Comunicação externa em massa** | E-mail, mensagem, notificação para listas grandes é irreversível | Ferramenta gera rascunho; humano aprova e envia |
| **Operações financeiras** | Débito, transferência, aprovação de pagamento têm impacto irreversível e regulatório | Ferramenta prepara instrução; sistema de aprovação separado executa |
| **Deleção de dados sem backup** | Erro num parâmetro pode apagar dados que não se recuperam | Soft delete + período de retenção; hard delete só com confirmação dupla |
| **Alteração de permissões de acesso** | Mudança de ACL pode abrir brechas de segurança ou bloquear usuários | Ferramenta propõe mudança; admin revisa e aplica |
| **Disparo de webhooks para sistemas de terceiros** | Efeito cascata em sistemas externos fora do seu controle | Ferramentas para sistemas internos; webhooks externos com retry e confirmação |

A heurística prática: se o erro de uma ferramenta exigiria uma ligação para corrigir, ela precisa de confirmação humana antes da execução — não depois.

---

## 23.5 — EXEMPLO MEMORÁVEL: O SISTEMA DE TRIAGEM QUE APRENDEU A PERGUNTAR ANTES DE AGIR

*Cenário ilustrativo brasileiro.* Uma empresa de e-commerce de médio porte em Belo Horizonte construiu, em 2026, um sistema de triagem de reclamações com Claude. Objetivo: reduzir o tempo de resposta a clientes com pedidos atrasados. O modelo receberia a mensagem, consultaria o sistema logístico, e proporia uma resolução.

A primeira versão foi ingênua e custou caro. O sistema expôs quatro ferramentas: `consultar_pedido`, `emitir_reembolso`, `reprocessar_pedido` e `enviar_email_cliente`. Claude usava todas encadeadas — consultava o pedido, verificava o atraso, emitia o reembolso e enviava e-mail confirmando. Rápido, eficiente, e desastroso quando o pedido estava em trânsito normal com rastreamento desatualizado: o modelo reembolsava e pedia desculpas por um atraso que não existia.

A segunda versão aplicou o Invariante 6 com rigor. Três mudanças cirúrgicas.

Primeiro, `emitir_reembolso` e `enviar_email_cliente` foram removidas e substituídas por `propor_reembolso` e `redigir_email_cliente` — ferramentas que **preparam** a ação mas não a executam. O resultado de cada uma era rascunho para revisão humana.

Segundo, `consultar_pedido` foi enriquecida com mais contexto: status logístico detalhado, histórico de rastreamento, última atualização do transportador. Claude passou a distinguir atraso real de atraso de rastreamento.

Terceiro, um nó de aprovação humana foi inserido: o atendente via o rascunho de resolução, ajustava se necessário, e disparava com um clique. A automação absorveu triagem e redação; o humano manteve a decisão final.

Resultado: tempo médio de triagem caiu de 12 para 3 minutos por caso. Taxa de reembolsos indevidos zerou. A satisfação dos atendentes subiu — passaram de triadores a decisores informados.

A lição estrutural é o Invariante 6 inteiro em produção: ferramentas de leitura com autonomia plena, ferramentas de escrita limitadas a rascunho, execução de ações irreversíveis com o humano. Observabilidade total, reversibilidade garantida. Autonomia proporcional ao que o sistema conseguia observar e desfazer.

---

## 23.6 — NA PRÁTICA: TRÊS APLICAÇÕES REPLICÁVEIS

Três aplicações na forma *situação → o que fazer → o ponto de julgamento* — o que separa tool use bem governado de delegação irrestrita.

**Aplicação 1 — Consulta e análise de dados internos com ferramenta de leitura.**
*Situação:* você quer que Claude responda perguntas sobre dados da empresa — clientes, pedidos, contratos — consultando o banco em tempo real, não apenas conhecimento estático. *O que fazer:* exponha ferramentas de leitura com escopo restrito (`buscar_cliente`, `listar_pedidos_por_periodo`, `consultar_contrato`); cada ferramenta retorna apenas os campos necessários, não o objeto inteiro. Instrua no system prompt que ferramentas de escrita não existem nesse contexto — eliminar do catálogo é mais seguro do que proibir por instrução. *O ponto de julgamento:* revise periodicamente os parâmetros passados em produção: o modelo está consultando intervalos razoáveis? Construindo filtros corretos? Um `buscar_pedidos(data_inicio="2020-01-01", data_fim="2026-12-31")` sem filtro de cliente útil indica que a instrução não especificou o escopo esperado da consulta.

**Aplicação 2 — Geração de rascunhos para ações de alto impacto com confirmação humana.**
*Situação:* você quer que Claude prepare comunicações, documentos ou registros que um humano revisa e dispara. *O que fazer:* exponha apenas ferramentas de rascunho (`redigir_email`, `preparar_relatorio`, `propor_atualizacao_cadastro`); o resultado de cada ferramenta é texto estruturado para revisão, não ação executada. Seu código exibe o rascunho ao operador com botão de aprovação — a execução real (enviar e-mail, gravar no banco, chamar API externa) fica no handler de aprovação, fora do ciclo de tool use. *O ponto de julgamento:* o operador não deve apenas "clicar em aprovar" — deve ler o conteúdo. Monitore o tempo médio entre geração e aprovação: abaixo de cinco segundos consistentemente significa que a revisão virou formalidade, e você voltou à obediência irrestrita com uma camada de UI por cima.

**Aplicação 3 — Agente com limite de turnos e dry-run para operações destrutivas.**
*Situação:* você tem um agente com loop agentico que chama múltiplas ferramentas em sequência (atualizar registros, processar lote, executar ações em sistema externo). *O que fazer:* implemente `max_turns` explícito no loop — se o agente não convergiu em N turnos, para e reporta o estado para revisão humana. Para ferramentas destrutivas ou irreversíveis, implemente `dry_run=True` que retorna o que *seria* feito sem executar; o agente roda em dry-run primeiro, e seu código exibe o sumário ao operador antes de permitir a execução real. *O ponto de julgamento:* o sumário de dry-run precisa ser legível por um humano não-técnico em menos de dois minutos. Se não for, o escopo está grande demais para aprovação informada — divida em etapas menores.

> 🔧 **EXERCÍCIO**
> Escolha uma tarefa repetitiva do seu fluxo de trabalho que hoje exige que você consulte pelo menos dois sistemas diferentes antes de tomar uma decisão. Escreva a definição de duas ferramentas de leitura que dariam ao Claude o acesso necessário — com `name`, `description` e `input_schema`. Depois, escreva a regra que seu código aplicaria como ponto de interceptação antes de executar cada chamada de ferramenta. Se a segunda parte for mais difícil que a primeira, você encontrou o lugar certo para construir governança.

---

## 23.7 — CAMADA VIVA: O QUE MUDA, O QUE FICA

Tool use é um dos padrões mais estáveis da engenharia de IA. O ciclo — modelo raciocina, ferramenta age, resultado volta, modelo continua — não é característica de uma versão específica de Claude. É o padrão arquitetural que surgiu com o advento dos LLMs como coordenadores de sistemas e vai perdurar enquanto modelos de linguagem precisarem interagir com o mundo externo.

O que é **durável**:
- O contrato "modelo pede, você executa"
- O schema JSON como interface entre linguagem natural e sistemas tipados
- A fronteira de execução como ponto de governança
- O ciclo agentico (`while stop_reason == "tool_use"`)
- O princípio de menor privilégio na definição de ferramentas

O que está **no Apêndice J** (volátil):
- Ferramentas de servidor disponíveis e preços por uso
- Limites de tokens nos schemas de ferramentas por modelo
- Número máximo de ferramentas por request por versão de API
- Modelos recomendados para tool use complexo (muda com cada geração)
- Benchmarks de performance de tool use por modelo

Veja [Apêndice J — Apêndice Vivo](../04-apendices/L2-APX-J-apendice-vivo.md) para a foto atual.

---

## 23.8 — LIMITAÇÕES E CUIDADOS

**A qualidade da ferramenta é teto da qualidade do agente.** Um modelo excelente com ferramentas mal descritas produz chamadas erradas com confiança. Invista na `description` tanto quanto no schema — frequentemente mais.

**O modelo erra parâmetros, especialmente em casos de borda.** Claude pode passar ID em formato incorreto, omitir campo obrigatório ou interpretar mal um enumerador. Validação antes da execução é defesa obrigatória, não opcional.

**Ferramentas com retorno verboso inflam o contexto.** Cada ciclo do loop acumula: a chamada, os parâmetros, o resultado. Ferramentas que retornam objetos grandes (um contrato inteiro quando o modelo precisava só do valor da multa) encarecem o ciclo e degradam a atenção em conversas longas. Projete retornos enxutos.

**Loops podem não convergir.** Em casos raros, o modelo entra em ciclo que nunca resolve — chama ferramenta A, o resultado leva a B, que leva de volta a A. Implemente limite de turnos (`max_turns` no Claude Code SDK, ou contador manual no loop próprio) e tratamento de loop.

**Ferramentas de servidor têm pricing adicional.** `web_search`, `code_execution` e similares cobram por uso além dos tokens. Volume alto pode surpreender o orçamento. Ver Apêndice J para números atuais.

**Tool use e extended thinking têm restrições de compatibilidade.** Quando extended thinking está ativo, `tool_choice: "any"` e `tool_choice: "tool"` retornam erro — apenas `"auto"` e `"none"` são compatíveis. Verifique antes de combinar.

---

## 23.9 — CONEXÕES COM OUTROS CAPÍTULOS

- 🔗 **Invariante que rege este capítulo** → [Framework 3 — Autonomia Proporcional](../../Livro-1-Os-Invariantes/03-frameworks/L1-F3-agente-prop.md)
- 🔗 **Cowork: tool use em produtos para não-técnicos** → [Capítulo 8 — Claude Cowork](L2-C08-cowork.md)
- 🔗 **Claude Code: tool use no terminal** → [Capítulo 9 — Claude Code](L2-C09-claude-code.md)
- 🔗 **Skills: ferramenta como ativo organizacional** → [Capítulo 31 — Claude Skills](L2-C31-skills.md)
- 🔗 **Subagents: orquestrar múltiplos agentes com ferramentas** → [Capítulo 32 — Subagents e Workflows](L2-C32-subagents-workflows.md)
- 🔗 **MCP: o protocolo que padroniza ferramentas em escala** → [Capítulo 29 — Claude + MCP](L2-C29-claude-mcp.md)
- 🔗 **Números voláteis (pricing de ferramentas de servidor, limites por modelo)** → [Apêndice J — Apêndice Vivo](../04-apendices/L2-APX-J-apendice-vivo.md)

### Tool use e MCP: a conexão estrutural

Tool use e MCP (Model Context Protocol) não são alternativas — são camadas distintas do mesmo ecossistema. Tool use é o mecanismo primitivo da API: você define ferramentas no JSON, Claude chama, você executa. MCP padroniza como ferramentas são descobertas, descritas e acessadas em escala.

Quando você conecta um servidor MCP ao Claude, cada `Tool` que ele expõe vira automaticamente uma ferramenta disponível — com schema, descrição e semântica definidos pelo servidor. Em vez de definir manualmente cada ferramenta no array `tools`, o servidor anuncia o catálogo, e o cliente (Claude, Cowork, Claude Code) o consome.

Para arquiteturas corporativas com dezenas de ferramentas e múltiplos sistemas internos, o MCP é o passo natural após dominar tool use primitivo. O Capítulo 29 detalha como construir e governar essa camada em escala.

---

## 23.10 — RESUMO EXECUTIVO

| Conceito | Síntese |
|----------|---------|
| **O que é tool use** | Mecanismo que permite ao modelo invocar funções externas; modelo raciocina, você executa, resultado volta |
| **O ciclo agentico** | `while stop_reason == "tool_use"`: Claude pede → você executa → `tool_result` de volta → Claude continua |
| **A ferramenta é um schema** | Três campos: `name`, `description` (mais importante), `input_schema` (JSON Schema) |
| **Tool use paralelo** | Claude pode emitir múltiplas chamadas num único turno; resultados devem voltar em uma única mensagem |
| **A fronteira de execução** | Claude pede; você decide se executa — ponto de governança onde validação, autorização e logging acontecem |
| **Quando usar ferramenta** | Dado externo ou atual, efeito colateral necessário, formato de saída garantido obrigatório |
| **Quando não usar** | Modelo responde do treinamento, tarefa é puramente de raciocínio ou escrita, latência adicional não vale |
| **Ferramentas seguras** | Menor privilégio, leitura separada de escrita, parâmetros explícitos, validação antes da execução |
| **O que nunca automatizar** | Comunicação em massa, operações financeiras, deleção sem backup — sempre confirmação humana antes |
| **MCP como evolução** | Protocolo que padroniza descoberta e execução de ferramentas em escala; detalhe no Cap 28 |
| **Invariante regente** | 6 — Autonomia Proporcional: ferramenta amplia ação; governança deve acompanhar o alcance |

---

## 23.11 — VALIDAÇÃO UAU

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | **Clareza** — Explicar em 60 segundos a diferença entre "Claude respondeu" e "Claude chamou uma ferramenta", e por que isso importa para governança | ☐ |
| 2 | **Técnica** — Descrever o ciclo agentico completo (os 6 passos), incluindo o que acontece com múltiplas ferramentas paralelas | ☐ |
| 3 | **Schema** — Escrever uma definição de ferramenta com `name`, `description`, e `input_schema` que um desenvolvedor poderia usar sem perguntas | ☐ |
| 4 | **Decisão** — Dado um conjunto de 5 ações, classificar cada uma: ferramenta automática, ferramenta com confirmação, ou não-ferramenta | ☐ |
| 5 | **Governança** — Identificar os três pontos de controle que seu código pode implementar entre o `tool_use` do modelo e a execução real | ☐ |

🔗 **Próximo capítulo:** [Capítulo 29 — Claude + MCP](L2-C29-claude-mcp.md) *(Tool use padronizado em escala corporativa)*

---

> *"A ferramenta amplifica o raio de ação. A fronteira de execução amplifica o raio de controle. Quem constrói sistemas com tool use sem construir a fronteira ao mesmo tempo não tem alavancagem — tem exposição."*
