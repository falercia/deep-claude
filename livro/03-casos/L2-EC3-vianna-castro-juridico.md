# EC3 — VIANNA, CASTRO E ALMEIDA ADVOGADOS
## Due diligence assistida em M&A

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em escritórios brasileiros de M&A entre 2025 e 2026; números são realistas mas não identificam banca específica.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | Jurídico — banca de M&A |
| **Tamanho** | ~180 advogados, 22 sócios na área de M&A |
| **Tickets típicos** | R$ 800 mil a R$ 4 milhões por operação |
| **Maturidade IA** | Inicial — uso de ChatGPT individual antes do projeto |
| **Tempo médio de DD** | 6-12 semanas |
| **Tempo de sócio sênior em leitura linear** | ~60% do esforço |
| **Invariantes ilustrados** | 1, 7, 8, 9 |
| **Frameworks** | F1 DECID-IA, F4 PROMPT-EXT, F6 GOV-INDELEGÁVEL, F8 EVAL-PIRÂMIDE |

## 2. PROBLEMA

Due diligence em M&A consome 6-12 semanas. Advogado sênior gasta 60% do tempo em leitura linear de contratos repetitivos. Risco real de cláusula crítica perdida — "change of control" enterrada na página 87 de um contrato de 150 páginas. Quando a cláusula é perdida, a banca responde por advogado sênior; reputação e seguro profissional ficam expostos.

## 3. TESE INICIAL ERRADA

Substituir a leitura humana por LLM lendo tudo. Violação de Inv. 8: parecer com base em "o modelo leu" não é defensável. Violação de Inv. 1: alucinação de citação em parecer jurídico é falha de carreira.

## 4. ARQUITETURA — RAG por categoria de cláusula + agente extrator + revisor humano

Pipeline em 6 etapas:
1. **Ingestão e chunking** do data room
2. **Classificação** de documentos por tipo (contrato comercial, societário, trabalhista, fiscal)
3. **Extração estruturada** de 30+ cláusulas-alvo por contrato (change of control, MAC, indemnification cap, non-compete, governing law, jurisdição, ANR, drag-along, tag-along)
4. **Sumarização executiva** por categoria
5. **Red flags** com citação literal (página, parágrafo, hash do trecho)
6. **Sócio sênior revisa apenas os flags** — não relê o data room linearmente

## 5. MCP — Tools privadas

| Tool | Permissão | Auditoria |
|------|-----------|-----------|
| `lista_documentos_data_room` | Read | Span por consulta |
| `extrai_clausula` | Read | Span + cláusula extraída |
| `cita_pagina_paragrafo` | Read | Hash do trecho + verificação contra original |
| `compara_clausula_padrao` | Read | Span + padrão da banca aplicado |
| `gera_sumario_categoria` | Read | Span + revisão por sêniores |
| `marca_red_flag` | Write (registro) | Span + SEV + dono |

Aplicação F5: Quadrante D (sem padrão público, dados sensíveis) — MCP próprio com auditoria por sócio responsável.

## 6. AGENTES

| Agente | Modelo | Função |
|--------|--------|--------|
| Classificador | Haiku | Classifica documento por tipo |
| Extrator por cláusula | Sonnet com rubrica em system prompt | Extrai cláusula específica com citação literal obrigatória |
| Sumarizador | Sonnet | Produz sumário executivo por categoria |
| Avaliador de flag | **Opus** (casos críticos) | Decide SEV-1 ou SEV-2 |
| Sócio sênior | Humano | Decide parecer; agente nunca recomenda |

## 7. GOVERNANÇA F6

| Camada | Item |
|--------|------|
| Técnica | Confidencialidade do data room (cliente exige); modelo Claude Enterprise com data zoning; tracing por documento e cláusula; retenção por operação conforme contrato com cliente |
| Operacional | AUP por operação (cada DD tem AUP específica assinada por sócio responsável); RACI claro (sócio responsável pelo parecer; advogado sênior pela extração; banca pela auditoria) |
| Executiva | Comitê de qualidade jurídica + Comitê de IA + Conselho de sócios mensal |

## 8. EVALS (F8)

**Base.** Validação estrutural da citação (página + parágrafo + hash do trecho confere com o original).
**Meio.** Golden set de **40 DDs reais** (anonimizadas com consentimento ou cenários equivalentes); gabarito de cláusulas-alvo por sêniores; LLM-as-judge calibrado para citação correta; adversarial set de cláusulas enterradas, redação ambígua, idioma misto (português + inglês), cláusulas com defesa por extensão.
**Topo.** Sócio sênior revisa amostra em cada operação.
**Política de bloqueio:** alucinação de citação ≥0,5% bloqueia release. Inv. 1 não admite tolerância em jurídico.

## 9. LLMOPS

- Tracing por documento e por cláusula extraída
- Versionamento de rubrica por categoria de cláusula
- Canário em 2 operações antes de uso pleno em toda a área de M&A
- Quota por operação (custo composto sob controle)
- Kill switch por categoria de cláusula

## 10. MÉTRICAS

| Métrica | Pré-projeto | Resultado |
|---------|-------------|-----------|
| Tempo médio de DD | 8 semanas | 3 semanas (operações típicas) |
| Cobertura de cláusulas (recall) | baseline | +27% |
| Flags relevantes capturados vs baseline humano | baseline | +14% |
| Alucinação de citação | n/a | <0,5% |
| Capacidade por sócio | baseline | 2,5× |

## 11. ROI

- Capacidade 2,5× sem expandir time de sêniores
- Preço por operação mantido (banca cobra por valor, não por hora)
- Margem ↑ 22 pontos percentuais
- Sócios reorientam tempo para a *decisão* (parecer, estratégia), não para *leitura linear*

## 12. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Alucinação de citação | Citação literal com hash; eval de "honestidade de citação" mensal; double-check humano em todo red flag SEV-1 |
| Vazamento de data room | Data zoning Enterprise; isolamento por cliente |
| Sycophancy diante do cliente comprador | Constitutional principle no system prompt ("nunca afirme cláusula sem citar texto literal") |
| Over-extraction de cláusula inexistente | Validação de hash do trecho |

## 13. LIÇÃO ESTRUTURAL

*No jurídico, IA não substitui o sócio; ela substitui a leitura linear que o sócio fazia para chegar ao parágrafo que importa. O ganho é redirecionar o tempo do humano caro para o que só ele pode decidir.*

## 14. CONEXÕES

- 🔗 [Manifesto](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Inv. 1, 7, 8, 9)
- 🔗 Frameworks: [F1](../../Livro-1-Os-Invariantes/03-frameworks/L1-F1-decid-ia.md), [F4](../../Livro-1-Os-Invariantes/03-frameworks/L1-F4-prompt-ext.md), [F6](../../Livro-1-Os-Invariantes/03-frameworks/L1-F6-gov-indelegavel.md), [F8](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md)
- 🔗 Caps: [6 RAG](../../Livro-1-Os-Invariantes/02-capitulos/L1-C06-rag.md), [11 Context](../../Livro-1-Os-Invariantes/02-capitulos/L1-C11-context-engineering.md), [39 Evals](../../Livro-1-Os-Invariantes/02-capitulos/L1-C39-evals.md), [42 Governança](../../Livro-1-Os-Invariantes/02-capitulos/L1-C42-governanca.md)
- 🔗 Claude: [Cap 22 Research](../02-capitulos/L2-C23-research.md), [Cap 30 Enterprise](../02-capitulos/L2-C31-enterprise.md), [Cap 31 Skills](../02-capitulos/L2-C32-skills.md)

---

> *"No jurídico, alucinação de citação é falha de carreira. Sem F8 EVAL-PIRÂMIDE, IA em DD é risco profissional."*
