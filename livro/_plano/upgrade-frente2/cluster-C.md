# CHANGELOG — Cluster C (Caps 14–18)
## Passes P1–P4 executados em 2026-06-17

---

## RESUMO DOS PASSES

### P1 — CAMADA VIVA (Perecível → Ponteiro ao Apêndice J)

**C14 (Artifacts)**
- "Artifacts cobrem em 2026 seis tipos" → "Artifacts suportam seis tipos [...] lista atual no Apêndice J"
- Lista de imports React suportados (Recharts, Lucide, Tailwind) → ponteiro ao Apêndice J
- Custo em R$ 200 do caso da empreendedora → padrão durável proporcional (sem número perecível)

**C15 (Research)**
- Latência "entre cinco e trinta minutos" → "alguns minutos a dezenas" com ponteiro ao Apêndice J
- "orquestrador rodando Opus, dez a trinta subqueries" → estrutura preservada, números removidos
- Custo em tokens "equivalente a dez ou vinte conversas" → princípio (significativamente maior) + ponteiro
- Caso da diretora: "vinte e dois minutos", "quarenta páginas", "cento e cinquenta e três fontes", "95% de acerto" → padrões qualitativos, números de exemplificação removidos

**C16 (Web Search)**
- Latência "30 segundos a um minuto" + "três e dez páginas" → "em segundos" + ponteiro ao Apêndice J
- "Em claude.ai com plano adequado, Web Search aparece como botão" → princípio de ativação + ponteiro ao Apêndice J
- Citações como "links clicáveis em nova aba" → descrição sem UI específica

**C17 (Voice)**
- "Voz disponível em três interfaces em 2026" + disponibilidade por plano → ponteiro ao Apêndice J
- Latência "1 a 2 segundos" → "faixa de conversa humana natural" + ponteiro ao Apêndice J

**C18 (Scheduled Tasks)**
- Sem intervenções P1 necessárias — o capítulo já estava limpo de specs perecíveis.

---

### P2 — DECISÃO + INVARIANTE

**C14 (Artifacts) — Invariante 9**
- Caixa decorativa substituída por pergunta substantiva: quem é responsável pelo que está dentro do artifact quando sai para o mundo? Distinção "Claude produz; você entrega" → ferramenta vira autoria, autoria carrega consequência. Exemplos concretos: cálculo errado no HTML, dados desatualizados no Markdown, protótipo que coleta dados sem aviso.
- Nova seção **14.3.5 — Quando NÃO usar artifacts**: 5 anti-padrões com critério real (resposta conversacional, rascunho inicial, sem destino, requisitos de produção, conteúdo confidencial).

**C17 (Voice) — Invariante 9**
- Caixa decorativa substituída por pergunta substantiva: o que você faz com o pensamento que voz destravou? Três cenários de responsabilidade do operador: transcreve e guarda (ok), envia resumo sem revisar (delegou autoria), usa posição oral como base de decisão sem confirmar (delegou julgamento). Responsabilidade dupla: reter e revisar antes de exportar.

---

### P3 — EXERCÍCIOS

**C17 (Voice) — capítulo estava sem exercícios/checklist/projeto**
Adicionadas, no padrão dos outros capítulos:
- **17.6 — Checklist do Capítulo** (5 itens)
- **17.7 — Perguntas de Revisão** (5 perguntas)
- **17.8 — Exercícios Práticos** (4 exercícios: brainstorm pré-evento, reflexão pós-evento ao vivo, problema travado em voz, aprendizado por diálogo)
- **17.9 — Projeto do Capítulo**: substituir uma sessão de escrita por semana por sessão de voz por um mês
- Seções renumeradas: RESUMO EXECUTIVO → 17.10, VALIDAÇÃO UAU → 17.11

**Profundidade C17 (Voice)** — seção nova:
- **17.3.4 — A mecânica cognitiva: por que voz produz pensamento diferente**: pensamento declarativo vs exploratório, papel do interlocutor que faz perguntas pontuais, latência zero de julgamento externo, cognição distribuída no tempo. Ancorado em psicologia cognitiva sem números específicos. Transforms o capítulo de tutorial de UI para método.

---

### P4 — FALSA CONFIANÇA (C15 e C16)

**C15 (Research) — nova seção 15.4.0**
- Título: "O problema que ninguém menciona: relatório bem-formatado com cem fontes que produz falsa confiança"
- Argumento central: volume de citações é evidência de que documentos foram lidos, não de rigor epistêmico. 140 fontes de qualidade variável + otimização por coerência narrativa = relatório que soa autoritativo com premissas falsas distribuídas invisivelmente.
- 5 práticas do executivo maduro: auditoria das fontes âncora (não todas), procurar a afirmação mais desejável, identificar o que o relatório não encontrou, distinguir fato verificado de síntese inferida, cuidado com números compostos.
- Fechamento do Invariante 1: "não confunda volume de citação com verdade verificada."

**C16 (Web Search) — nova seção 16.5.1**
- Título: "O padrão de falsa confiança específico do Web Search"
- Distingue do risco do Research: aqui o perigo é menor em escala mas mais frequente — resposta com citação inline que parece verificada porque o link está lá, mas que nunca foi aberta.
- 4 gatilhos de verificação obrigatória: material que sai da organização, afirmação numérica, afirmação que contradiz o que você sabia, afirmação que confirma perfeitamente sua tese.
- Fechamento do Invariante 1: "o link não é a verificação. Abrir o link é a verificação."

---

## PRESERVADO INTACTO

- **C15** — toda a honestidade existente sobre Plausibilidade (fontes de qualidade variável, alucinação possível, custo significativo)
- **C16** — hierarquia dos 5 tiers de confiabilidade, caso do diretor e o "fato que não era fato"
- **C18** — integridade do capítulo (o mais forte do cluster, 7/10); sem alterações de conteúdo

---

## O QUE AINDA PEDE REESCRITA PROFUNDA (P5)

**C17 (Voice)** — mesmo após P3/P4, ainda está abaixo do potencial. O que falta:
- Caso memorável (17.4) é bom mas único; precisaria de segundo caso em contexto executivo puro (não acadêmico)
- A seção de padrões profissionais (17.3.3) lista os quatro padrões corretamente mas não os aprofunda com estrutura de prompt — o leitor sabe o que fazer mas não como fazer bem
- Ausência de tratamento sobre **qualidade da síntese de voz**: Claude às vezes sintetiza de forma que distorce o que você disse; o operador precisa de critério para revisar sumários de voz antes de usar
- Conexão com Projects (como destino de conversas de voz) é mencionada mas não exemplificada com fluxo concreto

**C14 (Artifacts)** — seção 14.3.1 (exemplos práticos por tipo) tem qualidade desigual; Tipo 5 (SVG) e Tipo 4 (Mermaid) são superficiais comparados a Tipo 6 (React). Uma P5 deveria nivelar por cima.

**C15 (Research)** — seção 15.3.2.2 (prompt completo de Research) é o ponto mais forte do capítulo mas vive numa subseção de terceiro nível; merecia elevação estrutural e um segundo exemplo em domínio diferente do fintech.

---
*Changelog produzido por Editor Executivo — passes P1–P4 completos.*
