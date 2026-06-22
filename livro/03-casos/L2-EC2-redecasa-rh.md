# EC2 — REDECASA
## Triagem de currículos com auditoria e mitigação de viés

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em redes brasileiras de varejo de médio e grande porte durante adoção de IA em RH entre 2024 e 2026; números são realistas mas não identificam empresa específica.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | Varejo BR (rede de materiais de construção e decoração) |
| **Tamanho** | ~7.000 colaboradores em 110 lojas |
| **Maturidade IA** | Médio — uso de ferramentas pontuais em marketing e logística |
| **Volume de candidaturas/ano** | 280 mil |
| **Volume de contratações/ano** | 14 mil (rotatividade típica do setor) |
| **Tempo médio por currículo na triagem** | 22 segundos |
| **Tempo médio de fechamento de vaga** | 31 dias |
| **Restrições regulatórias** | LGPD art. 20 (decisão automatizada que afeta direitos); legislação antidiscriminação |
| **Invariantes ilustrados** | 1 (Plausibilidade), 8 (Responsabilidade Indelegável) |
| **Frameworks aplicados** | F1 DECID-IA, F6 GOV-INDELEGÁVEL, F8 EVAL-PIRÂMIDE |

---

## 2. PROBLEMA

Recrutadores leem em média 22 segundos por currículo. Auditoria interna identificou viés inconsciente em decisões de triagem (currículos com nome feminino em vagas de cargo de chefia recebiam recall menor que currículos masculinos equivalentes). Volume crescente (280 mil candidaturas/ano) torna humanização da triagem inviável no orçamento. Diretoria de RH pediu proposta de uso de IA. Diretoria jurídica e DPO alertaram para LGPD art. 20 (sobre decisão automatizada que afeta direitos) e exigiram governança rígida.

---

## 3. TESE INICIAL ERRADA

A proposta inicial do fornecedor era "deixar a IA classificar de 1 a 5 e cortar automaticamente os ≤2". A proposta tinha duas falhas estruturais.

- **Viola LGPD art. 20:** decisão automatizada que afeta direito (acesso ao emprego) precisa de revisão humana significativa, não cosmética. "IA decide, humano confirma 50/dia em pilha" não passa.
- **Viola Inv. 8 (Responsabilidade Indelegável):** se o sistema discriminar, "foi o algoritmo" não responde processo trabalhista nem ação da ANPD.
- **Viola Inv. 1 (Plausibilidade):** modelo entrega o plausível para o critério aprendido; vieses históricos no dataset de treino vão para o critério "plausível" sem alarme.

A diretora de RH aplicou o **F1 DECID-IA**. Reformulou para uso da IA como assistente do recrutador, nunca como decisor único.

---

## 4. ARQUITETURA ESCOLHIDA — IA como assistente, nunca decisor

A arquitetura usa IA como **camada de redução de carga cognitiva**, com decisão final sempre humana e auditada.

```
Vaga aberta com job description e rubrica  ←  Hiring manager + recrutador sênior co-criam
       ↓
Currículos chegam  →  Extração estruturada de campos (anos exp, formação, skills)
       ↓
Sumário objetivo de 3 bullets (sem inferir protected attributes)
       ↓
Comparação contra rubrica + ranqueamento parcial com justificativa por critério
       ↓
Recrutador humano decide top-15 a entrevistar  ←  Decisão sempre humana, registrada
       ↓
Decisão de avanço com justificativa textual  ←  Audit log retido por 5 anos
```

**Cinco princípios não-negociáveis:**

1. **Nunca classificar 1-5 e cortar automaticamente.** O modelo nunca toma a decisão final.
2. **Nunca inferir atributos protegidos.** Modelo proibido por system prompt de inferir gênero, raça, idade, religião, orientação a partir do currículo. Eval específico testa.
3. **Sempre humanizar a decisão.** Cada movimento (manter ou descartar) tem ação humana registrada com nome do recrutador.
4. **Auditoria de viés contínua.** Adversarial set roda mensalmente com variantes equivalentes do mesmo currículo (nomes diferentes, contextos diferentes); decisão deve ser consistente.
5. **Transparência com candidato.** Política pública declara uso de IA na triagem; candidato pode solicitar revisão humana adicional.

---

## 5. WORKFLOW

```
1. Job description + rubrica explícita por critério (definida com hiring manager)
       ↓
2. Currículos chegam → extração estruturada (anos exp, formação, skills)
       ↓
3. Sumário objetivo em 3 bullets, sem julgamento, sem inferência de atributos
       ↓
4. Comparação contra rubrica do cargo
       ↓
5. Ranqueamento parcial com justificativa por critério (não nota agregada)
       ↓
6. Recrutador humano lê sumário + justificativa, decide top-15 a entrevistar
       ↓
7. Decisão de avanço registrada com nome do recrutador, timestamp, justificativa
       ↓
8. Audit log retido por 5 anos (LGPD + legislação trabalhista)
```

---

## 6. MCP — Tools privadas

| Tool | Permissão | Auditoria |
|------|-----------|-----------|
| `extrai_campos` | Read | Span por chamada |
| `compara_contra_rubrica` | Read | Span por chamada com rubrica usada |
| `gera_sumario` | Read | Span + sumário gerado retido |
| `registra_decisao_humana` | Write (irreversível) | Span + nome do recrutador + timestamp + justificativa |
| `audita_log` | Read (restrito a DPO) | Span por consulta |

Aplicação do **F5 MCP-COBERTURA**: tools de RH ficam no **Quadrante D** (sem padrão maduro público; dados altamente sensíveis pela LGPD) — MCP próprio com auditoria por DPO.

---

## 7. AGENTES

| Agente | Modelo | Função |
|--------|--------|--------|
| Extrator | Haiku | Extrai campos estruturados; nunca infere atributo |
| Comparador | Sonnet | Compara contra rubrica explícita; gera ranqueamento parcial |
| Justificador | Sonnet | Gera justificativa por critério, em pt-BR objetivo |

Decisão sempre humana. Coordenação determinística.

---

## 8. GOVERNANÇA (F6 GOV-INDELEGÁVEL)

| Camada | Item | Dono |
|--------|------|------|
| Técnica | Tracing completo; retenção 5 anos; versionamento de rubrica e prompt; canário restrito a 1 unidade da rede; rollback <2 min | Tech Lead RH + DPO |
| Operacional | AUP que proíbe inferência de atributos; política de transparência com candidato; log auditável de cada decisão; auditoria de viés trimestral; canal de revisão para candidato rejeitado | Diretora de RH + DPO |
| Executiva | Comitê de RH + Jurídico + DPO mensal; revisão semestral de viés por auditor externo; relatório à diretoria | CHRO + CEO |

---

## 9. EVALS COMPORTAMENTAIS (F8 EVAL-PIRÂMIDE + Cap 41 Alignment)

**Base.** Schema validation do sumário (3 bullets obrigatórios, sem campos protegidos preenchidos). Validação estrutural da rubrica usada.

**Meio.** Golden set de **400 currículos** com gabarito de recrutadores sêniores anotado em sessões dedicadas. LLM-as-judge calibrado com rubrica de 5 critérios: extração correta, sumário factual sem julgamento, ausência de inferência de atributo protegido, comparação contra rubrica explícita, justificativa em pt-BR claro.

**Topo.** Auditoria mensal por consultor externo de RH especializado em viés algorítmico.

**Adversarial.** Conjunto crítico de **120 casos pareados**: mesmo currículo com **variantes equivalentes** — nome masculino × feminino × estrangeiro × negro × branco. Decisão esperada: **idêntica em todas as variantes** para o mesmo conteúdo. Variação na decisão por variante = falha automática que bloqueia release.

Eval específico de **honestidade**: o modelo deve dizer "não posso inferir" quando perguntado sobre atributo protegido, em qualquer formulação. Calibração mensal.

Eval específico de **over-refusal**: o modelo deve responder normalmente a pedidos legítimos sobre o currículo (qualificações técnicas, experiência), não recusar excessivamente por excesso de cautela.

**Política de bloqueio.** Viés medido por adversarial: ≤2% de delta entre variantes equivalentes. Honestidade: ≥99% de respostas corretas em "não posso inferir". Qualquer falha em adversarial crítico bloqueia release.

---

## 10. MÉTRICAS

| Métrica | Pré-projeto | Resultado em 6 meses |
|---------|-------------|------------------------|
| Tempo por currículo | 22s (humano) | 4s humano + 6s IA = 10s total |
| Recall de candidatos qualificados | baseline | +18% (medido em vagas piloto) |
| Viés medido em adversarial | sem medição (incidente) | ≤2% delta entre variantes |
| SEV de viés (ANPD ou denúncia trabalhista) | 1 incidente em 18 meses | 0 |
| Tempo de fechamento de vaga | 31 dias | 17 dias |
| Capacidade de volume sem expansão de headcount | baseline | +120% |
| NPS de candidato (pesquisa pós-processo) | 6,2 | 7,4 |

---

## 11. ROI

- **Capacidade adicional** de absorver +120% de volume sem aumentar headcount de recrutamento
- **Redução de tempo** de fechamento de vaga de 31 dias para 17 dias (-45%)
- **Eliminação de risco** de ação trabalhista por discriminação algorítmica (custo evitado estimado: R$ 2-5 milhões anuais em multas e indenizações)
- **Melhoria de NPS de candidato** que reduz custo de aquisição em vagas reabertas

---

## 12. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Viés residual do modelo (treinado em corpus com vieses históricos) | Adversarial pareado mensal; calibração contra rubrica explícita; sem inferência de atributo |
| Alegação de discriminação algorítmica | Decisão sempre humana e registrada; pipeline auditável; comunicação pública sobre uso de IA |
| Vazamento de currículos (PII) | Classificação automática de PII no pipeline; retenção controlada por DPO |
| Opacidade percebida pelo candidato | Política de transparência publicada; canal de revisão; resposta a solicitação de informação por candidato em ≤15 dias (LGPD) |
| Over-refusal frustrando recrutador | Eval de over-refusal mensal; ajuste fino do system prompt |
| Hiring manager pular o processo | Treinamento obrigatório; auditoria trimestral de decisões para detectar bypass |

---

## 13. LIÇÃO ESTRUTURAL

*Em RH, o ganho de IA não está em decidir, está em compor — ler o que humano não conseguiria, propor o que humano vai aprovar. O Invariante 8 (Responsabilidade Indelegável) protege a empresa contra si mesma: a decisão humana indelegável é o que sustenta a operação juridicamente e moralmente. Quem terceiriza essa decisão para o modelo está construindo passivo institucional, não eficiência operacional.*

---

## 14. CONEXÕES

- 🔗 **Manifesto:** [Cap 00M](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Invariantes 1, 8)
- 🔗 **Frameworks:** [F1](../../Livro-1-Os-Invariantes/03-frameworks/L1-F1-decid-ia.md), [F6](../../Livro-1-Os-Invariantes/03-frameworks/L1-F6-gov-indelegavel.md), [F8](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md)
- 🔗 **Capítulos-âncora:** [Cap 37 Segurança](../../Livro-1-Os-Invariantes/02-capitulos/L1-C37-seguranca.md), [Cap 39 Evals](../../Livro-1-Os-Invariantes/02-capitulos/L1-C39-evals.md), [Cap 41 Alignment](../../Livro-1-Os-Invariantes/02-capitulos/L1-C41-alignment.md), [Cap 42 Governança](../../Livro-1-Os-Invariantes/02-capitulos/L1-C42-governanca.md)
- 🔗 **Aplicação Claude:** [Cap 29 (L2) Team](../02-capitulos/L2-C30-team.md), [Cap 30 (L2) Enterprise](../02-capitulos/L2-C31-enterprise.md), [Cap 34 (L2) Executivos](../02-capitulos/L2-C35-executivos.md)

---

> *"Em decisão automatizada com efeito jurídico, IA é assistente — não decisor. Quem confunde, paga em ação trabalhista e em multa da ANPD."*
