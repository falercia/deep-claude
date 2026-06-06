---
name: analise-juridica-br
description: Skill para análise estruturada de contratos brasileiros como apoio a advogado. Acionar quando usuário pedir para "analisar contrato", "revisar cláusulas", "due diligence contratual" ou similar, em contexto de Direito brasileiro. NÃO emite parecer jurídico — produz insumo qualificado para advogado.
version: 1.0
---

# Análise Jurídica BR

## Quando ativar

Acione quando o usuário pedir:

- "analise este contrato"
- "revisa as cláusulas"
- "due diligence contratual"
- "identifica riscos contratuais"
- "pontos de negociação"
- Termos similares em contexto contratual

**Não ative** quando:

- Pedido envolve emissão de parecer jurídico (skill é apoio, não parecer)
- Contrato é em jurisdição não-brasileira (skill é calibrado para Brasil)
- Pergunta é sobre legislação geral (use conhecimento direto, sem skill)

## O que faz

Produz análise estruturada em 5 seções:

1. **Síntese executiva** — para CTO/CEO em 60 segundos
2. **Cláusulas críticas identificadas** — com transcrição + análise + risco
3. **Pontos de negociação prioritários** — com proposta alternativa
4. **Riscos LGPD e regulatórios** — quando aplicável
5. **Próximos passos recomendados** — ação executiva

## Regras absolutas

- **NUNCA** emitir parecer jurídico. Output é insumo para advogado.
- **NUNCA** classificar risco genericamente. Sempre justificar.
- **SEMPRE** citar cláusula literalmente quando crítica.
- **SEMPRE** incluir disclaimer obrigatório.

## Modelo recomendado

- Claude Opus (versão corrente) com extended thinking ativo
- Temperature 0.0 para análise determinística

## Configurações

```xml
<contexto>
  <setor>{{setor_da_empresa}}</setor>
  <jurisdicao>Brasil</jurisdicao>
  <relacao>{{B2B | B2C | Estatal}}</relacao>
  <criticidade>{{alto | medio | baixo}}</criticidade>
</contexto>
```

## Prompt base

Use o prompt `P-LEG-CLAUDE-01` do repositório como base, adaptando contexto.

## Disclaimer obrigatório no output

> Análise gerada com auxílio de IA. Insumo qualificado, sem valor de parecer jurídico. Decisão final deve ser tomada por advogado responsável.

## Conexões

- Cap 36 — Casos Jurídicos
- Cap 24 — Engenharia de Prompt Avançada
- Cap 23 — Extended Thinking
- Prompt P-LEG-CLAUDE-01 (versão completa)

## Fundamentação regulatória

- OAB Provimento 205/2021 (uso responsável de IA jurídica)
- LGPD (Art. 5, 7, 46 — quando contrato envolve dados pessoais)
- Código Civil (Arts. 421, 422)
- CDC (quando relação B2C)
- Lei das Estatais (13.303/16, quando uma das partes for estatal)
