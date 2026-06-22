# Changelog — Cluster A (C01, C02, C04)
**Data:** 2026-06-17
**Passes aplicados:** P1 (Camada Viva), P2 (Decisão + Invariante), P3 (Exercícios)

---

## L2-C01 — Claude para Executivos

### P1 — Camada Viva
Nenhum número perecível encontrado no corpo original (C01 era o capítulo menos técnico). Sem movimentações de P1 necessárias.

### P2 — Decisão + Invariante
- **Adicionado:** seção `1.2` expandida com descrição mecânica das três ferramentas mencionadas por nome (Briefing, Research, Voz) — cada uma agora tem mecânica concreta + analogia + link para capítulo específico.
- **Adicionado:** seção `1.4.1 — O Critério de Delegação`, com listas explícitas "delegar com segurança" vs "não delegar", mais régua prática.
- **Reforçado:** Invariante 8 (Responsabilidade Indelegável) aparece agora no CORPO do capítulo (seção 1.4.1) operando em tensão real, não apenas no chapéu.

### P3 — Exercícios
- **Adicionado:** seção `1.6.1 — Perguntas de Revisão` (5 perguntas).
- **Adicionado:** seção `1.6.2 — Exercícios Práticos` (4 exercícios com entregável explícito: mapeamento de semana, teste de briefing pré-reunião, auditoria de delegação, rotina de 7 dias).
- **Adicionado:** seção `1.6.3 — Projeto do Capítulo` (documento de sistema de amplificação pessoal, 2 páginas, com avaliação em 30 dias).

---

## L2-C02 — Entendendo o Claude

### P1 — Camada Viva
- **2 movimentações:**
  1. `seção 2.3.3`: percentuais de preferência em comparação cega (47% / 29% / 24% vs GPT-5.4 e Gemini 3.1 Pro) removidos do corpo → substituídos por ponteiro para Apêndice Vivo (J).
  2. `seção 2.3.4`: estimativas de receita ("US$ 5 bilhões anuais contra US$ 30+ bilhões da OpenAI") e montante de investimento Amazon ("US$ 4 bilhões") removidos do corpo → mantida a informação estrutural (parceria com Amazon, independência entre parceiros), dado numérico movido para Apêndice Vivo.

### P2 — Decisão + Invariante
- **Adicionado:** seção `2.5.1 — Quando usar Claude — e quando não usar`, com framework durável de três blocos: "Use Claude quando", "Use outro modelo quando", "O critério durável". Sem preços; critérios baseados em DNA de empresa, perfil de risco, ecossistema e requisito de explicabilidade.
- **Reforçado:** Invariante 8 aparece no CORPO do capítulo — parágrafo adicionado ao final da seção 2.4 (caso da seguradora), mostrando a tensão do Invariante operando de verdade: a responsabilidade não migrava para o modelo, Claude apenas tornava a tensão visível antes do dano.

### P3 — Exercícios
C02 já tinha exercícios de qualidade (seções 2.10 e 2.11). Não reescritos; o projeto do capítulo ("Por que Claude, para nós") permanece e agora é informado pelo framework adicionado em 2.5.1.

---

## L2-C04 — Todos os Modelos Claude

### P1 — Camada Viva
- **7 movimentações (o capítulo mais perecível do livro):**
  1. `seção 4.3.1` inteira reescrita: removidos Opus 4.6/4.7, Sonnet 4.5/4.6, Haiku 4.5 como nomes fixos no corpo → substituídos por "tier premium", "tier balanceado", "tier de velocidade".
  2. Benchmark Opus: "80,8% SWE-bench Verified" e "64,3% SWE-bench Pro" → removidos, ponteiro para Apêndice Vivo.
  3. Benchmark Sonnet: "77,2% SWE-bench Verified (setembro 2025)" → removido, ponteiro para Apêndice Vivo.
  4. Preço Opus: "US$ 15/75 por M tokens" → removido do corpo e do Resumo Executivo, ponteiro para Apêndice Vivo.
  5. Preço Sonnet: "US$ 3/15 por M tokens" → removido do corpo e do Resumo Executivo, ponteiro para Apêndice Vivo.
  6. Preço Haiku: "US$ 0,80/4 por M tokens" → removido do corpo e do Resumo Executivo, ponteiro para Apêndice Vivo.
  7. "47% comparações cegas, contra 29% GPT-5.4 e 24% Gemini 3.1 Pro" na seção 4.3.1 → removido (dado repetido de C02; também perecível).
  8. "Janela de 200 mil tokens" → mantida menção ao padrão estrutural; limite exato apontado para Apêndice Vivo no Resumo.

### P2 — Decisão + Invariante
- **Adicionado:** seção `4.6.1 — Quando usar cada tier — e quando EVITAR`, com critérios explícitos de uso e evitação para cada um dos três tiers. Cada tier tem bloco "Use quando" e "Evite quando" com situações concretas (não genéricas).
- **Reforçado:** Invariante 4 (Encaixe) aparece no corpo da seção 4.6.1 em tensão real: usar modelo errado não é desperdício de custo, é degradação de resultado; Opus em tarefa simples não entrega mais qualidade, Haiku em tarefa complexa não economiza.

### P3 — Exercícios
C04 já tinha exercícios (seções 4.11 e 4.12). Preservados integralmente — são exercícios com entregável real (teste comparativo cego, cálculo de economia, teste A/B extended thinking, esboço de roteador, implementação real de roteamento).

---

## Status por capítulo

| Capítulo | Score original | P1 | P2 | P3 | Reescrita profunda (P5)? |
|---|---|---|---|---|---|
| C01 Executivos | 5/10 | — | Completo | Completo (adicionado do zero) | Não; profundidade adequada após edição |
| C02 Entendendo Claude | 7/10 | 2 movimentações | Completo | Preservado | Não |
| C04 Modelos | 6/10 (manual de botão) | 7 movimentações | Completo | Preservado | Não; critério de decisão agora presente |
