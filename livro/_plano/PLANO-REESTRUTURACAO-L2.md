# Plano de reestruturação — Livro 2 · Deep Claude

**Data:** 2026-06-17 · Diagnóstico + plano de ação. **Nada renomeado ainda** — aguarda sua aprovação.

---

## 1. O DIAGNÓSTICO EM UMA FRASE

Os arquivos de capítulo estão numerados **C17–C34b** (resíduo de quando L1+L2 eram uma obra contínua), mas o **sumário canônico do próprio L2** define **46 capítulos numerados 1–46**. Os arquivos ficaram presos no mapa velho; o sumário é o mapa novo. Além disso, o L2 está **~45% redigido** (19 de 46 capítulos) e tem **paratexto duplicado**.

A régua para corrigir já existe: é o `L2-PT-04-sumario.md`, que o autor já escreveu. O trabalho é **reconciliar os arquivos a esse mapa** e tornar visível o que falta.

---

## 2. MAPA CANÔNICO (fonte: L2-PT-04-sumario.md)

**46 capítulos · 5 partes.** Parte 1 Fundamentos (1–7) · Parte 2 Ecossistema (8–20) · Parte 3 Engenharia (21–35) · Parte 4 Aplicação Executiva (36–44) · Parte 5 Continuidade (45–46).

---

## 3. MAPEAMENTO: arquivo atual → capítulo canônico

| Arquivo atual | Cap. no arquivo | Conteúdo | Cap. CANÔNICO | Parte | Nota |
|---|---|---|---|---|---|
| L2-C17-entendendo-claude | 17 | Entendendo Claude/Anthropic — porta de entrada | **2** (Claude 101) | 1 | abre a Parte; conferir vs cap 1 |
| L2-C34-executivos | 34 | Claude para Executivos (Inv 8+9) | **1** (AI Fluency Exec.) | 1 | ambíguo — ver §6 |
| L2-C18-modelos-claude | 18 | Todos os modelos + Opus/Sonnet/Haiku | **4 (+5)** | 1 | pode cobrir caps 4 e 5 |
| L2-C24-claude-code | 24 | Claude Code | **9** | 2 | |
| L2-C19-claude-web | 19 | Claude Web | **10** | 2 | |
| L2-C25-desktop | 25 | Claude Desktop | **11** | 2 | |
| L2-C26-mobile | 26 | Claude Mobile | **12** | 2 | |
| L2-C20-projects | 20 | Claude Projects | **13** | 2 | |
| L2-C21-artifacts | 21 | Claude Artifacts | **14** | 2 | |
| L2-C22-research | 22 | Claude Research | **15** | 2 | |
| L2-C23-web-search | 23 | Claude Web Search | **16** | 2 | |
| L2-C27-voice | 27 | Claude Voice | **17** | 2 | |
| L2-C28-scheduled-tasks | 28 | Scheduled Tasks | **18** | 2 | |
| L2-C29-team | 29 | Claude Team | **19** | 2 | fundir com C30 OU split 19→19/19b |
| L2-C30-enterprise | 30 | Claude Enterprise | **19** | 2 | idem |
| L2-C34b-connectors… | 34b | Connectors, Dispatch, Routines | **20** | 2 | |
| L2-C33-claude-mcp | 33 | MCP | **28 ou 29** | 3 | sumário tem MCP Fundamentos (28) + Avançado (29) |
| L2-C31-skills | 31 | Claude Skills | **30** | 3 | |
| L2-C32-subagents-workflows | 32 | Subagents + workflows | **31** | 3 | |

**Casos (pasta 03-casos) → Parte 4 (36–40), por setor:**

| Arquivo | Empresa / setor | Cap. canônico |
|---|---|---|
| L2-EC3-vianna-castro-juridico | Jurídico (M&A) | **36** Jurídico |
| — *(sem caso)* | Saúde | **37** Saúde — **LACUNA** |
| L2-EC1-banco-solar-atendimento | Fintech BR | **38** Financeiro |
| L2-EC4-metrica-io-copiloto + L2-EC5-entertech-prevendas | SaaS B2B / vendor | **39** SaaS+Suporte |
| L2-EC2-redecasa-rh + L2-EC7-instituto-norte-educacao | RH / Educação | **40** RH+Mkt+Edu |
| L2-EC6-atlas-consultoria | Consultoria estratégica | **órfão** — não há setor "consultoria" nos caps 36–40 |

**Apêndice Vivo:** `04-apendices/L2-APX-J-apendice-vivo.md` → **Cap. 45**.

---

## 4. LACUNAS — o que falta redigir (≈25 capítulos)

- **Parte 1:** 1 AI Fluency*, 3 Anatomia da Conversa, 5 Opus/Sonnet/Haiku*, 6 Refresher Tokens, 7 Personas. *(podem já estar embutidos em C17/C18/C34 — verificar.)*
- **Parte 2:** **8 Claude Cowork** (não há arquivo).
- **Parte 3 (a mais incompleta):** 21 API+SDKs, 22 Tool Use, 23 Extended Thinking, 24 Prompt Avançado, 25 Caching, 26 Embeddings, 27 RAG, **28/29 MCP** (1 dos 2 existe), 32 Computer Use, 33 Vision, 34 Evaluations, 35 LLMOps.
- **Parte 4:** 37 caso Saúde, 41 Governança Executiva, 42 Adoção Institucional, 43 ROI/Métricas, 44 Segurança/LGPD.
- **Parte 5:** 46 Repositório Acompanhante.

> Em números: **19 redigidos · ~25 a redigir · ~3 a fundir/dividir.** O L2 está a ~45% do plano.

---

## 5. OUTRAS INCONSISTÊNCIAS (além da numeração)

1. **Paratexto duplicado.** Dois sumários (`L2-02-sumario` = visão de partes; `L2-PT-04-sumario` = detalhado/canônico) e dois esquemas de prefixo (`L2-00/01/02` vs `L2-PT-01..06`). Consolidar em UM esquema.
2. **Casos por empresa vs por setor.** Há 7 casos-empresa (EC1–7) para 5 capítulos-setor (36–40). Falta Saúde; sobra Consultoria (EC6). Decidir: agrupar empresas por setor dentro de cada capítulo, ou mudar a grade de setores.
3. **Terminologia antiga.** O sumário ainda rotula "P9 — Operador" (Princípio). Após o rebrand do L1, o L2 precisa da mesma migração **Princípio → Invariante** (os capítulos já usam "Invariante" no corpo — ex.: C34 diz "Invariante 8"; o sumário não).

---

## 6. DECISÕES QUE PRECISO DE VOCÊ

- **D-A — C34-"executivos":** é o Cap 1 (AI Fluency Executiva) reposicionado, ou um capítulo executivo da Parte 4? Define onde ele entra.
- **D-B — Team/Enterprise:** um capítulo único (cap 19) ou dois (19 Team / 19b Enterprise)? Hoje são 2 arquivos.
- **D-C — Caso Consultoria (EC6):** vira parte de algum capítulo-setor, ganha setor próprio, ou sai?
- **D-D — Momento da renumeração:** renumerar os 19 arquivos para o esquema canônico **agora** (resolve os "números estranhos" já e fixa os slots), ou **só depois** de redigir mais capítulos? *(Recomendo agora: o mapa não muda, e parar de conviver com C17–C34b reduz erro em todo trabalho futuro.)*

---

## 7. SEQUÊNCIA RECOMENDADA

1. **Você decide D-A a D-D** (rápido).
2. **Renumerar os 19 arquivos** para o canônico (1–46), atualizando H1 interno, nome de arquivo e referências cruzadas — com backup, como no L1.
3. **Consolidar o paratexto** (um sumário canônico, um esquema de prefixo) e **migrar Princípio→Invariante** no sumário.
4. **Reconciliar os casos** (EC → 36–40) conforme D-C.
5. **Congelar o mapa de lacunas** como backlog de redação (ordem sugerida: fechar Parte 2 com Cowork → Parte 1 → Parte 3 → Parte 4 executiva).
6. *(Depois)* Banca editorial dos capítulos já redigidos, no padrão do L1.

---

*Aprovado o plano, executo do passo 2 em diante. Backup antes de qualquer renomeação.*
