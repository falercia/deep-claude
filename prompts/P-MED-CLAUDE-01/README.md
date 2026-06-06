# P-MED-CLAUDE-01 — Anamnese estruturada (apoio ao médico)

> Prompt profissional para suporte a anamnese estruturada com Claude.
> Calibrado para respeitar CFM (Resolução 2.314/2022) e LGPD em dados de saúde.
> Versão 1.0 — 2026-07

---

## Quando usar

Use este prompt quando precisar de apoio à organização de anamnese, estruturação de queixa do paciente e síntese para prontuário. Tipicamente para:

- Apoio à triagem inicial (com supervisão médica)
- Estruturação de notas pós-consulta para prontuário
- Preparação de discussão de caso clínico
- Síntese de história clínica para encaminhamento

O prompt opera sob princípio "médico-no-loop": **toda decisão clínica é do médico**. Claude apoia organização e estruturação, nunca diagnóstico autônomo.

## Quando NÃO usar

- **Diagnóstico autônomo.** CFM Resolução 2.314/2022 é clara: diagnóstico é ato médico exclusivo.
- **Prescrição.** Prescrição é ato privativo do médico, sem mediação de IA.
- **Decisão de conduta terapêutica.** Mesmo princípio.
- **Comunicação direta com paciente sem supervisão médica.** Resposta a paciente sem médico-no-loop é vedada.
- **Sem fonte primária médica.** Sempre direcionar paciente a profissional habilitado.

## Fundamentação regulatória

| Norma | Aplicação |
|---|---|
| **CFM Resolução 2.314/2022** | Telemedicina; uso de IA em apoio ao médico |
| **CFM Resolução 1.821/2007** | Prontuário eletrônico, integridade, confidencialidade |
| **LGPD Art. 11** | Dados de saúde são sensíveis; tratamento exige base legal específica |
| **Lei 13.787/2018** | Digitalização e arquivamento de prontuários |
| **ANS** | Regras setoriais para operadoras de planos de saúde |

## Estrutura do prompt

Output em 6 seções estruturadas:

1. **Síntese clínica** (para entrada no prontuário, 4-6 linhas)
2. **Queixa principal e história da moléstia atual (HMA)**
3. **Antecedentes relevantes** (pessoais, familiares, hábitos, medicamentos)
4. **Sistemas revisados** (apenas o relatado, sem inferir)
5. **Pontos para o médico avaliar** (hipóteses, exames sugeridos para discussão, sinais de alerta)
6. **Disclaimer obrigatório CFM**

## Modelo e configuração

| Parâmetro | Valor |
|---|---|
| Modelo | Claude Sonnet (versão corrente) |
| Extended thinking | Opcional (casos complexos) |
| Temperature | 0.2 (baixa variação) |
| Max output tokens | 2000 |
| Soberania de dados | **Obrigatória: Bedrock SP** |

**Crítico**: dados de saúde são dados pessoais sensíveis (LGPD Art. 11). Use **Bedrock SP** ou outro endpoint com soberania nacional. Não use API direta para dados de pacientes em produção.

## Conexão com o livro

- **Cap 24 — Engenharia de Prompt**: técnicas XML
- **Cap 37 — Casos Saúde**: contexto regulatório completo (3 prompts da família P-MED)
- **Cap 44 — LGPD**: tratamento de dados sensíveis

## Changelog

Ver [`changelog.md`](./changelog.md).
