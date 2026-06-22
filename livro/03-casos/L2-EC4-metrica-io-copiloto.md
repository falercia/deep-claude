# EC4 — MÉTRICA.IO
## Copiloto in-product com eval contínuo

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em SaaS B2B brasileiros de BI durante adoção de copilotos in-product entre 2024 e 2026; números são realistas mas não identificam empresa específica.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | SaaS B2B (BI para mid-market) |
| **Tamanho** | ~70 colaboradores, ~480 contas pagantes |
| **ARR** | R$ 32 milhões |
| **Maturidade IA** | Médio — uso interno em código (Claude Code) antes do copiloto |
| **Problema central** | Adoção baixa de features avançadas; CAC alto; expansão lenta |
| **Invariantes ilustrados** | 6, 7 |
| **Frameworks** | F3 AGENTE-PROP, F7 COMPOSTO-3T, F8 EVAL-PIRÂMIDE |

## 2. PROBLEMA

Adoção de features avançadas baixa (apenas 32% das contas usam mais que 3 features). CS gasta horas/semana respondendo "como faço X". CAC alto, NRR estagnado em 108%. Diretoria quer alavanca de retenção e expansão.

## 3. TESE — Copiloto in-product

Implementar copiloto que (a) responda dúvidas com base na documentação, (b) gere consultas SQL e dashboards a partir de linguagem natural, (c) sugira insights baseados nos dados da própria conta.

## 4. ARQUITETURA — RAG + agente read-only

- **RAG** sobre documentação (chunking por seção)
- **Agente com tools de query** (read-only por padrão; escrita só com confirmação humana)
- **Sub-agente de explicação** para resultado de query
- **Sandbox por conta** (zero cross-tenant)

## 5. MCP — Tools privadas

| Tool | Permissão | Auditoria |
|------|-----------|-----------|
| `busca_documentacao` | Read | Span |
| `executa_query_read_only` | Read (sandbox por conta) | Span + query gerada |
| `gera_visualizacao` | Write (visualização efêmera) | Span |
| `explica_resultado` | Read | Span |
| `salva_dashboard_proposto` | Write (com confirmação humana) | Span + usuário confirmador |

## 6. AGENTES

| Agente | Modelo | Função |
|--------|--------|--------|
| Triagem | Haiku | Decide rota (docs vs dados) |
| RAG sobre docs | Sonnet | Responde dúvida com base em documentação |
| Query writer | Sonnet com prompt extra para SQL seguro | Escreve query read-only |
| Explicador | Sonnet | Explica resultado |

**Coordenação determinística** (não-LLM).

## 7. GOVERNANÇA F6

- Sandbox por conta (tenant isolation a nível de tool)
- Read-only por padrão; write apenas com confirmação humana
- Consentimento explícito de coleta de telemetria de uso do copiloto
- Auditoria de queries geradas (mensal pelo CS Ops)
- Comitê de produto + segurança quinzenal

## 8. EVALS (F8 com loop em produção)

**Base.** Schema validation de SQL (não-destrutivo, parseável, com LIMIT).
**Meio.** Golden set de **250 perguntas reais** por categoria (docs, query, insight). LLM-as-judge calibrado para faithfulness em explicação numérica.
**Adversarial.** Injection via nome de tabela/coluna; tentativas de cross-tenant; jailbreak via dado da conta.

**Eval em produção (loop fechado):** thumbs up/down explícito; abandono de query; retentativa do usuário. Casos com sinal negativo entram no próximo ciclo de golden set.

## 9. LLMOPS

- Tracing por sessão e por conta
- Canário por % de contas (free → paid → enterprise)
- Rollback de prompt em segundos
- Quota por conta para circuit breaker
- Custos atribuídos por conta (precificação correta + sinal de adoção)

## 10. MÉTRICAS

| Métrica | Pré-copiloto | Resultado |
|---------|--------------|-----------|
| Adoção de features avançadas | 32% | 71% (+39 pp) |
| Tempo até primeiro insight | 14 dias | 4 dias |
| Tickets de CS "como faço X" | baseline | -57% |
| NRR projetado | 108% | 124% (-> meta) |

## 11. ROI

- Custo do copiloto absorvido em melhoria de NRR e redução de churn
- Payback em 7 meses
- Custo por conta atribuído permite cobrar add-on premium em planos enterprise

## 12. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Injection via dado da conta | Sanitização + schema validation antes de execução |
| Vazamento cross-tenant | Tenant isolation a nível de tool; teste mensal |
| Alucinação numérica | Eval específico de faithfulness; resultado vem de query, não do modelo |
| Dependência operacional do copiloto | Fallback gracioso para UI normal |

## 13. LIÇÃO ESTRUTURAL

*Copiloto que aprende com o uso real é o único que melhora. Sem eval em produção fechando o loop com o golden set, copiloto vira gadget que envelhece junto com o release.*

## 14. CONEXÕES

- 🔗 [Manifesto](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Inv. 6, 7)
- 🔗 Frameworks: [F3](../../Livro-1-Os-Invariantes/03-frameworks/L1-F3-agente-prop.md), [F7](../../Livro-1-Os-Invariantes/03-frameworks/L1-F7-composto-3t.md), [F8](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md)
- 🔗 Caps: [12 Agentes](../../Livro-1-Os-Invariantes/02-capitulos/L1-C12-agentes.md), [13 MCP](../../Livro-1-Os-Invariantes/02-capitulos/L1-C13-mcp.md), [39 Evals](../../Livro-1-Os-Invariantes/02-capitulos/L1-C39-evals.md), [40 LLMOps](../../Livro-1-Os-Invariantes/02-capitulos/L1-C40-llmops.md)
- 🔗 Claude: [Cap 21 Artifacts](../02-capitulos/L2-C22-artifacts.md), [Cap 32 Subagents](../02-capitulos/L2-C33-subagents-workflows.md), [Cap 33 MCP](../02-capitulos/L2-C34-claude-mcp.md)

---

> *"Copiloto sem eval em produção é gadget. Com eval contínuo fechando o loop, vira alavanca de retenção."*
