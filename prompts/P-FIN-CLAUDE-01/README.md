# P-FIN-CLAUDE-01 — Análise de crédito estruturada

> Prompt profissional para análise de crédito com Claude.
> Calibrado para regras BACEN e CVM, com soberania de dados via Bedrock SP.
> Versão 1.0 — 2026-07

---

## Quando usar

- Apoio à análise de crédito PJ (small/medium business)
- Triagem inicial de propostas para revisão humana
- Apoio a comitê de crédito (síntese de dossiês)
- Auditoria de carteira (revisão de exposições)

Prompt opera sob princípio "analista-no-loop": decisão de crédito final é humana. Claude apoia organização e síntese.

## Quando NÃO usar

- **Decisão automatizada sem revisão humana.** LGPD Art. 20 dá direito à revisão humana em decisões com impacto. Recusa de crédito automatizada vira passivo regulatório.
- **Pessoa física com dados sensíveis.** Dados de saúde, raça, orientação não podem ser usados em scoring (LGPD Art. 11 + jurisprudência BACEN).
- **Operação com soberania não-garantida.** Dados financeiros corporativos exigem Bedrock SP.

## Fundamentação regulatória

| Norma | Aplicação |
|---|---|
| **Resolução BACEN sobre IA** (atualizada anualmente, ver Apêndice Vivo) | Uso de IA em instituições financeiras |
| **LGPD Art. 20** | Direito à revisão humana em decisões automatizadas |
| **LGPD Art. 11** | Dados sensíveis vedados em scoring |
| **CVM (quando aplicável)** | Para operações com valores mobiliários |
| **Lei Cadastro Positivo** (12.414/11) | Uso de informações de crédito |

## Estrutura do prompt

Output em 5 seções:

1. **Síntese para comitê** (3-5 frases, recomendação direcional)
2. **Capacidade de pagamento** (capacidade analisada vs solicitada)
3. **Riscos identificados** (com classificação alto/médio/baixo)
4. **Pontos de mitigação sugeridos** (garantias, covenants, prazos)
5. **Disclaimer obrigatório** (revisão humana obrigatória)

## Modelo e configuração

| Parâmetro | Valor |
|---|---|
| Modelo | Claude Sonnet (versão corrente) |
| Soberania | **Obrigatória: Bedrock SP** |
| Temperature | 0.0 (determinístico) |
| Max output | 2500 |

## Conexão com o livro

- **Cap 38 — Casos Financeiros**: contexto regulatório completo
- **Cap 44 — LGPD e soberania**: dados financeiros sensíveis

Ver [`changelog.md`](./changelog.md).
