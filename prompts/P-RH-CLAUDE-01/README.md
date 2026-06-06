# P-RH-CLAUDE-01 — Triagem de currículo com mitigação de viés

> Prompt profissional para triagem inicial de currículos com mitigação ativa de viés.
> Calibrado para o contexto brasileiro de RH e LGPD.
> Versão 1.0 — 2026-07

---

## Quando usar

- Triagem inicial de currículos em volumes médios/altos
- Apoio a recrutadores na priorização de candidatos
- Identificação de match entre vaga e perfil técnico
- Auditoria de processos seletivos (revisão de critérios)

## Quando NÃO usar

- **Decisão final de contratação automatizada.** LGPD Art. 20 dá direito à revisão humana.
- **Uso de variáveis protegidas em scoring.** Idade, raça, gênero, religião, orientação, deficiência, estado civil NUNCA entram em scoring (CF Art. 5, LGPD Art. 11).
- **Sem auditoria de viés.** Processo seletivo sem auditoria periódica é negligência.

## Princípio raiz: mitigação ativa de viés

Modelos de IA herdam vieses históricos. RH é caso onde viés tem impacto direto na vida de pessoas. Por isso este prompt:

- **Bloqueia variáveis protegidas** explicitamente
- **Foca em competências verificáveis**, não em sinalizações sociais
- **Anonimiza** quando possível (nome, foto, endereço, escola podem viesar)
- **Audit log** de decisões para revisão humana mensal

## Fundamentação

| Norma | Aplicação |
|---|---|
| **CF Art. 5** | Igualdade; vedação de discriminação |
| **CLT** | Direitos trabalhistas; processo seletivo |
| **LGPD Art. 11** | Dados sensíveis vedados em scoring |
| **LGPD Art. 20** | Direito à revisão humana |
| **Lei 9.029/95** | Vedação de práticas discriminatórias na contratação |

## Estrutura

Output em 5 seções:

1. **Match técnico** (% de fit, com justificativa)
2. **Pontos fortes verificáveis** (apenas competências, evidências)
3. **Lacunas observadas** (sem inferir, apenas o que não está no CV)
4. **Recomendação para próxima etapa** (entrevista técnica / cultural / dispensa)
5. **Disclaimer obrigatório**

## Conexão com o livro

- **Cap 40 — Casos RH + Marketing + Educação**: contexto completo
- **Cap 24 — Engenharia de Prompt**: técnicas aplicadas
- **Cap 34 — Evaluations**: auditoria de viés

Ver [`changelog.md`](./changelog.md).
