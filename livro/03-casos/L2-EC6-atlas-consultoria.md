# EC6 — ATLAS STRATEGY
## Knowledge cells por cliente com Projects + Skills

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em consultorias estratégicas brasileiras durante adoção de IA em produção de entregáveis entre 2025 e 2026; números são realistas mas não identificam empresa específica. Cenário expandido a partir do exemplo memorável apresentado no Cap 39.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | Consultoria estratégica BR |
| **Tamanho** | ~120 consultores, 18 sócios |
| **Tickets típicos** | R$ 200 mil a R$ 1,5 milhão por engajamento |
| **Problema central** | Conhecimento por cliente disperso em PowerPoints; rotatividade de consultores cria reinício constante |
| **Invariantes** | 3, 9 |
| **Frameworks** | F4 PROMPT-EXT, F8 EVAL-PIRÂMIDE, F9 ROTA-DUPLA |

## 2. PROBLEMA

Conhecimento por cliente disperso em PowerPoints espalhados em SharePoint. Rotatividade de consultores (taxa de 18%/ano) cria reinício constante. Partner gasta tempo recontextualizando equipe nova a cada movimento. Tempo de relatório mensal: 18h por consultor.

## 3. TESE — Knowledge Cell por cliente

Criar uma "knowledge cell" por cliente em Claude Projects, com Skills específicas por tipo de output (relatório mensal, deck executivo, análise de mercado, briefing de partner), e governança rígida de confidencialidade.

## 4. ARQUITETURA — Projects + Skills

- **Claude Projects** por cliente (1 Project = 1 cliente ativo)
- **Skills** por tipo de output (5 Skills proprietárias da Atlas)
- **Ingestão controlada** de materiais (apenas materiais aprovados pelo partner)
- **Uso individual** + uso de partner como auditor

## 5. SKILLS PROPRIETÁRIAS

| Skill | Função |
|-------|--------|
| Relatório mensal — padrão Atlas | Voz autoral, estrutura, voz de tabela canônica |
| Deck executivo — 10 slides | Storytelling padrão Atlas |
| Análise SWOT estruturada | Framework próprio com 4 quadrantes calibrados |
| Memo para o board | Padrão de 1 página, com decisão pedida |
| Q&A para a diretoria do cliente | Roteiro de antecipação de objeções |

## 6. GOVERNANÇA F6 — Camada Operacional Forte

- NDA por cliente embutida na política de uso
- Isolamento por Project (tenant isolation a nível Claude)
- Auditoria de quem acessou o quê
- Política de saída de consultor (revogação imediata de acesso aos Projects ativos)
- Comitê de qualidade quinzenal

## 7. EVALS (F8) — A LIÇÃO APRENDIDA

Caso aprendido no Cap 39: regressão silenciosa de números trocados em relatório por mudanças sucessivas de prompt sem golden set. A Atlas implementou após o incidente:

**Base.** Schema validation do relatório (seções obrigatórias, números formatados, citação presente).
**Meio.** Golden set de **80 relatórios reais** com gabarito de números e tese. LLM-as-judge com rubrica de faithfulness numérico (4 critérios). Juiz = Opus; gerador = Sonnet. Calibrado contra 3 sócios em 30 itens, correlação 0,82.
**Topo.** Auditoria semanal de partner em release crítico. Trimestral por consultor externo.
**Adversarial.** 30 casos: sycophancy (cliente forçando conclusão), prompt injection via dado, números invertidos sutilmente, citação de fonte inexistente, omissão de risco crítico.
**Política de bloqueio:** faithfulness numérico delta máximo 1 ponto contra baseline.

## 8. LLMOPS

- Tracing por Project
- Versionamento de Skills
- Canário por consultor antes de virar padrão de área
- Rollback rápido de Skill problemática

## 9. MÉTRICAS

| Métrica | Pré-projeto | Resultado em 6 meses |
|---------|-------------|------------------------|
| Tempo de relatório mensal | 18h | 7h por consultor |
| Consistência de voz (LLM-as-judge) | baseline | +31% |
| Tempo de onboarding de consultor a um cliente | 14 dias | 4 dias |
| Capacidade adicional sem nova contratação | baseline | +22% |

## 10. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Vazamento entre clientes | Isolamento técnico; auditoria; revogação imediata em saída |
| Perda de voz autoral | Eval de voz contínuo via LLM-as-judge |
| Dependência da knowledge cell para tomada de decisão | Treinamento: "Skill é rascunho, não autoridade" |
| Inflação de uso (consultor pula a etapa de pensamento próprio) | Auditoria amostral por partner; cultura de "submetemos pensamento, IA refina" |

## 11. LIÇÃO ESTRUTURAL

*Em consultoria, Skills + Projects bem governados transformam conhecimento tácito em ativo escalável. Sem governança, transformam conhecimento confidencial em risco contratual. A Camada Dupla (Inv. 3) aplicada: Skill captura o método (padrão durável); a execução do dia consome a Skill como referência (número volátil).*

## 12. CONEXÕES

- 🔗 [Manifesto](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Inv. 3, 9)
- 🔗 Frameworks: [F4](../../Livro-1-Os-Invariantes/03-frameworks/L1-F4-prompt-ext.md), [F8](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md), [F9](../../Livro-1-Os-Invariantes/03-frameworks/L1-F9-rota-dupla.md)
- 🔗 Caps: [9 Engenharia Prompt](../../Livro-1-Os-Invariantes/02-capitulos/L1-C09-engenharia-prompt.md), [39 Evals](../../Livro-1-Os-Invariantes/02-capitulos/L1-C39-evals.md), [42 Governança](../../Livro-1-Os-Invariantes/02-capitulos/L1-C42-governanca.md)
- 🔗 Claude: [Cap 20 Projects](../02-capitulos/L2-C21-projects.md), [Cap 31 Skills](../02-capitulos/L2-C32-skills.md)

---

> *"Skill captura o método. Projects organizam o cliente. Eval impede o método de se corromper. Sem os três, conhecimento confidencial vira risco contratual."*
