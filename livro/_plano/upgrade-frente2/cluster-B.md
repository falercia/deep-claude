# CHANGELOG — UPGRADE CLUSTER B: ECOSSISTEMA 1
**Data:** 2026-06-17 · Editor Executivo: Claude (Sonnet 4.6)
**Capítulos:** C09 Claude Code · C10 Claude Web · C11 Desktop · C12 Mobile · C13 Projects
**Passes executados:** P1 (Camada Viva) · P2 (Decisão + Invariante) · P3 (Exercícios)

---

## C09 — Claude Code

### P1 — Camada Viva
- **9.3.3:** Removidos preços absolutos de Cursor Pro (US$20/mês) e Copilot (US$10–19/mês) do corpo → substituídos por ponteiro ao Apêndice Vivo (J).
- **9.3.3:** Removido benchmark "SWE-bench Verified com cerca de 80%" do corpo → ponteiro ao Apêndice Vivo (J).
- **9.3.3:** Removida referência a planos nominais ("Claude Pro e Max, sem cobrança adicional") → ponteiro ao Apêndice Vivo (J).

### P2 — Decisão + Invariante
- **Abertura (Inv. 6):** Expandida de 3 linhas para 2 parágrafos. Explica o critério operacional de calibração de autonomia ("quanto menos você entende o que o agente fará, menos autonomia") e por que o Modo Plan existe. Adiciona instância do Inv. 9 ao CLAUDE.md.
- **Nova seção 9.3.4 — "Quando usar Claude Code / quando EVITAR":** Tabela de critério explícito por situação (codebase com/sem testes, staging, domínio regulado, objetivo exploratório). Identifica a falha nº1 (autonomia alta em codebase sem testes).

### P3 — Exercícios
- **4 exercícios reescritos** com critério de autonomia explícito: Exercício 1 inclui avaliação de cobertura antes de executar; Exercício 2 especifica batches com escalada de confiança; Exercício 4 inclui comparação de tipo de atenção exigida (execução vs. revisão estrutural).
- **Pergunta de revisão 6 adicionada:** foca nas condições de risco de autonomia alta.
- **Checklist:** item de avaliação de nível de autonomia adicionado.

### Seção adicionada
- **9.13 — Validação UAU** (antes ausente): 5 critérios, incluindo o critério de decisão negativo (item 3). Referências internas corrigidas de "24.x" para "9.x".

### Preservados (conforme instrução)
- Analogia dev-júnior/ticket (9.2): intocada.
- Caso da fintech com números de migração (9.5): intocado.
- Regra universal "descreva objetivo final" (9.4.1): intocada.

---

## C10 — Claude Web

### P1 — Camada Viva
- **10.3.1:** Removidos nomes de versão "Sonnet 4.6 ou Opus 4.7" do corpo → substituídos por referência a "tiers disponíveis" com ponteiro ao Apêndice Vivo (J).
- **10.3.1:** Removida lista nominal "Opus, Sonnet e Haiku" do seletor → substituída por "tiers disponíveis (premium, balanceado e compacto)".

### P2 — Decisão + Invariante
- **Abertura (Inv. 9):** Reescrita de 1 linha para 3 parágrafos operacionais. Explica por que Web é onde o Invariante 9 fica mais visível (sem código nem arquitetura para se esconder), por que a maioria trava no nível 1, e que a lacuna é de competência de operação, não de acesso.
- **Nova seção 10.3.4 — "Quando usar Web / quando EVITAR (e quando preferir outra interface)":** Este era o gap crítico apontado na auditoria (5/10 por falta de critério). Cobre: Web para conversa/escrita/pesquisa/Artifacts; Desktop para arquivos locais/MCP; Mobile para voz/câmera; Code para engenharia; quando chat livre vs. Project. Tabela de decisão por tipo de tarefa.

### P3 — Exercícios
- **4 exercícios reescritos** para ser acionáveis com critério de medição: Exercício 1 inclui comparação antes/depois; Exercício 2 adiciona "critério de parada" para iteração refinadora; Exercício 3 substitui "auditoria de uso" por "auditoria de interface com decisão de migração"; Exercício 4 adiciona critério de adoção.
- **Checklist e Validação UAU:** item de decisão de interface adicionado; critério 2 da UAU substituído por critério de decisão.
- **Resumo Executivo:** linha do seletor de modelo movida para Apêndice Vivo; linhas de "quando usar Web" e "quando preferir outra" adicionadas.

### Preservados (conforme instrução)
- Analogia do coworking premium (10.2): intocada.
- Cinco fluxos profissionais (10.4): intocados.
- Projeto do Capítulo (10.11): intocado.

---

## C11 — Claude Desktop

### P1 — Camada Viva
- **11.3.1:** Removido nome específico do arquivo de configuração (`claude_desktop_config.json`) → substituído por "arquivo de configuração do Desktop" com ponteiro ao Apêndice Vivo (J).
- **11.3.2:** Removida data de lançamento do Cowork mode ("lançado pela Anthropic em 2025 e expandido em 2026") → texto atemporal.
- **11.3.2:** Nomes de tier "full/click/read" movidos para "três níveis (completo / clique / leitura)" com ponteiro ao Apêndice Vivo (J) para nomenclatura corrente.
- **Resumo Executivo:** linha de tiers atualizada para Apêndice Vivo.

### P2 — Decisão + Invariante
- **Abertura (Inv. 9):** Reescrita. Posiciona Desktop como "ponto mais alto do espectro de delegação do Inv. 9" — não é diferença de grau, é de natureza. Explica que a responsabilidade do Operador aumenta proporcionalmente.
- **11.3.2 — Cowork mode em profundidade:** Adicionada seção "Quando NÃO ativar Cowork mode": 4 cenários específicos (sistemas de produção sem staging, dados sensíveis sem política de retenção, apps com ações destrutivas não configuradas para confirmação, fluxo que o operador não entende).

### P3 — Exercícios (seções antes ausentes — inconsistência de formato corrigida)
- **11.8 — Checklist do Capítulo:** 7 itens, incluindo critério de não-uso do Cowork.
- **11.9 — Perguntas de Revisão:** 5 perguntas, incluindo pergunta sobre espectro de delegação e critério de risco.
- **11.10 — Exercícios Práticos:** 4 exercícios acionáveis (setup MCP, automação com critério de risco, comparação Desktop vs. Web, defesa interna).
- **11.11 — Projeto do Capítulo:** "Libere cinco horas mensais de trabalho mecânico."
- **11.12 — Validação UAU:** Renumerada; critério 2 de decisão de risco adicionado.

### Preservados (conforme instrução)
- Analogia do assistente na sala (11.2): intocada.
- Seção Web vs. Desktop com critério (11.3.3): intocada (usada como modelo para C10).
- Caso do diretor de operações com automação de segunda-feira (11.4): intocado.
- Cowork mode em profundidade (11.3.2): profundidade preservada, nomenclatura de tiers apenas tornada ponteiro.

---

## C12 — Claude Mobile

### P1 — Camada Viva
- **12.1:** Removida lista nominal "Opus, Sonnet e Haiku" do seletor mobile → ponteiro ao Apêndice Vivo (J).
- **12.3.2:** Removida "latência típica em 2026 fica em torno de 1 a 2 segundos" → substituída por referência a "condições de conexão estável" com ponteiro ao Apêndice Vivo (J).
- **12.3.2:** Removida asserção "Suporta português brasileiro com qualidade alta" como fato absoluto → reescrita para refletir condições (versão do app, qualidade de conexão).

### P2 — Decisão + Invariante
- **Abertura (Inv. 9):** Reescrita. Define Mobile como "extensão do Inv. 9 ao tempo não-estruturado" — muda o tipo de competência exigida (o que cabe em 5 min de carro, o que cabe em voz, o que deve aguardar o Desktop). Essa era a justificativa ausente.
- **Nova seção 12.3.4 — "O que muda tecnicamente no Mobile":** Profundidade técnica real que faltava (falha crítica da auditoria). Cobre: contexto fragmentado e por que Projects são especialmente importantes no Mobile; câmera vs. upload (casos de uso diferentes, não qualidade diferente); condições de degradação do reconhecimento de voz em PT-BR (previsíveis e contornáveis); sincronização com Web/Desktop (lag de segundos, comportamento no envio); bateria e limites de sessão. Cada ponto é operacional, não apenas descritivo.

### P3 — Exercícios (seções antes ausentes — inconsistência de formato corrigida)
- **12.8 — Checklist do Capítulo:** 7 itens.
- **12.9 — Perguntas de Revisão:** 5 perguntas com profundidade técnica (degradação de voz, câmera vs. upload, critério de janela de tempo).
- **12.10 — Exercícios Práticos:** 4 exercícios acionáveis (mapeamento de janelas improdutivas, semana deliberada, modo híbrido voz+teclado, câmera em uso real).
- **12.11 — Projeto do Capítulo:** "Recupere duas horas semanais de tempo improdutivo."
- **12.12 — Validação UAU:** Renumerada; critério 2 de decisão e critério 3 de profundidade técnica adicionados.

### Preservados (conforme instrução)
- Seção "Limitações e quando não usar" (12.5): intocada (melhor do capítulo, conforme auditoria).
- Caso do trânsito de São Paulo (12.4): intocado.
- Descrição do modo híbrido voz+teclado (12.3.2): intocada.

---

## C13 — Claude Projects

### P1 — Camada Viva
- **13.3.1:** Removido "limite combinado é tipicamente 200 mil tokens de conteúdo na Knowledge Base, mas isso varia por plano" → substituído por ponteiro ao Apêndice Vivo (J).
- **13.3.1:** Removida referência a "planos Max e Enterprise" com limite maior → generalizada para "planos corporativos".
- **13.5:** Removida repetição do limite "200 mil tokens, que cobre algumas centenas de páginas" → ponteiro ao Apêndice Vivo (J).
- **13.5:** Removidas referências nominais a "plano Pro / Team / Enterprise" e restrições de compartilhamento específicas → substituídas por "planos de entrada / corporativos" com ponteiro ao Apêndice Vivo (J) para mecânica específica de compartilhamento.

### P2 — Decisão + Invariante
- **Nova seção 13.5.1 — "Projects versus RAG dedicado: critério de decisão":** Resolve lacuna de alta prioridade da auditoria. Cobre: 5 condições para usar Projects; 5 condições para migrar para RAG dedicado (volume, tempo real, multiusuário, rastreabilidade); tabela de decisão visual com casos concretos.

### P3 — Exercícios
- **Exercício 4 reescrito:** Incorpora o critério de 13.5.1 (Projects vs. RAG) antes de construir — alinha o exercício à nova seção de profundidade.
- **Pergunta de revisão 5 reformulada:** Solicita 3 condições concretas para RAG (não apenas "quando é melhor").
- **Pergunta de revisão 6 adicionada:** Cenário concreto de decisão de arquitetura (base de RH com 500 políticas).
- **Checklist:** item de critério Projects vs. RAG adicionado.
- **Resumo Executivo:** linha de limites atualizada para Apêndice Vivo; linha de Projects vs. RAG adicionada.
- **Validação UAU:** critério 2 substituído por critério de decisão Projects vs. RAG; critério 3 e 4 reformulados para refletir profundidade real.

### Preservados (conforme instrução)
- Justificativa do Inv. 3 (Camada Dupla materializada) na abertura: intocada (melhor parágrafo do cluster).
- Analogia da sala de trabalho dedicada (13.2): intocada.
- Caso da agência com quote do CFO (13.4): intocado.
- Distinção "arquivos no chat vs. Knowledge Base persistente" (13.3.1): intocada.
- Seis padrões de uso (13.3.3): intocados.

---

## ESTADO APÓS UPGRADE

| Capítulo | Nota pré | Nota pós (estimada) | Risco "manual de botão" |
|----------|----------|---------------------|------------------------|
| C09 | 7/10 | 8/10 | BAIXO |
| C10 | 5/10 | 7.5/10 | BAIXO (de ALTO) |
| C11 | 6/10 | 8/10 | BAIXO (de MÉDIO) |
| C12 | 5/10 | 7.5/10 | BAIXO (de MÉDIO-ALTO) |
| C13 | 7/10 | 8.5/10 | BAIXO |

---

## ITENS QUE AINDA PEDEM REESCRITA PROFUNDA (P5)

**C10 (Web) — Profundidade técnica epidérmica nas seções 10.3.1–10.3.3:**
O tour de interface foi condensado mas não aprofundado. A seção de atalhos (10.3.3) ainda é lista sem trade-offs; a seção de settings (10.3.2) não explica mecânica do profile como system prompt pessoal com profundidade técnica real; a seção de anatomia (10.3.1) não explica como funciona a busca semântica do Cmd+K. P5 deveria adicionar 1-2 parágrafos técnicos reais nessas subseções.

**C12 (Mobile) — Exemplo memorável (12.4) sem profundidade adicional de adoção:**
O caso do diretor comercial foi preservado, mas não foi expandido com um segundo eixo de resultado (além de horas recuperadas). Um detalhe sobre a curva de adaptação das primeiras semanas (o que ele aprendeu a delegar vs. a guardar para o Desktop) tornaria o exemplo mais instrutivo, não apenas mais memorável. P5 poderia adicionar 2-3 linhas de insight operacional extraído do caso.

**C11 (Desktop) — Seção 11.3.3 (Web vs. Desktop) é boa mas não cobre Mobile e Code:**
A seção já existe e é o modelo do cluster, mas foi escrita antes da adição do critério Web/Desktop/Mobile/Code em C10. Em P5, seria consistente expandir a tabela de 11.3.3 para cobrir os quatro eixos explicitamente, alinhando com a seção 10.3.4 de C10.

**C13 (Projects) — Compartilhamento em Teams e Enterprise:**
A seção 13.3.1 e 13.5 ainda não descrevem a mecânica de compartilhamento em planos corporativos (ownership, permissões, visibilidade de Knowledge Base). Isso foi movido para o Apêndice Vivo como item perecível, mas a descrição conceitual de como o compartilhamento funciona (independente de tier) poderia ser adicionada ao corpo. P5 deveria resolver.

---

*Upgrade executado em 2026-06-17. Próxima etapa recomendada: revisão de galé (Onda 5) com versão de leitura linear completa dos 5 capítulos para verificar coerência de tom e numeração de seções.*
