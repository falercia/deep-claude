# Auditoria Frente 2 — qualidade dos 19 capítulos redigidos do L2

**Data:** 2026-06-17 · Banca adversarial (4 papéis + 5 testes) contra a régua do Livro 1. Detalhe por cluster em `auditoria-frente2/`.

---

## 1. VEREDITO

**Média ~6,2/10.** Nenhum capítulo é ruim; nenhum está, ainda, no nível do L1. A distância para o L1 **não é de talento — é de método**: os capítulos descrevem bem o produto, mas falham nos mesmos pontos, de forma **sistêmica e padronizada**. Isso é a boa notícia: corrige-se em **passes temáticos**, não em 19 reescritas sob medida.

---

## 2. AS NOTAS

| Cap | Tema | Nota | Manual de botão |
|---|---|---|---|
| C30 | Skills | **8** | baixo |
| C02 | Entendendo Claude | 7 | baixo |
| C09 | Claude Code | 7 | baixo |
| C13 | Projects | 7 | baixo |
| C15 | Research | 7 | médio |
| C16 | Web Search | 7 | médio |
| C18 | Scheduled Tasks | 7 | baixo |
| C28 | MCP | 7 | médio |
| C04 | Modelos | 6 | **alto** |
| C11 | Desktop | 6 | médio |
| C14 | Artifacts | 6 | médio |
| C19b | Enterprise | 6 | médio |
| C20 | Connectors | 6 | médio |
| C31 | Subagents | 6 | médio |
| **C01** | Executivos | **5** | alto |
| **C10** | Web | **5** | **alto** (tour de interface) |
| **C12** | Mobile | **5** | alto |
| **C17** | Voice | **5** | alto |
| **C19** | Team | **5** | alto |

---

## 3. OS 5 PADRÕES SISTÊMICOS (a verdadeira lista de trabalho)

**① Camada Viva ausente — em TODOS os 19.** *(o achado mais grave e mais fácil de corrigir)*
Preços (Cursor $20, Copilot), benchmarks (SWE-bench %), nomes/versões de modelo (Sonnet 4.6, Opus 4.7), tiers (Pro/Team/Enterprise/Max), limites (KB 200k tokens) — tudo no corpo, nenhum apontado ao Apêndice Vivo. **Envelhecimento garantido em 3–6 meses.** É a violação da própria tese da série (Camada Dupla).

**② Invariante declarado, mas decorativo.** A abertura ancora num Invariante e o corpo nunca volta à tensão. Pior em C10, C11, C12, C14, C17. Só C09, C13, C15, C16, C18, C28, C30 honram o Invariante ao longo do texto.

**③ "Quando evitar" ausente — a marca do "manual de botão".** O critério de decisão (quando NÃO usar a capacidade) falta na maioria. É o que separa referência de tutorial. Exceções boas: C11 (Web vs Desktop), C12 (seção 12.5).

**④ Exercícios declarativos ou ausentes.** C01 e C17 não têm exercícios/projeto; os demais tendem ao declarativo. O L1 tem exercícios acionáveis com entregável — a régua.

**⑤ Profundidade que para cedo.** C15/C16 (Research/Web Search) instanciam Plausibilidade com honestidade mas não enfrentam o ponto mais duro: **o relatório bem-formatado com 150 fontes que gera falsa confiança**. É exatamente onde o Invariante 1 mordia.

---

## 4. ACHADOS ESTRUTURAIS PONTUAIS

- **C19 ↔ C19b (Team/Enterprise): sobreposição redundante.** Ambos descrevem SSO/SAML do zero e compliance. Correção: C19 fecha com tabela de fronteira (o que Enterprise faz que Team não faz); C19b assume essa tabela como lida.
- **C30 (Skills), o melhor do livro, tem um ponto cego:** governança de Skills (aprovação, descontinuação, teste) ausente — paradoxal num capítulo de Responsabilidade Indelegável.
- **C01 (Executivos)** menciona Briefing/Research/Voice como se o leitor já soubesse o que são — depende de capítulos que vêm depois; precisa de mecânica e analogia próprias.

---

## 5. ROADMAP DE UPGRADE (em passes, não capítulo a capítulo)

| Passe | O quê | Alcance | Natureza |
|---|---|---|---|
| **P1 — Camada Viva** | Varrer os 19; todo número/tier/versão perecível → ponteiro ao Apêndice Vivo (J) | 19 caps | semi-mecânico, **altíssimo ROI de durabilidade** |
| **P2 — Decisão + Invariante** | Adicionar "quando evitar" e devolver o Invariante ao corpo (callback estrutural) em cada cap | 19 caps | editorial |
| **P3 — Exercícios** | Padronizar exercícios/autoavaliação acionáveis no padrão L1 | foco em C01, C17 + declarativos | editorial |
| **P4 — Pontuais** | C19/C19b fronteira; C15/C16 falsa confiança; C30 governança de Skills | 4–5 caps | cirúrgico |
| **P5 — Reescrita dos 5 mais fracos** | C01, C10, C12, C17, C19 ganham profundidade/mecânica | 5 caps | redação |

**Sequência recomendada:** P1 primeiro (protege contra envelhecimento e é o mais rápido) → P2 (eleva a média e mata o "manual de botão") → P3/P4 → P5.

> **Nota de método:** P1 e P2 aplicados aos 19 já levam a média de ~6,2 para a faixa 7,5–8. Os 5 mais fracos (P5) são os que exigem redação real. Tudo deve passar por nova banca antes de "pronto", como no L1.

---

*Próximo: executar P1 (Camada Viva) — o passe de maior retorno e menor risco.*
