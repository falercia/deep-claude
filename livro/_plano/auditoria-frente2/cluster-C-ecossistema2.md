# AUDITORIA — CLUSTER C: ECOSSISTEMA 2
## Capítulos C14 a C18 | Banca Editorial Adversarial
**Data:** 2026-06-17

---

## [C14 — Claude Artifacts]
Nota: 6/10 · Veredito: Manual de função bem escrito, mas sem tensão crítica · "Manual de botão"? MÉDIO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ⚠️
   - Seção 14.0 (box 🧭) identifica Inv. 9 — Operador, mas a justificativa é rasa: "é o operador entregando ao mundo aquilo que validou." Nenhuma seção do capítulo desenvolve essa tensão. Onde está o dilema de *o que* merece sair do chat e virar artefato público? A conexão ao Invariante é declarativa, não desenvolvida.

2. **Conceito intuitivo + analogia** ✅
   - Seção 14.1 clara. Analogia da prancheta do arquiteto em 14.2 funciona bem e é memorável. Passa no Teste da Joana.

3. **Quando usar / quando EVITAR** ⚠️
   - Seção 14.4 lista cinco gatilhos de USO de forma competente. A seção 14.5 lista limitações (complexidade, dependências, storage, exportação). Mas falta o critério de *quando artifacts são a escolha ERRADA* como pergunta de decisão explícita. A virada entre "melhor em artifact" e "melhor deixar em chat" é tratada como regra de ouro rápida ao final do 14.4, sem desenvolver os casos-limite reais. Ex.: quando o artefato vira sobreengenharia para um texto de 200 palavras que nunca será reutilizado.

4. **Profundidade técnica real** ⚠️
   - Seção 14.3.1 lista os seis tipos com exemplos práticos — aceitável. Porém: (a) não há menção ao modelo que roda React artifacts (limitação de qual Claude?), (b) a lista de imports suportados em React é citada mas não exemplificada — usuário continua sem saber o que pode e o que não pode, (c) versionamento (14.3.3) é tratado com leveza; não explica o mecanismo real (é por sessão? persiste em Projects?). Profundidade parece de documentação de produto, não de livro de método.

5. **Exemplo memorável brasileiro, rotulado** ✅
   - Seção 14.4: empreendedora, 5 dias, R$ 200 vs R$ 15-30k. Concreto, calibrado, brasileiro. Bem rotulado com lição estrutural ao final.

6. **Camada Viva** ❌
   - Seção 14.3.1 lista tipos de artifacts em 2026 com declarações perecíveis embutidas no corpo principal: "Artifacts cobrem em 2026 seis tipos principais". Os detalhes de imports suportados em React, bibliotecas funcionais (Recharts, Lucide, Tailwind), ausência de localStorage — tudo isso é altamente perecível e está no corpo do capítulo, não em Apêndice Vivo. Em 6 meses, esse inventário pode ser parcialmente errado. Risco real de "manual de botão" envelhecido.

7. **Exercícios + autoavaliação + conexões** ✅
   - Exercícios 14.10 práticos e operacionalizáveis. Projeto do capítulo 14.11 desafiante. Checklist 14.8 e Validação UAU 14.13 funcionam. Conexões 14.6 com links relevantes.

### 5 testes

- **Joana:** PASSA — qualquer profissional não técnico entende a prancheta.
- **Durabilidade:** FALHA — inventário de tipos, bibliotecas suportadas e comportamentos de sandbox são perecíveis no corpo.
- **Diferenciação:** PARCIAL — explica bem *o que* é, mas não *por que* Artifacts vs Google Docs/Figma/Notion como escolha de workflow.
- **Memorização:** PASSA — caso da empreendedora (R$ 200 vs R$ 30k, 5 dias) é aderente.
- **Transformação:** PARCIAL — exercícios são bons, mas a tensão decisória (quando usar / quando é sobreengenharia) não está presente.

### Top lacunas (priorizadas, com seção)

1. **Camada Viva ausente** (seções 14.3.1 e 14.3.2): toda a especificidade técnica de tipos, imports, localStorage, bibliotecas deve migrar para Apêndice Vivo com data de validade. O corpo deveria preservar apenas o método de raciocínio sobre artifacts.
2. **Quando EVITAR sem critério real** (seção 14.4): "se vai ficar no chat, deixa em resposta normal" não é critério operacional. Falta a análise de custo-benefício explícita: quando o overhead de artifact é maior que o ganho.
3. **Invariante 9 não desenvolvido** (seção 14.0 e corpo): qual é a *responsabilidade do operador* ao exportar um artifact? Quem valida o que sai do painel para o mundo? Essa tensão existe e o capítulo a ignora completamente.
4. **Profundidade técnica de versionamento** (seção 14.3.3): o mecanismo de versões dentro de Projects vs sessões avulsas não está explicado — omissão que cria expectativa errada.

### Maior força a preservar
Exemplo da empreendedora (14.4): lição estrutural clara, números brasileiros críveis, progressão narrativa de 5 dias bem construída. É o tipo de caso que vira referência em treinamentos corporativos.

---

## [C15 — Claude Research]
Nota: 7/10 · Veredito: O melhor capítulo do cluster — mas o Invariante 1 (Plausibilidade) ainda não recebe tratamento adversarial suficiente · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅
   - Box 🧭 identifica Inv. 1 — Plausibilidade com justificativa real: "Research entrega pesquisa, não verdade." Seção 15.4 (Validação e Limites) desenvolve a tensão de forma honesta: fontes não confiáveis, alucinação ainda possível, viés de cobertura web. É o capítulo que mais honra o Invariante de ancoragem.

2. **Conceito intuitivo + analogia** ✅
   - Seção 15.1 clara. Analogia do chefe de pesquisa com equipe (15.2) é forte e operacional. Passa no Teste da Joana.

3. **Quando usar / quando EVITAR** ✅
   - Seção 15.3.3 é a melhor desta dimensão em todo o cluster: três modos com critério explícito (Research / Web Search / Chat normal), com regra prática em termos de tempo ("mais de meia hora manualmente → Research"). Modelo de decisão claro.

4. **Profundidade técnica real** ✅
   - Seção 15.3.1 explica orquestrador + subagentes paralelos + agregação + síntese com fidelidade suficiente. Seção 15.3.2.1 (anatomia de prompt) e 15.3.2.2 (prompt completo) são excepcionais — nível de detalhe que transforma uso imediato. Padrões avançados em 15.3.2.3 (Research em camadas, adversarial, comparativo, de validação) elevam o capítulo acima do manual.

5. **Exemplo memorável brasileiro, rotulado** ✅
   - Seção 15.5: diretora de logística, 22 minutos vs 6-10 horas, 153 fontes, 95% de acerto na validação. Concreto, verificável, lição estrutural explícita ao final.

6. **Camada Viva** ⚠️
   - Seção 15.3.1 declara "em 2026, esse processo consome entre cinco e trinta minutos" e "custos equivalente a dez ou vinte conversas" — números perecíveis no corpo. Seção 15.3.2 cita que ativação "varia ligeiramente conforme o plano e a interface" sem nomear o mecanismo estável. Melhor que C14, mas ainda há especificidades operacionais que deveriam estar em Apêndice Vivo.

7. **Exercícios + autoavaliação + conexões** ✅
   - Exercício 4 (validação rigorosa com documentação de taxa de acerto) é notável — é o único exercício do cluster que força o leitor a confrontar os limites da ferramenta. Projeto do capítulo (incorporar Research por um mês com registro de ROI) é excelente.

### 5 testes

- **Joana:** PASSA — analogia do chefe de pesquisa é forte.
- **Durabilidade:** PASSA COM RESSALVA — o método de Research em camadas / adversarial / comparativo vai durar; os tempos e custos exatos não.
- **Diferenciação:** PASSA — explica com precisão a distinção entre Research, Web Search e Chat, com critério temporal operacional.
- **Memorização:** PASSA — "22 minutos vs 6-10 horas, 153 fontes" fica.
- **Transformação:** PASSA — prompt completo de 15.3.2.2 é imediatamente utilizável; exercício de validação rigorosa muda comportamento.

### Top lacunas (priorizadas, com seção)

1. **Invariante 1 não levado ao limite** (seção 15.4): a seção existe e é honesta, mas falta o caso em que Research *ativa e deliberadamente* gera falsa confiança — ou seja, quando o relatório bem formatado com 150 fontes leva o usuário a *não* validar porque parece mais credível do que deveria. Esse é o risco real do Invariante 1 aplicado a Research, e o capítulo roça mas não enfrenta.
2. **Camada Viva** (seções 15.3.1 e 15.3.2): tempos, custos e mecânica de ativação por plano deveriam ser Apêndice Vivo.
3. **Research em organizações** (ausente): o capítulo é individual. Qual o protocolo quando múltiplos profissionais de uma equipe usam Research? Há risco de echo chamber por todos usarem o mesmo sistema?

### Maior força a preservar
Seção 15.3.2.1 + 15.3.2.2 (anatomia do prompt + exemplo completo): é a melhor seção técnica do cluster inteiro. O nível de detalhe sobre os 6 componentes do prompt transforma imediatamente a qualidade do uso.

---

## [C16 — Claude Web Search]
Nota: 7/10 · Veredito: O capítulo mais alinhado ao Invariante que ancora — Plausibilidade recebe tratamento real · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅
   - Box 🧭 declara Inv. 1 — Plausibilidade com formulação precisa: "Web Search é o antídoto parcial à Plausibilidade: quando o modelo não sabe, pergunta a uma fonte fora dele. Não elimina alucinação; restringe a superfície em que ela atua." É a formulação mais honesta dos dois capítulos que instanciam Inv. 1.

2. **Conceito intuitivo + analogia** ✅
   - Seção 16.1 clara. Analogia do assistente com acesso ao jornal (16.2) é funcional e precisa. Passa no Teste da Joana.

3. **Quando usar / quando EVITAR** ✅
   - Seções 16.3.3 (quando rende) e 16.3.4 (quando não usar) são explícitas e operacionais. Cada classe de pergunta tem justificativa. "Análise sobre conteúdo já no contexto" como caso de não-uso é insight não óbvio — bem incluído.

4. **Profundidade técnica real** ✅
   - Seção 16.3.1 explica mecânica de busca com fidelidade: query otimizada diferente da pergunta original, seleção de 3-10 fontes, leitura + extração + citações inline. Seção 16.4 (hierarquia de 5 tiers de confiabilidade) é a adição técnica mais valiosa do capítulo e diferencia este livro de tutoriais genéricos.

5. **Exemplo memorável brasileiro, rotulado** ✅
   - Seção 16.5: diretor de saúde, fevereiro 2026, blog sem autoria como "consultoria especializada", 40% de diferença no número. Lição estrutural dura e necessária. O exemplo incomum (Web Search falha) é mais útil do que os de sucesso dos outros capítulos.

6. **Camada Viva** ⚠️
   - Seção 16.3.1 menciona "três a dez páginas" e "30 segundos a um minuto" — perecíveis. Seção 16.3.2 cita "botão na barra de ferramentas" — detalhe de interface que pode mudar. Melhor que C14, ainda presente.

7. **Exercícios + autoavaliação + conexões** ✅
   - Exercício 4 (auditar últimas cinco respostas de Web Search para verificar o que foi citado sem validar) é o exercício de maior impacto real do cluster — força confronto com comportamento já existente do leitor.

### 5 testes

- **Joana:** PASSA.
- **Durabilidade:** PASSA COM RESSALVA — a hierarquia de 5 tiers é o elemento mais durável e mais valioso; detalhes de interface são perecíveis.
- **Diferenciação:** PASSA — a distinção Web Search / Research / Chat está clara e referenciada para o capítulo anterior.
- **Memorização:** PASSA — "O número não era de uma consultoria; não existia" fica. É o anti-exemplo mais potente do cluster.
- **Transformação:** PASSA — política pessoal de validação (16.11) é exercício que muda comportamento permanentemente.

### Top lacunas (priorizadas, com seção)

1. **Camada Viva** (seções 16.3.1 e 16.3.2): contagem de páginas consultadas, tempos e detalhes de interface deveriam estar em Apêndice Vivo.
2. **Plausibilidade não levada ao extremo** (seção 16.4): a hierarquia de tiers é excelente, mas falta o caso de Tier 3 que *parece* Tier 1 — como detectar blog corporativo disfarçado de fonte oficial? O leitor precisa de heurísticas de detecção além da classificação passiva.
3. **Integração com Research ausente** (ausente): quando começar com Web Search e escalar para Research? Falta protocolo de transição entre os dois modos — ponto que C15 também não cobre do lado de cá.

### Maior força a preservar
Seção 16.4 (hierarquia de 5 tiers de confiabilidade): é o conceito mais original e mais durável do capítulo. Nenhuma documentação oficial de Claude ensina isso. É contribuição editorial real do livro.

---

## [C17 — Claude Voice]
Nota: 5/10 · Veredito: Capítulo honesto sobre modalidade, mas raso em profundidade técnica e fraco na âncora ao Invariante · "Manual de botão"? MÉDIO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ❌
   - Box 🧭 identifica Inv. 9 — Operador com justificativa: "Voice muda o canal, não o contrato." Mas nenhuma seção do capítulo desenvolve o que isso significa em prática. Qual é a responsabilidade do operador ao usar voz? Validar o que foi dito antes de agir? Verificar que a transcrição capturou a intenção? O capítulo ignora completamente a dimensão de operador aplicada a voz. A âncora parece escolhida por descarte ("não era os outros invariantes") em vez de escolha genuína.

2. **Conceito intuitivo + analogia** ✅
   - Seção 17.1 distingue bem voz-como-modalidade-cognitiva de voz-como-ditado-acelerado. Analogia das duas formas de chegar a uma ideia (17.2) funciona. Passa no Teste da Joana.

3. **Quando usar / quando EVITAR** ✅
   - Seção 17.3.2 separa com precisão: "voz brilha" vs "voz é desperdício". Quatro classes de brilho e quatro de desperdício. Inclui casos não óbvios (privacidade, conteúdo técnico com nomes próprios). Bom.

4. **Profundidade técnica real** ❌
   - Seção 17.3.1 é superficial: descreve onde voz está disponível e a mecânica básica em 3 parágrafos. Não há: (a) explicação de como funciona o sistema de voz (STT + modelo + TTS vs end-to-end?), (b) como o contexto de conversa se mantém em voz (diferente do texto?), (c) como integrar transcrições de voz em Projects, (d) tratamento de interrupções e mudanças de assunto. O capítulo tem profundidade de tutorial de onboarding, não de livro de método.

5. **Exemplo memorável brasileiro, rotulado** ✅
   - Seção 17.4: mestranda em administração, dissertação travada, 40 minutos de caminhada, tese articulada. A passagem "ela disse algo que ela mesma não tinha pensado antes daquela frase sair" é o momento mais potente do caso. Brasileiro, específico, com lição estrutural clara.

6. **Camada Viva** ⚠️
   - Seção 17.3.1: "latência fim a fim fica em torno de 1 a 2 segundos" e "fluente em português brasileiro" são afirmações que envelhecem. Seção 17.3.1 cita interface mobile como "mais polida" — detalhe de estado atual, não método. Moderado mas presente.

7. **Exercícios + autoavaliação + conexões** ❌
   - Capítulo não tem seções de exercícios práticos (equivalentes a 14.10, 15.11, 16.10), sem projeto do capítulo, sem checklist. A Validação UAU (17.7) existe mas encerra o capítulo abruptamente. É o capítulo mais curto do cluster e o único sem exercícios estruturados. Lacuna grave para um livro que promete transformação de comportamento.

### 5 testes

- **Joana:** PASSA — distinção voz-como-cognição vs voz-como-ditado é acessível.
- **Durabilidade:** PARCIAL — os 4 padrões profissionais (brainstorm pré-evento, reflexão pós-evento, ditado, aprendizado) são duráveis; latência e qualidade PT-BR são perecíveis.
- **Diferenciação:** PARCIAL — o que diferencia este capítulo de um blog post de "dicas para usar voz com IA" é tênue.
- **Memorização:** PASSA — caso da mestranda e a frase sobre pensamento que emerge ao falar ficam.
- **Transformação:** FALHA — sem exercícios, sem projeto, sem checklist. Não há mecanismo de mudança de comportamento estruturado.

### Top lacunas (priorizadas, com seção)

1. **Ausência total de exercícios e projeto do capítulo** (faltam seções equivalentes a X.10 e X.11): é a lacuna mais grave e mais fácil de corrigir. Pelo menos três exercícios específicos e um projeto de uma semana de adoção são necessários para paridade com o restante do livro.
2. **Profundidade técnica** (seção 17.3.1): o capítulo precisa explicar como voz se integra com Projects (para que os insights não se percam), o que acontece quando você interrompe (Claude processa a interrupção?), e como lidar com transcrições imprecisas em conteúdo técnico.
3. **Invariante 9 não desenvolvido** (ausente): qual é o papel do operador ao usar voz? Validar transcrições antes de agir? O capítulo nunca responde. É a âncora mais fraca do cluster.
4. **Dica do gancho contextual subdesenvolvida** (seção 17.3.4): a técnica de sinalizar destino no início/fim de sessão é boa mas ocupa apenas um parágrafo. Merece desenvolvimento com exemplos concretos.

### Maior força a preservar
Distinção conceitual entre voz-como-modalidade-cognitiva vs voz-como-ditado (seções 17.1 e 17.2): é o insight de maior valor do capítulo e não aparece em documentações oficiais. A lição da mestranda (17.4) concretiza esse insight de forma memorável.

---

## [C18 — Claude Scheduled Tasks]
Nota: 7/10 · Veredito: Capítulo sólido com ancoragem ao Invariante mais desenvolvida do cluster — mas Camada Viva e ausência de checklist são problemas · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅
   - Box 🧭 identifica Inv. 6 — Autonomia Proporcional com justificativa genuína: "Sem observabilidade e sem rollback, essa autonomia é passivo, não ativo." É a âncora mais bem desenvolvida do cluster. A seção 18.5 (Limitações) retoma a tensão com "trabalho que exige julgamento contextual em tempo real" e "falhas silenciosas" — o Invariante é honrado, não apenas declarado.

2. **Conceito intuitivo + analogia** ✅
   - Seção 18.1 clara. Analogia da assistente que trabalha à noite (18.2) é eficaz e acessível. Passa no Teste da Joana.

3. **Quando usar / quando EVITAR** ✅
   - Seção 18.5 (Limitações) e final do 18.3.2 cobrem explicitamente os casos de não-uso: julgamento contextual em tempo real, interação contínua, falhas silenciosas. A seção 18.3.2 (como definir uma boa tarefa) funciona como critério de qualidade — o segundo ponto sobre "periodicidade compatível com utilidade" é especialmente bom.

4. **Profundidade técnica real** ⚠️
   - Seção 18.3.1 descreve os componentes de forma clara (schedule + prompt + tools + entrega + registro). Seção 18.3.3 com seis padrões é útil. Porém: (a) não explica como definir tasks na interface (onde exatamente? Claude Desktop apenas? claude.ai?), (b) o mecanismo de "registro de execução" com histórico é citado mas não detalhado — como acessar? como revisar falhas?, (c) integração com MCP específico não tem exemplo concreto de configuração. Novamente: detalhe de interface poderia ir para Apêndice Vivo, mas o método de raciocínio sobre tasks poderia ir mais fundo.

5. **Exemplo memorável brasileiro, rotulado** ✅
   - Seção 18.4: diretora de marketing, 12 pessoas, 6 tasks configuradas, 8 horas semanais recuperadas. É o exemplo mais completo do cluster — detalha horários, cadências, canais de entrega. Lição estrutural sobre redistribuição de atenção qualificada é precisa e não óbvia.

6. **Camada Viva** ⚠️
   - Seção 18.3.3 cita que a diretora configurou tasks "toda manhã às 6h45", "a cada quatro horas durante o dia útil" — são exemplos, não afirmações perecíveis, o que é bom. Mas a seção 18.3.2 menciona "MCPs configurados no Claude Desktop" como se fosse o único vetor de acesso — isso é estado atual, pode mudar. Moderado.

7. **Exercícios + autoavaliação + conexões** ⚠️
   - Não há seção de exercícios estruturados (ausente como C17). A Validação UAU (18.8) existe e inclui "configurar três tasks na sua rotina pessoal nesta semana" — mas isso seria exercício, não autoavaliação. A ausência de uma seção dedicada de exercícios e projeto do capítulo é inconsistência com os outros capítulos do cluster (C14, C15, C16 têm exercícios detalhados). Conexões (18.6) são boas e relevantes.

### 5 testes

- **Joana:** PASSA — assistente que trabalha à noite é forte.
- **Durabilidade:** PASSA — os seis padrões profissionais e o framework de design de tasks (objetivo, periodicidade, canal, escopo, revisão) são duráveis. Detalhes de interface são os únicos riscos.
- **Diferenciação:** PASSA — "autonomia delegada no tempo" com "sem observabilidade = passivo, não ativo" é formulação que não aparece em tutoriais genéricos.
- **Memorização:** PASSA — "8 horas semanais recuperadas", "Claude trabalha enquanto você dorme" ficam.
- **Transformação:** PARCIAL — a lista de boas práticas de 18.3.2 é operacional, mas sem exercícios estruturados o capítulo não fecha o loop de mudança de comportamento.

### Top lacunas (priorizadas, com seção)

1. **Ausência de exercícios e projeto do capítulo** (ausentes): paridade com C14-C16 exige pelo menos 3 exercícios práticos e um projeto de "uma semana configurando e refinando três tasks reais".
2. **Mecanismo de observabilidade não desenvolvido** (seção 18.3.1): o "registro de execução" é citado mas não explicado. Dado que Autonomia Proporcional é o Invariante de ancoragem, a seção de *como monitorar e reverter* deveria ser a mais desenvolvida do capítulo — é a mais curta.
3. **Interface de configuração ausente** (ausente): onde se configura uma task (Desktop apenas? claude.ai?), como se cria, como se edita, como se desativa — esses detalhes não aparecem. Poderiam ir para Apêndice Vivo, mas precisam existir em algum lugar.
4. **Drift de utilidade subdesenvolvido** (seção 18.5): a limitação de "task que virou ruído" é citada em uma linha. Merece um mini-framework de revisão periódica — por ser a consequência mais comum em uso real.

### Maior força a preservar
Formulação do Invariante 6 no contexto de tasks (seção 18.0 + 18.5): "sem observabilidade e sem rollback, essa autonomia é passivo, não ativo" é a articulação mais precisa e mais durável do cluster. O exemplo da diretora de marketing (18.4) com os 6 patterns concretos é o guia de implementação mais completo do cluster.

---

## LINHAS-TRACKER

```
CODIGO|NOTA|MANUAL_BOTAO|LACUNA_PRINCIPAL
C14-ARTIFACTS|6|MEDIO|Camada Viva no corpo (inventário de tipos/imports perecível); Invariante 9 não desenvolvido
C15-RESEARCH|7|BAIXO|Risco de falsa confiança por relatório bem formatado não tratado; tempos/custos perecíveis no corpo
C16-WEB-SEARCH|7|BAIXO|Detecção de Tier 3 disfarçado de Tier 1 ausente; protocolo de transição Web Search→Research faltando
C17-VOICE|5|MEDIO|Sem exercícios nem projeto do capítulo; profundidade técnica de onboarding; Invariante 9 sem desenvolvimento
C18-SCHEDULED-TASKS|7|BAIXO|Sem exercícios nem projeto; mecanismo de observabilidade/rollback subdesenvolvido apesar de ser o Invariante central
```

---

## SÍNTESE FINAL DO CLUSTER C (10-14 linhas)

**Notas:** C14 = 6, C15 = 7, C16 = 7, C17 = 5, C18 = 7. Média: 6,4/10.

**Padrão comum positivo:** todos os cinco capítulos têm exemplos brasileiros específicos, concretos e com lição estrutural explícita — é a maior força do cluster e deve ser preservada. A distinção entre modos (Research vs Web Search vs Chat) é tratada com rigor em C15 e C16.

**Padrão comum negativo número 1 — Camada Viva:** em todos os capítulos, informações altamente perecíveis (contagens de fontes, latências, listas de imports, cadências em minutos, detalhes de interface) estão embutidas no corpo do capítulo. Isso é risco sistêmico: em 12 meses, o leitor encontrará afirmações factuais incorretas no meio do método. A migração para Apêndice Vivo com data de validade é corretivo obrigatório em C14, C15, C16, C17 e C18.

**Padrão comum negativo número 2 — Invariantes declarados, não desenvolvidos:** em C14 (Inv. 9), C17 (Inv. 9) e parcialmente C18 (Inv. 6), o box de ancoragem existe mas o corpo do capítulo nunca retorna à tensão anunciada. A âncora vira decoração. Somente C15, C16 e C18 realmente honram o Invariante ao longo do texto.

**Padrão comum negativo número 3 — Manual de botão residual:** C14 e C17 têm risco MÉDIO. C14 porque a maior parte do valor técnico é inventário de features. C17 porque sem exercícios estruturados o capítulo não diferencia um livro de método de um blog post.

**O mais fraco é C17 (Voice, nota 5):** é o único capítulo sem exercícios práticos, sem projeto do capítulo e sem checklist — inconsistência grave com os demais do cluster. A profundidade técnica está no nível de onboarding, e o Invariante de ancoragem (Inv. 9 — Operador) nunca é desenvolvido concretamente. O capítulo tem boa intuição (voz como modalidade cognitiva distinta) mas não a executa em método.
