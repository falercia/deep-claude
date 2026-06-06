# Changelog — P-LEG-CLAUDE-01

Todas as mudanças relevantes deste prompt registradas em ordem cronológica reversa.

---

## [1.0.0] — 2026-07

### Adicionado
- Versão inicial do prompt
- Constituição XML completa com role, contexto, regras (3 prioridades), estrutura de output (5 seções)
- Extended thinking ativo por padrão (budget 12000 tokens)
- Self-critique embutido para validação pré-resposta
- Disclaimer obrigatório citando insumo qualificado
- Golden set inicial com 12 casos representativos
- README com fundamentação regulatória (OAB Provimento 205/2021, LGPD, CDC, Lei das Estatais)

### Decisões editoriais
- Output em português brasileiro, tom executivo
- Modelo recomendado: Claude Opus (versão corrente) por padrão
- Variantes futuras para Sonnet em volume alto (v1.1)

### Próximos passos
- v1.1: variante Sonnet para casos não-críticos
- v1.2: variantes regionais por estado (foro, especificidades)
- v2.0: integração com ferramentas externas via tool_use (consulta a jurisprudência)
