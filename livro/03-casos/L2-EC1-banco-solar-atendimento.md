# EC1 — BANCO SOLAR
## Atendimento humano → agente híbrido com governança

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em fintechs brasileiras com produto de cartão de crédito e conta de pagamento entre 2024 e 2026; números são realistas mas não identificam empresa específica.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | Fintech BR (cartão + conta de pagamento) |
| **Tamanho** | ~450 colaboradores, 2,1 milhões de clientes ativos |
| **Maturidade IA** | Início — sem programa estruturado de IA antes do projeto |
| **NPS pré-projeto** | 58 |
| **Custo de atendimento pré-projeto** | R$ 18,40 por contato |
| **Volume de tickets** | Crescimento de 40% a/a |
| **Backlog médio** | 14h horário comercial · 36h fora |
| **Turnover Nível 1** | >70%/ano |
| **Invariantes ilustrados** | 6 (Autonomia Proporcional), 7 (Termômetro), 8 (Responsabilidade Indelegável) |
| **Frameworks aplicados** | F1 DECID-IA, F3 AGENTE-PROP, F6 GOV-INDELEGÁVEL, F7 COMPOSTO-3T, F8 EVAL-PIRÂMIDE |

---

## 2. PROBLEMA

Volume de tickets em crescimento sustentado. CSAT em declínio (4,1 → 3,8 em 18 meses). Backlog crescente em horário comercial; cliente em conta digital espera 14h por resposta em ticket simples. Turnover de atendentes de Nível 1 acima de 70% ao ano, com custo de recrutamento e treinamento corroendo margem. A diretoria recebeu três propostas de fornecedor — duas de chatbot tradicional, uma de "agente full autônomo" — e quer entender qual seguir.

---

## 3. TESE INICIAL ERRADA

Substituir Nível 1 inteiro por chatbot LLM "porque a IA agora consegue". A proposta tinha três falhas que violam Invariantes do livro.

- **Viola Inv. 8 (Responsabilidade Indelegável):** "agente full autônomo" sem governança nem RACI assinado deixa accountability indefinida quando der ruim.
- **Viola Inv. 7 (Termômetro):** sem golden set para mostrar que o agente entrega qualidade equivalente em todas as classes, "vamos confiar no modelo" é fé.
- **Viola Inv. 6 (Autonomia Proporcional):** delegação total sem observabilidade nem rollback equivale a soltar o agente sem rede.

O CTO aplicou o **F1 DECID-IA** e parou a iniciativa nesse formato. Reformulou.

---

## 4. ARQUITETURA ESCOLHIDA — Agente híbrido por tier de risco (F3 AGENTE-PROP)

A arquitetura é híbrida, com classificação prévia de risco que decide nível de autonomia por categoria de ticket.

| Tier de risco | Volume | Tipo de ticket | Nível de autonomia (F3) |
|---------------|--------|----------------|-------------------------|
| **Tier 1 — Baixa criticidade** | ~50% | Informacional, segunda via, status, dúvida de uso | **Agente supervisionado** com tracing online; resolve ou escala |
| **Tier 2 — Média criticidade** | ~25% | Dúvida sobre cobrança, pedido de limite, alteração cadastral | **Co-piloto assíncrono**: agente prepara resposta, humano valida em até 4h |
| **Tier 3 — Alta criticidade** | ~15% | Fraude, contestação, jurídico, vulnerabilidade financeira | **Assistente** apenas: humano sempre, agente gera sumário pré-atendimento |
| **Tier 4 — Crítica** | ~10% | Pedido de cancelamento de cartão por roubo, ameaça à pessoa, denúncia regulatória | Roteamento direto ao humano, sem agente; sumário de contexto opcional |

A **classificação** por tier é feita por um classificador Haiku-like na entrada, com regras de roteamento explícitas (regex + intent classification). O classificador é instrumentado com tracing e tem golden set próprio para detectar regressão.

---

## 5. WORKFLOW

```
Cliente abre ticket → classificador (Haiku) atribui tier
       ↓
   ┌───────────────┬───────────────┬───────────────┬───────────────┐
   │   Tier 1      │   Tier 2      │   Tier 3      │   Tier 4      │
   │ Agente Sonnet │ Sonnet prepara│ Sumário p/    │ Humano direto │
   │ + MCP core    │ + humano      │ humano sênior │ + sumário     │
   │ resolve       │ valida em 4h  │ decide        │ (opcional)    │
   │ ou escala     │               │               │               │
   └───────┬───────┴───────┬───────┴───────┬───────┴───────────────┘
           ↓               ↓               ↓
       Resposta        Resposta        Resposta
       imediata        em 4h           humana
```

Em qualquer tier, **escalação para humano preserva contexto completo** (toda a sessão com tracing, sumário do agente, justificativa de escalação).

---

## 6. MCP — Tools privadas internas

| Tool | Tier autorizado | Permissão | Auditoria |
|------|-----------------|-----------|-----------|
| `consulta_conta` | 1, 2, 3 | Read | Span por chamada, retenção 5 anos |
| `gera_segunda_via` | 1, 2 | Write (idempotente) | Span + assinatura no sistema bancário |
| `consulta_limite` | 1, 2, 3 | Read | Span por chamada |
| `solicita_revisao_limite` | 2 | Write (compensável) | Span + aprovação humana obrigatória |
| `abre_contestacao_minor` | 2, 3 | Write (compensável) | Span + revisão humana antes de execução |
| `escala_para_humano` | Todos | Read + sinal | Span |
| `consulta_historico` | 1, 2, 3 | Read | Span + classificação de PII |

Aplicação do **F5 MCP-COBERTURA**: tools internas do core bancário ficam no **Quadrante D** (sem padrão, dados sensíveis) — MCP próprio com auditoria completa, dono nominal (Diretor de Tecnologia + DPO + Compliance), retenção de log por 5 anos para qualquer chamada que afete saldo, transação ou contestação.

---

## 7. AGENTES (subagents e workflows)

| Agente | Modelo | Função |
|--------|--------|--------|
| Triagem | Haiku | Classifica tier; nunca toca tools |
| Resolutor T1 | Sonnet | Resolve ticket de baixa criticidade com tools permitidas |
| Co-piloto T2 | Sonnet | Prepara resposta para revisão humana |
| Sumarizador para humano | Sonnet | Produz contexto para humano antes de atendimento |

**Coordenação é determinística**, não baseada em LLM. O coordenador é código simples que roteia conforme o tier classificado.

---

## 8. GOVERNANÇA (F6 GOV-INDELEGÁVEL)

| Camada | Item | Dono |
|--------|------|------|
| Técnica | Tracing OpenTelemetry GenAI; rollback testado mensal; kill switch por tool em 30s; eval em CI; auditoria imutável | CTO + Tech Lead de IA |
| Operacional | RACI assinado pela diretoria; AUP em 4 páginas; runbook de incidente SEV-1 com SLA 15min; treinamento de atendentes | Diretor de Atendimento + DPO |
| Executiva | AI Council mensal; comitê de revisão semanal de incidentes; comunicação trimestral com Conselho | CEO + diretoria |

**Retenção:** 5 anos para qualquer ticket com efeito financeiro ou jurídico (alinhado à LGPD art. 20 e regulação BACEN).

---

## 9. EVALS (F8 EVAL-PIRÂMIDE)

**Base (100%).** Schema validation da resposta (formato pt-BR, sem expressão coloquial, com call-to-action quando aplicável). Validação estrutural de tool call.

**Meio.** Golden set de **600 tickets reais** com gabarito de resolução, anotado por 4 supervisores em sessões dedicadas. LLM-as-judge com rubrica de 5 critérios (clareza, completude, faithfulness em dados financeiros, tom adequado, recomendação correta de escalonamento). Juiz = Opus; gerador = Sonnet. Calibração contra os 4 supervisores em 80 itens, correlação 0,79.

**Topo (10% por sample).** Auditoria semanal por supervisor sênior em release crítico. Auditoria mensal por consultor externo de qualidade de atendimento.

**Adversarial (mensal).** 120 casos com: jailbreak via input do cliente; sycophancy contra cliente bravo; indução a fraude (cliente fingindo ser titular); pedido de quebra de sigilo; over-refusal frustrando cliente legítimo; vazamento de PII em sumário.

**Política de bloqueio em CI.** Faithfulness em dados financeiros ≥0,98 (delta máximo 0,5 pontos contra baseline). Adversarial: zero passagens em itens críticos.

---

## 10. LLMOPS (F3 + 7 PILARES)

| Pilar | Implementação |
|-------|---------------|
| 1 Tracing | OpenTelemetry GenAI semantic conventions; cobertura 100% das chamadas |
| 2 Versionamento | Prompt em registry com PR + revisão obrigatória + eval em CI; tool registry com schema versionado |
| 3 Deploy progressivo | Shadow mode → canário 1% → 10% → 50% → 100%; canário por segmento (clientes free antes de PJ enterprise) |
| 4 Rollback | Botão único por feature; teste mensal em staging; MTTR alvo 15min para SEV-1 |
| 5 Custos | Circuit breaker de R$ 0,40 por contato como limite duro; atribuição por feature, cliente, atendente; alerta em 80% do envelope |
| 6 Segurança | Sanitização rígida de input; allowlist de tools por tier; classificação prévia de prompt injection; kill switch por tool em 30s |
| 7 Governança | SEV-1 com runbook testado; postmortem público em 5 dias; retenção 5 anos para casos financeiros |

---

## 11. MÉTRICAS-ALVO (12 MESES)

| Métrica | Pré-projeto | Meta 12 meses |
|---------|-------------|----------------|
| Custo por contato | R$ 18,40 | R$ 6,80 |
| CSAT | 3,8 | 4,4 |
| Backlog horário comercial | 14h | 1h |
| Escalação para humano | 100% | 22% dos contatos |
| Tempo médio de resposta T1 | 14h | <2min |
| SEV-1 críticos | — | ≤2/ano |
| Turnover de atendentes | 70% | 40% (atendimento vira menos exaustivo) |

---

## 12. ROI CENÁRIO

- **Economia anualizada estimada** ~R$ 38 milhões em custo de atendimento (cenário otimista descontando investimento de R$ 6 milhões em ano 1, com governança e LLMOps embutidos)
- **Payback** em 6 meses
- **Externalidades positivas:** retenção de cliente em ticket simples, redução de churn por atrito de atendimento, melhoria de NPS, redução de custo de recrutamento e treinamento de atendentes

---

## 13. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Sycophancy diante de cliente bravo (concorda para evitar conflito) | Adversarial set específico de sycophancy bancário; calibração de recusas com supervisores |
| Prompt injection via campo livre | Sanitização rígida + allowlist de tools por tier + classificador de input suspeito |
| Alucinação de saldo (zero tolerância) | Saldo nunca é gerado pelo modelo; sempre via tool `consulta_conta` com retorno literal |
| Over-refusal frustrando cliente legítimo | Eval de over-refusal mensal; ajuste fino do system prompt; gate de bloqueio |
| Vazamento de PII em logs | Classificador automático de PII no pipeline de logging; sanitização antes de span |
| Dependência de vendor (lock-in) | Modelo alternativo (Claude + um secundário) em fallback documentado |
| Decisão automatizada com efeito jurídico (LGPD art. 20) | Tier 4 sempre humano; Tier 3 com sumário, humano decide; auditoria 5 anos |

---

## 14. LIÇÃO ESTRUTURAL

*O agente híbrido por tier de risco é quase sempre melhor que o agente único "que faz tudo". O ganho não vem do modelo mais caro, vem do roteamento certo. Inv. 6 (autonomia proporcional ao tier) + Inv. 7 (eval por classe) + Inv. 8 (responsabilidade nominal por tier) sustentam a operação. Sem os três, fica pilha de boas intenções.*

---

## 15. CONEXÕES

- 🔗 **Manifesto:** [Cap 00M](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Invariantes 6, 7, 8)
- 🔗 **Frameworks:** [F1](../../Livro-1-Os-Invariantes/03-frameworks/L1-F1-decid-ia.md), [F3](../../Livro-1-Os-Invariantes/03-frameworks/L1-F3-agente-prop.md), [F5](../../Livro-1-Os-Invariantes/03-frameworks/L1-F5-mcp-cobertura.md), [F6](../../Livro-1-Os-Invariantes/03-frameworks/L1-F6-gov-indelegavel.md), [F7](../../Livro-1-Os-Invariantes/03-frameworks/L1-F7-composto-3t.md), [F8](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md)
- 🔗 **Capítulos-âncora:** [Cap 12 Agentes](../../Livro-1-Os-Invariantes/02-capitulos/L1-C12-agentes.md), [Cap 13 MCP](../../Livro-1-Os-Invariantes/02-capitulos/L1-C13-mcp.md), [Cap 39 Evals](../../Livro-1-Os-Invariantes/02-capitulos/L1-C39-evals.md), [Cap 40 LLMOps](../../Livro-1-Os-Invariantes/02-capitulos/L1-C40-llmops.md), [Cap 42 Governança](../../Livro-1-Os-Invariantes/02-capitulos/L1-C42-governanca.md)
- 🔗 **Aplicação Claude:** [Cap 32 (L2) Subagents e Workflows](../02-capitulos/L2-C33-subagents-workflows.md), [Cap 33 (L2) Claude + MCP](../02-capitulos/L2-C34-claude-mcp.md), [Cap 30 (L2) Enterprise](../02-capitulos/L2-C31-enterprise.md)

---

> *"Modelo certo, roteamento certo, governança certa, dono certo. Sem qualquer uma das quatro, vira incidente disfarçado de produto."*
