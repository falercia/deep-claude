# AUDITORIA ADVERSARIAL — CLUSTER B: ECOSSISTEMA 1
**Capítulos:** C09 Claude Code · C10 Claude Web · C11 Desktop · C12 Mobile · C13 Projects
**Data:** 2026-06-17 · Auditor: Banca Editorial Adversarial
**Régua:** PROGRAMA-CONTEUDO-L2.md §2 (7 elementos) + 5 testes

---

## C09 — Claude Code

**Nota: 7/10 · Veredito: Sólido mas incompleto · "Manual de botão"? BAIXO**

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅
   - Inv. 6 (Autonomia Proporcional) declarado com justificativa funcional real: "agente executa, humano rastreia / os níveis plan-edit-run operacionalizam F3-AGENTE-PROP". Inv. 9 como secundário citado. A justificativa é de 3 linhas, suficiente — não é decorativa.

2. **Conceito intuitivo + analogia memorável (Teste da Joana)** ✅
   - Seção 9.2: "O estagiário que entrega o ticket completo" vs. "estagiário que sugere linha". A distinção é precisa e memorável. Passes o Teste da Joana: um executivo sem background técnico entende o paradigma shift. Força preservar.

3. **Quando usar / quando EVITAR** ⚠️
   - Seção 9.3.3 descreve bem quando Cursor ou Copilot são melhores escolhas. Seção 9.6 lista limitações. Mas falta um critério explícito de decisão tipo "use Claude Code quando X, use Cursor quando Y, use nenhum quando Z". O leitor tem peças mas não tem a regra sintetizada. Falta uma tabela ou parágrafo-síntese de decisão — especialmente para **quando não delegar autonomia ao Code** (ex: codebase sem testes, sistema legacy frágil, produção sem staging).

4. **Profundidade técnica real** ✅
   - Seção 9.3.1 lista todas as tools com descrição funcional real (não só nomes). Modo Plan, CLAUDE.md, subagents — tudo explicado com mecânica. Seção 9.6 tem 5 limitações honestas, incluindo acesso a sistemas sensíveis e custo de tokens. Profundidade acima da média do cluster.

5. **Exemplo memorável brasileiro** ✅
   - Seção 9.5: "A migração de 3 semanas que virou 2 dias" — startup de fintech brasileira, 180 mil linhas TypeScript, 312 componentes, 240h-pessoa → 16h de revisão. Números específicos, metodologia descrita, lição estrutural extraída. Rotulado implicitamente (é o único exemplo do capítulo). Bom.

6. **Camada Viva** ❌ — FALHA CRÍTICA
   - Múltiplos números perecíveis no corpo do capítulo:
     - Seção 9.3.1: "Sonnet ou Opus, dependendo da configuração e do plano" — tipo de modelo perecível
     - Seção 9.3.1: "lidera benchmarks como SWE-bench Verified com cerca de 80%" — benchmark perecível, no corpo
     - Seção 9.3.3: "US$ 20 por mês" (Cursor Pro), "US$ 10 a US$ 19 por mês" (Copilot) — preços no corpo
     - Seção 9.3.3: "Claude Pro e Max, sem cobrança adicional" — estrutura de plano perecível
   - Nenhuma referência ao Apêndice Vivo. Esses números envelhecem em meses e tornam o capítulo desatualizado.

7. **Exercícios + autoavaliação + conexões** ✅
   - 5 perguntas de revisão, 3 exercícios práticos, checklist de 6 itens, 8 conexões cruzadas (L1 e L2). Sólido. Sem Validação UAU (os outros capítulos têm — inconsistência de formato).

### 5 testes

| Teste | Resultado |
|-------|-----------|
| **Joana** | ✅ PASSA — analogia do desenvolvedor júnior / ticket completo funciona para executivo |
| **Durabilidade** | ⚠️ PARCIAL — conceito dura; preços e benchmarks no corpo envelhecem em 6 meses |
| **Diferenciação** | ✅ PASSA — distinção Claude Code vs Cursor vs Copilot é precisa e acionável |
| **Memorização** | ✅ PASSA — "migração de 3 semanas em 2 dias" e "7 fluxos profissionais" ficam na cabeça |
| **Transformação** | ✅ PASSA — leitor sai com paradigma mudado (execução → direção) e 7 fluxos concretos |

### Top lacunas (priorizadas, com seção)

1. **[CRÍTICA] Camada Viva ausente** — Seções 9.3.1 e 9.3.3: preços Cursor/Copilot, benchmark SWE-bench, estrutura de planos → mover para Apêndice Vivo com âncoras no texto.
2. **[ALTA] Critério de decisão negativo** — Seção 9.6 (ou criar 9.3.4): falta explicitar quando *não* usar Code com autonomia alta — codebase sem cobertura de teste, sistemas sem staging, domínios regulados sem supervisão humana no loop.
3. **[MÉDIA] Sem Validação UAU** — inconsistente com C10, C11, C12, C13 que todos têm. Adicionar seção 9.12.
4. **[BAIXA] Custo de tokens sem orientação prática** — Seção 9.6 menciona custos mas não orienta como monitorar nem qual ordem de grandeza esperar — ou vai para Apêndice Vivo ou ganha linha de orientação prática.

### Maior força a preservar

A analogia estagiário/desenvolvedor-júnior (9.2) e o exemplo da migração de fintech com números reais (9.5) são as melhores peças do capítulo. A regra universal "descreva objetivo final, não passos" (9.4.1) é mnemônico operacional que o leitor vai repetir. Preservar exatamente.

---

## C10 — Claude Web

**Nota: 5/10 · Veredito: "Tour de interface" claro · "Manual de botão"? ALTO**

### Os 7 elementos

1. **Abertura ancorada num Invariante** ⚠️
   - Inv. 9 (Operador) declarado, mas justificativa é fraca: "A interface é onde o operador encontra o modelo. Aqui não se programa; aqui se opera." Isso descreve o produto, não instancia o Invariante. Por que a interface Web é *especificamente* a materialização de Operador e não, digamos, a API? A justificativa precisa de 1-2 parágrafos explicando que a curva de aprendizado do Operador é integralmente visível nessa interface — e que é aqui que a maioria dos usuários trava no nível 1 do Invariante.

2. **Conceito intuitivo + analogia memorável (Teste da Joana)** ✅
   - Seção 10.2: "O escritório de coworking que você nunca explorou" — funciona. A Joana entende que paga pelo espaço inteiro e usa só uma mesa. Memorável.

3. **Quando usar / quando EVITAR** ❌ — FALHA PRINCIPAL
   - O capítulo não tem nenhuma seção ou critério de "quando usar Web vs. outra interface". A seção 10.3.3 (Web vs. Desktop) só aparece no Capítulo 11 — aqui ela está ausente. Não há critério de decisão: quando preferir Web ao Desktop? Quando uma tarefa não deve começar no Web? Quando o chat livre é errado e o Project é certo? O leitor recebe cinco fluxos mas sem nenhuma árvore de decisão.
   - A ausência desse critério é a definição de "manual de botão": ensina como usar, não quando e quando não.

4. **Profundidade técnica real** ⚠️
   - Seção 10.3.1 descreve regiões da tela (topologia visual). Seção 10.3.2 lista settings. Seção 10.3.3 lista atalhos. Tudo correto mas epidérmico. Não há explicação de como funciona a busca semântica no histórico (Cmd+K), não há profundidade sobre como o seletor de modelo afeta o comportamento, não há nenhum trade-off real (ex: extended thinking custa tokens — quanto? quando a diferença de qualidade não justifica?). A profundidade está abaixo do padrão L1.

5. **Exemplo memorável brasileiro** ✅
   - Seção 10.5: "O consultor que triplicou output em semanas" — consultor estratégico, cinco mudanças específicas, três dimensões de resultado. Rotulado e com lição estrutural. Aceitável, embora menos específico que o de C09 (sem números de faturamento, sem setor específico).

6. **Camada Viva** ❌ — FALHA CRÍTICA
   - Seção 10.3.1: "Sonnet 4.6 ou Opus 4.7" — números de versão de modelo no corpo, perecíveis em semanas.
   - Seção 10.3.1: "Opus, Sonnet e Haiku" como opções no seletor — nomes de produto perecíveis (a família de modelos muda).
   - Seção 13.3.1 (cruzada): "200 mil tokens de conteúdo na Knowledge Base" e "planos Max e Enterprise" — limites no corpo.
   - Nenhuma âncora para Apêndice Vivo.

7. **Exercícios + autoavaliação + conexões** ✅
   - 4 exercícios práticos, 5 perguntas de revisão, checklist, Validação UAU (5 critérios), conexões L1+L2, "Projeto do Capítulo". Estruturalmente completo — é o melhor elemento do capítulo.

### 5 testes

| Teste | Resultado |
|-------|-----------|
| **Joana** | ✅ PASSA — analogia do coworking funciona |
| **Durabilidade** | ❌ FALHA — versões de modelo no corpo envelhecem em semanas; o conceito de "cinco fluxos" dura |
| **Diferenciação** | ❌ FALHA — não diferencia Web de outras interfaces com critério; o capítulo é o mais substituível por qualquer tutorial online |
| **Memorização** | ⚠️ PARCIAL — os cinco fluxos são memoráveis; a anatomia da interface não fica |
| **Transformação** | ⚠️ PARCIAL — leitor profissionaliza o uso, mas sem critério de decisão sai sem saber *quando* mudar de interface |

### Top lacunas (priorizadas, com seção)

1. **[CRÍTICA] Ausência total de critério de decisão** — criar seção 10.3.4 "Web vs. Desktop vs. Mobile: quando escolher cada". Sem isso o capítulo é tour de interface.
2. **[CRÍTICA] Camada Viva ausente** — Seções 10.3.1: versões de modelo, lista Opus/Sonnet/Haiku, planos → Apêndice Vivo.
3. **[ALTA] Justificativa do Invariante** — Seção de abertura: desenvolver por que Web é instância de Inv. 9 (não só "é onde o operador opera").
4. **[ALTA] Profundidade técnica real** — Seções 10.3.x: trade-offs de modelo (quando extended thinking não vale o custo), mecânica da busca semântica, limitações reais do chat livre vs. Project.
5. **[MÉDIA] Exemplo mais específico** — Seção 10.5: adicionar setor, volume de trabalho, ou quantificar faturamento para deixar tão concreto quanto o exemplo de C09.

### Maior força a preservar

A analogia do coworking premium (10.2) é a peça mais forte — memorável e instrutiva. Os cinco fluxos profissionais (10.4) são acionáveis e reaplicáveis. O "Projeto do Capítulo" (10.11) é o melhor exercício do cluster. Preservar os três.

---

## C11 — Claude Desktop

**Nota: 6/10 · Veredito: Melhor do trio de interfaces, mas Camada Viva ausente · "Manual de botão"? MÉDIO**

### Os 7 elementos

1. **Abertura ancorada num Invariante** ⚠️
   - Inv. 9 (Operador) declarado. Justificativa melhor que C10: "Desktop é o ambiente em que o operador integra Claude ao próprio fluxo de trabalho: arquivos locais, MCPs nativos, cowork mode. A diferença para Web não é nominal, é o quanto o operador pode delegar sem sair do contexto." Passa, mas fraco: ainda não instancia o Invariante conceitualmente — explica o produto, não explica por que Cowork mode é o caso mais extremo de Autonomia do Operador que o ecossistema oferece.

2. **Conceito intuitivo + analogia memorável (Teste da Joana)** ✅
   - Seção 11.2: "O assistente que entra na sua sala" — preciso, memorável, distingue Web (videochamada) de Desktop (presença física). A Joana entende imediatamente a diferença qualitativa.

3. **Quando usar / quando EVITAR** ✅
   - Seção 11.3.3: "Web versus Desktop, quando usar cada" — critério explícito: Web para conversa/escrita/pesquisa/qualquer dispositivo; Desktop para automação/arquivos locais/apps nativos/MCP customizado. Tabela visual referenciada. O único capítulo do cluster que acerta esse elemento. Falta, porém, critério de *quando não usar Cowork mode* — ex: em sistemas com dados sensíveis sem ambiente de teste.

4. **Profundidade técnica real** ✅
   - Seção 11.3.2 (Cowork mode em profundidade): mecânica de screenshots, tiers de aplicação (full/click/read), por que browsers ficam em read. Seção 11.5: 5 cuidados de segurança com lógica real (não só "seja cuidadoso"). Profundidade genuína — melhor do cluster depois de C09.

5. **Exemplo memorável brasileiro** ✅
   - Seção 11.4: "A automação que libertou cinco horas por semana" — diretor de operações, e-commerce de 40 funcionários, rotina de segunda-feira descrita passo a passo, resultado mensurável (5h → 30min). Bem construído.

6. **Camada Viva** ❌ — FALHA CRÍTICA
   - Seção 11.3.1: "arquivo chamado `claude_desktop_config.json`, localizado em pasta específica do seu sistema (varia por SO)" — referência a nome de arquivo de configuração específico, perecível com atualizações do produto.
   - Seção 11.3.2: "Cowork mode, lançado pela Anthropic em 2025 e expandido em 2026" — data de lançamento e estado de expansão perecíveis.
   - Seção 11.3.2: "tier full, click, read" — nomenclatura de produto, muda com releases.
   - Nenhuma âncora para Apêndice Vivo.

7. **Exercícios + autoavaliação + conexões** ⚠️
   - Validação UAU (5 critérios), 8 conexões cruzadas, seção de Cuidados de Segurança (11.5). Mas sem perguntas de revisão numeradas, sem exercícios práticos numerados, sem checklist estruturado — diferente de C09, C10, C12, C13 que todos têm. Inconsistência de formato prejudica a seção mais fraca do capítulo.

### 5 testes

| Teste | Resultado |
|-------|-----------|
| **Joana** | ✅ PASSA — "assistente que entra na sua sala" funciona para executivos |
| **Durabilidade** | ⚠️ PARCIAL — conceito de Cowork dura; nome do config.json e tiers de app não duram |
| **Diferenciação** | ✅ PASSA — único capítulo do cluster com critério Web vs. Desktop explícito |
| **Memorização** | ✅ PASSA — "cinco horas em trinta minutos" e analogia da sala ficam |
| **Transformação** | ✅ PASSA — leitor sai sabendo que Desktop não é irmão menor do Web — é outra coisa |

### Top lacunas (priorizadas, com seção)

1. **[CRÍTICA] Camada Viva ausente** — Seções 11.3.1/11.3.2: nome do arquivo de config, tiers de app, data de lançamento do Cowork → Apêndice Vivo.
2. **[ALTA] Exercícios e checklist ausentes** — Seção 11.8 tem Validação UAU mas não há perguntas de revisão nem exercícios práticos. Criar seções 11.8-11.10 no mesmo padrão dos outros capítulos.
3. **[ALTA] Critério de não-uso do Cowork** — Seção 11.3.2 ou 11.5: quando *não* ativar Cowork mode (ambientes de produção, dados sensíveis, ausência de logs de auditoria).
4. **[MÉDIA] Justificativa do Invariante** — Abertura: desenvolver por que Desktop é o ponto mais alto do espectro de delegação do Operador — vai além de "integra fluxo de trabalho".

### Maior força a preservar

A analogia do assistente na sala (11.2), a seção Web vs. Desktop com critério claro (11.3.3), e o caso do diretor de operações com automação de segunda-feira (11.4) são as melhores peças. A Seção 11.3.2 sobre Cowork mode em profundidade (tiers, mecânica) é rara no L2 — profundidade técnica genuína, preservar.

---

## C12 — Claude Mobile

**Nota: 5/10 · Veredito: Funcional mas o mais epidérmico do cluster · "Manual de botão"? MÉDIO-ALTO**

### Os 7 elementos

1. **Abertura ancorada num Invariante** ⚠️
   - Inv. 9 (Operador) declarado. Justificativa: "Mobile é Claude no contexto em movimento: tarefas pequenas, decisões rápidas, captura de pensamento. Não é versão reduzida; é canal próprio com regras próprias." Fraca — é descrição do produto, não instancia o Invariante. Por que Mobile é uma dimensão específica de Inv. 9? A resposta está no capítulo mas não na abertura: Mobile expande o escopo de operação do Operador para momentos improdutivos — é a extensão do Invariante ao tempo não-estruturado. Essa é a justificativa que falta.

2. **Conceito intuitivo + analogia memorável (Teste da Joana)** ✅
   - Seção 12.2: "O colaborador que anda com você" — fone de ouvido, acesso contínuo em movimento. Funciona. A Joana entende a diferença entre o analista que atende só na sala dele e o que está disponível onde quer que você esteja.

3. **Quando usar / quando EVITAR** ✅
   - Seção 12.3.2: onde voz *não* funciona bem (precisão alta, ambientes barulhentos) — honesto.
   - Seção 12.5: "Limitações e quando não usar" — 5 cenários explícitos: trabalho longo, integração com sistemas locais, precisão extrema, ambientes barulhentos, múltiplas janelas.
   - O capítulo tem o melhor tratamento de "quando evitar" do cluster — algo raro, preserve.
   - Lacuna: falta o equivalente positivo sintetizado — um critério "use mobile quando X" além dos 8 casos de uso listados (12.3.3).

4. **Profundidade técnica real** ❌
   - Seção 12.3.1: lista de componentes (voz, câmera, atalho de compartilhar, widgets, notificações) com descrição epidérmica. Seção 12.3.2: explicação do modo voz tem alguma profundidade (latência ~1-2s, modo híbrido). Mas falta: como funciona o reconhecimento de voz em PT-BR? Quais são as limitações técnicas da câmera vs. upload de imagem? A sincronização mobile-web-desktop tem algum lag? Seção 12.3.3: 8 casos de uso são lista, não profundidade.
   - Este é o capítulo com menor profundidade técnica real do cluster.

5. **Exemplo memorável brasileiro** ✅
   - Seção 12.4: "A hora do trânsito que virou escritório" — diretor comercial em São Paulo, trânsito, duas horas por dia, 300 horas/ano recuperadas. Específico o suficiente. A contextualização "São Paulo" cria verossimilhança para o leitor brasileiro. Lição estrutural clara.

6. **Camada Viva** ❌ — FALHA CRÍTICA
   - Seção 12.1: "iOS e Android" — distribuição de plataformas OK (estável), mas "mesmo seletor de modelos entre Opus, Sonnet e Haiku" — nomes de modelo perecíveis.
   - Seção 12.3.2: "latência típica em 2026 fica em torno de 1 a 2 segundos" — benchmark de latência no corpo, perecível.
   - Seção 12.3.2: "Suporta português brasileiro com qualidade alta" — asserção de qualidade perecível (vai melhorar, mas pode mudar qualitativamente).
   - Nenhuma âncora para Apêndice Vivo.

7. **Exercícios + autoavaliação + conexões** ⚠️
   - Validação UAU (5 critérios), 6 conexões cruzadas. Mas sem perguntas de revisão, sem exercícios práticos, sem checklist — mais incompleto que C09, C10, C13. O capítulo termina abruptamente após a Validação UAU.

### 5 testes

| Teste | Resultado |
|-------|-----------|
| **Joana** | ✅ PASSA — analogia do colaborador com fone funciona |
| **Durabilidade** | ❌ FALHA — latência específica e nomes de modelo no corpo envelhecem em meses |
| **Diferenciação** | ⚠️ PARCIAL — distingue mobile de desktop/web nos casos de uso, mas sem critério de decisão positivo sintetizado |
| **Memorização** | ⚠️ PARCIAL — "trânsito de SP virou escritório" fica; lista de 8 casos não fica |
| **Transformação** | ⚠️ PARCIAL — leitor entende o valor do mobile mas sem protocolo de adoção claro |

### Top lacunas (priorizadas, com seção)

1. **[CRÍTICA] Camada Viva ausente** — Seções 12.1/12.3.2: latência específica, nomes de modelo, asserções de qualidade de voz → Apêndice Vivo.
2. **[ALTA] Profundidade técnica real** — Seção 12.3.x: limitações técnicas do reconhecimento de voz em PT-BR, diferença de qualidade câmera vs. upload, latência de sincronização — ou é profundo ou confessa que é superficial.
3. **[ALTA] Exercícios e perguntas ausentes** — Criar seções 12.9 (perguntas de revisão), 12.10 (exercícios práticos) no padrão do cluster.
4. **[MÉDIA] Critério positivo sintetizado** — Seção 12.5 ou criar 12.3.4: "Use mobile quando [X], não use quando [Y]" numa tabela ou parágrafo — hoje o leitor tem a lista de 8 casos e a lista de 5 limitações mas sem síntese.
5. **[MÉDIA] Justificativa do Invariante** — Abertura: Mobile como extensão do Inv. 9 ao tempo não-estruturado — isso é o argumento que falta.

### Maior força a preservar

A seção "Limitações e quando não usar" (12.5) é a melhor do capítulo — honesta, específica, rara no cluster. O caso do trânsito de São Paulo (12.4) é memorável e geograficamente ancorado no Brasil. A descrição do modo híbrido voz+teclado (12.3.2) é insight operacional útil que não aparece em outros lugares. Preservar os três.

---

## C13 — Claude Projects

**Nota: 7/10 · Veredito: O mais maduro do cluster, com lacuna estrutural em Camada Viva · "Manual de botão"? BAIXO**

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅
   - Inv. 3 (Camada Dupla) declarado e justificado com precisão real: "Projects é Camada Dupla materializada: o padrão durável vai no system prompt e nos arquivos persistentes; o número volátil vai na conversa do dia." Inv. 2 (Extremidades) como secundário com razão técnica: system prompt ocupa posição mais forte do contexto. Esta é a melhor justificativa de abertura do cluster — instancia o Invariante com argumento técnico, não descrição de produto.

2. **Conceito intuitivo + analogia memorável (Teste da Joana)** ✅
   - Seção 13.2: "A sala de trabalho dedicada" — café diferente toda semana vs. sala de trabalho com biblioteca própria. Memorável, exato, funciona para executivo e técnico.

3. **Quando usar / quando EVITAR** ✅
   - Seção 13.3.2: explica o que faz um Project medíocre vs. profissional (curadoria, especificidade das instruções, manutenção). Seção 13.3.2 final: critério claro de "quando Project vs. chat solto" (trabalho recorrente vs. pergunta pontual). Seção 13.5: 5 limitações/armadilhas com profundidade real (drift de informação, proliferação, limite de tokens). Sólido, embora faltasse uma tabela de decisão visual.

4. **Profundidade técnica real** ✅
   - Seção 13.3.1: anatomia das 3 camadas com distinção "arquivos compartilhados no chat vs. Knowledge Base" — detalhe técnico genuíno que a maioria dos tutoriais ignora. Seção 13.3.2: 4 critérios de Project bem feito, não só "adicione arquivos". Seção 13.5 menciona comparação com RAG dedicado (Cap 6) quando limits são excedidos — esse trade-off é profundidade real.

5. **Exemplo memorável brasileiro** ✅
   - Seção 13.4: "A agência que digitalizou memória institucional" — agência de comunicação com 40 funcionários, 25 clientes, onboarding 3 semanas → 5 dias, três dimensões de resultado, quote do CFO do cliente. É o melhor exemplo do cluster: específico, com múltiplas dimensões de impacto, com voz de stakeholder externo.

6. **Camada Viva** ❌ — FALHA CRÍTICA
   - Seção 13.3.1: "limite combinado é tipicamente 200 mil tokens de conteúdo na Knowledge Base, mas isso varia por plano" — limite específico no corpo.
   - Seção 13.3.1: "Em planos Max e Enterprise, esse limite é maior" — estrutura de planos no corpo.
   - Seção 13.5: "limite combinado de arquivos é tipicamente 200 mil tokens, que cobre algumas centenas de páginas" — repetição do limite no corpo.
   - Seção 13.5: "Em planos Team e Enterprise, limites maiores" e "Em plano Pro, Projects são individuais e não podem ser compartilhados" — tiers e restrições de compartilhamento no corpo.
   - Nenhuma âncora para Apêndice Vivo. É o capítulo com mais números perecíveis no corpo de todo o cluster.

7. **Exercícios + autoavaliação + conexões** ✅
   - 5 perguntas de revisão, 4 exercícios práticos, "Projeto do Capítulo" (exercício longo e ambicioso), checklist de 6 itens, Validação UAU (5 critérios), 7 conexões cruzadas, referências com URLs. O mais completo do cluster.

### 5 testes

| Teste | Resultado |
|-------|-----------|
| **Joana** | ✅ PASSA — "sala de trabalho dedicada" vs. café toda semana é cristalino |
| **Durabilidade** | ❌ FALHA — limites de tokens, estrutura de planos no corpo envelhecem em meses |
| **Diferenciação** | ✅ PASSA — Projects como "arquitetura cognitiva organizacional" vs. "recurso técnico" é posicionamento claro |
| **Memorização** | ✅ PASSA — exemplo da agência e CFO comentando "vocês lembram de tudo" são cenas memoráveis |
| **Transformação** | ✅ PASSA — leitor sai com critério de criação, protocolo de curadoria e caso de organização para defender internamente |

### Top lacunas (priorizadas, com seção)

1. **[CRÍTICA] Camada Viva ausente** — Seções 13.3.1 e 13.5: limite de 200k tokens, tiers de plano (Pro/Team/Enterprise), compartilhamento → Apêndice Vivo com âncoras. É o capítulo com mais violações dessa regra.
2. **[ALTA] Critério de decisão Projects vs. RAG** — Seção 13.5 menciona mas não desenvolve: quando a Knowledge Base de Projects não é suficiente e RAG dedicado é necessário. Um parágrafo de critério (volume, atualização em tempo real, multiusuário) elevaria muito a profundidade.
3. **[MÉDIA] Compartilhamento em equipes** — Seção 13.3.1: como funciona tecnicamente o compartilhamento em Team/Enterprise? Permissões, ownership, visibilidade — tema prático ausente.
4. **[BAIXA] Tabela de decisão visual** — Seção 13.3.2: converter os 4 critérios de Project bem feito em tabela ou checklist visual, mais acionável para o leitor em pressa.

### Maior força a preservar

A justificativa do Invariante 3 (Camada Dupla materializada) na abertura é o melhor parágrafo do cluster — preciso, técnico, pedagógico. O exemplo da agência (13.4) com quote do CFO é o exemplo mais rico do cluster. A distinção "arquivos no chat vs. Knowledge Base persistente" (13.3.1) é detalhe técnico que o leitor não encontra em tutoriais. Os 6 padrões de uso (13.3.3) são framework acionável. Preservar todos.

---

## LINHAS-TRACKER

```
C09|7|BAIXO|CAMADA_VIVA_AUSENTE(precos-benchmarks-corpo)
C10|5|ALTO|CRITERIO_DECISAO_AUSENTE+CAMADA_VIVA_AUSENTE
C11|6|MEDIO|CAMADA_VIVA_AUSENTE+EXERCICIOS_INCOMPLETOS
C12|5|MEDIO-ALTO|CAMADA_VIVA_AUSENTE+PROFUNDIDADE_TECNICA_EPIDÉRMICA
C13|7|BAIXO|CAMADA_VIVA_AUSENTE(limite-tokens-tiers-corpo)
```

---

*Auditoria realizada em 2026-06-17. Próximo passo recomendado: upgrade dos capítulos em ordem de prioridade C10→C12→C11→C13→C09, priorizando os dois críticos (Camada Viva e critério de decisão) antes da galé.*
