# Changelog — P-MED-CLAUDE-01

## [1.0.0] — 2026-07

### Adicionado
- Versão inicial respeitando CFM Resolução 2.314/2022
- Constituição XML com 7 regras (3 absolutas: nunca diagnostica, nunca prescreve, nunca atende paciente direto)
- Output em 6 seções estruturadas para entrada em prontuário
- Soberania Bedrock SP **obrigatória** para dados de saúde (LGPD Art. 11)
- Self-critique reforçado para validação pré-resposta
- Disclaimer CFM obrigatório
- Golden set com 8 casos (threshold 90%, médico-no-loop validar 100%)

### Decisões editoriais
- Modelo Sonnet padrão (custo/qualidade adequado)
- Médico-no-loop como requisito não-negociável
- Anonimização de PII no output
