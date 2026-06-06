# Governança de IA

> Templates de governança executiva para empresas brasileiras adotando IA com Claude.

---

## Por que esta pasta existe

A obra *Deep Claude*, na Parte 4 (Caps 41-44), apresenta governança como prerrequisito de operação corporativa séria de IA. Esta pasta carrega templates executivos para casa que está construindo sua governança: política-quadro de IA, AI cards por sistema, RACI por comitê, atas modelo, runbook de incidente ANPD.

Templates aqui são ponto de partida. Adapte ao seu setor, valide com jurídico interno, formalize com sponsor executivo.

---

## O que vive aqui

```
governance/
  README.md                        — este arquivo
  politica-quadro-ia.md            — política-quadro modelo (template)
  ai-card-template.md              — modelo de AI Card por sistema (Cap 41)
  raci-comite-ia.md                — RACI modelo do Comitê de IA
  ata-comite-ia-template.md        — modelo de ata trimestral
  runbook-anpd-72h.md              — runbook para incidente comunicado em 72h (LGPD Art. 48)
  checklist-iso-42001.md           — checklist de prontidão para certificação ISO 42001
  matriz-decisoes-ia.md            — matriz de decisões típicas com framework
```

---

## Cobertura inicial — v1.0 (jul/2026)

Templates essenciais:

| Template | Propósito | Capítulo |
|---|---|---|
| `politica-quadro-ia.md` | Documento institucional base | Cap 41 |
| `ai-card-template.md` | Ficha de cadastro de sistema de IA | Cap 41 |
| `raci-comite-ia.md` | Matriz de responsabilidades | Cap 41 |
| `runbook-anpd-72h.md` | Resposta a incidente regulatório | Cap 44 |
| `checklist-iso-42001.md` | Prontidão para certificação | Cap 44 |

---

## Cobertura roadmap

### v1.1 — out/2026
- Templates específicos por setor regulado: saúde (CFM), jurídico (OAB), financeiro (BACEN, CVM)
- Cadernos de governança por porte de empresa

### v1.2 — jan/2027
- Runbooks de auditoria interna
- Templates de relatório anual de governança de IA
- Templates de comunicação a stakeholders

---

## Como usar

**1. Leia o capítulo do livro primeiro.** Templates sem fundamento conceitual viram bureaucracy. Cap 41 detalha o porquê de cada peça.

**2. Adapte ao seu contexto.** Templates são genéricos por desenho. Customize a tom da casa, a estrutura organizacional vigente, o setor regulado.

**3. Valide com jurídico.** Antes de adotar política-quadro como documento oficial, passe por jurídico interno. Templates são ponto de partida, não documento final assinado.

**4. Obtenha sponsor executivo.** Governança sem sponsor vira teatro. CEO, CTO ou CFO precisa assinar a política e participar do comitê.

**5. Itere conforme aprende.** Documento de governança não é estático. Revise trimestralmente, atualize conforme regulação evolui.

---

## Princípios editoriais

**Aterrissado no Brasil.** Templates referenciam LGPD, ANPD, setoriais brasileiros (CFM, OAB, BACEN, CVM). Não tradução literal de templates internacionais.

**Para empresa real.** Templates são para casa que está adotando, não exercício acadêmico. Linguagem de documento corporativo, com seções típicas (versão, owner, revisão, anexos).

**ISO 42001 como referência.** Templates não certificam, mas estão alinhados ao framework ISO 42001:2023 para casa que quer evoluir para certificação.

**Sem auto-promoção.** Templates não citam autor, não vendem serviços, não promovem nada. Documento institucional limpo.

---

## Como contribuir

Sua casa tem template de governança brasileiro maduro? Contribuição é muito bem-vinda.

1. Abra issue com label `novo-template` e descrição
2. Para áreas reguladas, contribuição passa por revisão de especialista
3. Abra PR com template e exemplo de uso

Veja [CONTRATO.md](../CONTRATO.md) para princípios completos.

---

## Capítulos relacionados

- **Cap 41 — Governança Executiva**: fundamentação completa do AI Card e Comitê de IA
- **Cap 42 — Adoção Institucional**: como instalar governança em fases
- **Cap 43 — ROI**: orçamento de governança no orçamento geral
- **Cap 44 — Segurança, Compliance e LGPD**: regulação brasileira aplicada

---

## Referências regulatórias

- **LGPD**: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **ANPD**: https://www.gov.br/anpd/
- **ISO 42001:2023**: https://www.iso.org/standard/81230.html
- **NIST AI RMF**: https://www.nist.gov/itl/ai-risk-management-framework
- **EU AI Act** (se opera Europa): https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
