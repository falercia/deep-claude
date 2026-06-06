# P-SAAS-CLAUDE-01 — Suporte SaaS Tier 1 com escalonamento

> Prompt profissional para suporte automatizado de Tier 1 com escalonamento estruturado.
> Calibrado para SaaS B2B brasileiro.
> Versão 1.0 — 2026-07

---

## Quando usar

- Resposta automatizada de Tier 1 em suporte SaaS
- Triagem de tickets com classificação e priorização
- Apoio a agentes humanos em casos de Tier 2/3 (síntese de histórico)
- Geração de KBs (knowledge base) a partir de interações

## Quando NÃO usar

- **Casos enterprise com SLA crítico** sem revisão humana
- **Cobrança e financeiro** (escalonar para humano sempre)
- **Reclamações formais com indicação de Reclame Aqui ou Procon** (escalonar)
- **Pedido de cancelamento** (escalonar para retenção/sucesso)

## Estrutura

Output em 4 seções:

1. **Resposta ao cliente** (tom da casa, máximo 4 parágrafos)
2. **Classificação interna** (categoria, urgência, complexidade)
3. **Próximo passo** (resolvido / encaminhar Tier 2 / encaminhar Tier 3 / produto)
4. **Sinalizações para o time** (insights, padrões observados)

## Modelo e configuração

| Parâmetro | Valor |
|---|---|
| Modelo | Claude Haiku (versão corrente) |
| Temperature | 0.3 |
| Max output | 1500 |
| Custo otimizado | Sim |

## Conexão com o livro

- **Cap 24 — Engenharia de Prompt**
- **Cap 39 — Casos SaaS + Suporte**: contexto completo

Ver [`changelog.md`](./changelog.md).
