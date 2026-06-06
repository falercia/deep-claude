# Política-Quadro de Uso de Inteligência Artificial

> **Template institucional**. Adapte ao contexto da sua casa antes de adotar como documento oficial.
> Versão template: 1.0 — 2026-07
> Calibrado para empresa brasileira com LGPD, ISO 42001 como referência.

---

## METADADOS DO DOCUMENTO

| Campo | Valor |
|---|---|
| **Documento** | Política-Quadro de Uso de Inteligência Artificial |
| **Código** | POL-IA-001 |
| **Versão** | 1.0 |
| **Data de aprovação** | [DATA] |
| **Owner** | [CTO ou Head de Tecnologia] |
| **Sponsor executivo** | [CEO] |
| **Periodicidade de revisão** | Anual |
| **Próxima revisão** | [DATA + 12 meses] |
| **Classificação** | Política institucional |

---

## 1. OBJETIVO

Estabelecer os princípios, diretrizes e responsabilidades para uso responsável de sistemas de Inteligência Artificial pela [NOME DA EMPRESA], garantindo conformidade regulatória, proteção de dados pessoais, mitigação de riscos e aproveitamento estratégico da tecnologia.

---

## 2. ESCOPO

Esta política aplica-se a:

- Todos os colaboradores, terceiros e parceiros que utilizem sistemas de IA em nome da [NOME DA EMPRESA]
- Todos os sistemas de IA desenvolvidos internamente, contratados ou consumidos via API
- Todos os ambientes operacionais (produção, homologação, desenvolvimento)
- Todas as áreas de negócio que adotam IA (engenharia, produto, dados, RH, jurídico, financeiro, marketing, atendimento)

Não se aplica a:

- Uso pessoal de IA fora do contexto profissional
- Sistemas de IA que não processam dados da [NOME DA EMPRESA] e não tomam decisões em nome dela

---

## 3. PRINCÍPIOS FUNDAMENTAIS

### 3.1 Conformidade regulatória

Todo uso de IA respeitará a legislação brasileira aplicável, com atenção especial a:

- Lei Geral de Proteção de Dados (LGPD - Lei 13.709/2018)
- Marco Civil da Internet (Lei 12.965/2014)
- Constituição Federal (Art. 5 - igualdade e não-discriminação)
- Regulação setorial aplicável ([listar: BACEN, CFM, OAB, ANS, CVM, etc.])

### 3.2 Supervisão humana

Sistemas de IA operam sob princípio de supervisão humana qualificada. Decisões com impacto material em pessoas (contratação, crédito, atendimento médico, jurídico) terão revisão humana obrigatória, conforme LGPD Art. 20.

### 3.3 Transparência

Sistemas de IA serão documentados em **AI Cards** institucionais, com propósito, dados utilizados, métricas de desempenho, limitações e responsável. Stakeholders afetados serão informados quando IA é utilizada em decisão que os impacta.

### 3.4 Mitigação de viés

Sistemas de IA serão avaliados periodicamente quanto a viés algorítmico, especialmente em casos de uso com impacto em pessoas. Variáveis protegidas (raça, gênero, idade, religião, orientação, deficiência) não serão usadas em scoring sem justificativa específica e revisão humana.

### 3.5 Segurança da informação

Dados utilizados em sistemas de IA respeitarão as políticas de segurança da informação da [NOME DA EMPRESA]:

- Criptografia em trânsito e em repouso
- Controle de acesso por menor privilégio
- Audit log de todas as operações
- Soberania de dados via [Bedrock SP ou equivalente] para dados sensíveis

### 3.6 Soberania da casa

A [NOME DA EMPRESA] mantém soberania sobre decisões estratégicas envolvendo IA, evitando dependência crítica de fornecedor único quando viável (estratégia multi-modelo ou multi-cloud).

### 3.7 Evolução contínua

Esta política é revisada anualmente ou conforme demanda regulatória, com atualizações comunicadas ao corpo executivo e times.

---

## 4. GOVERNANÇA

### 4.1 Comitê de IA

Fica instituído o **Comitê de IA** da [NOME DA EMPRESA], com a seguinte composição:

| Papel | Responsável | Frequência |
|---|---|---|
| Sponsor executivo | [CEO ou C-level designado] | Aprova mudanças estruturais |
| Owner técnico | [CTO/Head de Tecnologia] | Conduz comitê |
| Representante jurídico | [Jurídico Sênior ou DPO] | Valida compliance |
| Representante de dados | [Head de Dados ou Eng. responsável] | Valida tratamento |
| Representante de negócio | [VP Operações ou área crítica] | Valida impacto operacional |
| Convidados | Por demanda | Especialistas em casos específicos |

**Periodicidade**: trimestral (ordinária) + extraordinária quando incidente ou decisão crítica.

**Atribuições**:

- Aprovar novos sistemas de IA (via AI Card)
- Revisar incidentes
- Aprovar mudanças nesta política
- Receber e priorizar contribuições de auditoria
- Comunicar decisões estratégicas ao corpo executivo

### 4.2 AI Cards

Todo sistema de IA em produção será cadastrado em **AI Card** padronizado (ver `ai-card-template.md`), contendo:

- Propósito e caso de uso
- Modelos e fornecedores utilizados
- Dados de entrada e saída
- Métricas de desempenho
- Limitações conhecidas
- Responsável técnico e de negócio
- Data de aprovação pelo Comitê

AI Cards são revisados a cada 6 meses ou mediante mudança material.

### 4.3 RACI

| Tarefa | R | A | C | I |
|---|---|---|---|---|
| Aprovar novo sistema | Comitê | CEO | Jurídico | Áreas |
| Manter AI Card | Owner técnico | CTO | Comitê | Stakeholders |
| Responder incidente | Owner técnico | CTO | Jurídico, DPO | CEO |
| Auditoria periódica | Owner técnico | CTO | Comitê | Auditoria interna |
| Comunicar a stakeholders | Owner técnico | CTO | Comunicação | Públicos afetados |

---

## 5. DIRETRIZES OPERACIONAIS

### 5.1 Adoção de novo sistema

Todo novo sistema de IA passa por:

1. **Proposta** (área solicitante preenche AI Card preliminar)
2. **Análise técnica** (Owner técnico avalia)
3. **Análise jurídica** (Jurídico/DPO avalia LGPD e regulatório)
4. **Análise de risco** (Comitê avalia riscos identificados)
5. **Aprovação ou ajustes** (Comitê delibera)
6. **Implementação** (com monitoramento ativo)
7. **Revisão pós-lançamento** (30, 60, 90 dias)

### 5.2 Dados pessoais

Sistemas que processam dados pessoais respeitarão:

- **Base legal LGPD Art. 7** declarada explicitamente
- **Dados sensíveis (Art. 11)** apenas com consentimento ou base legal específica
- **Direitos do titular (Art. 18)** garantidos via processo definido
- **Soberania nacional** para dados sensíveis ([Bedrock SP ou equivalente])
- **Transferência internacional (Art. 33+)** apenas com garantias adequadas

### 5.3 Decisões automatizadas

Sistemas que tomam decisões automatizadas com impacto em pessoas (crédito, contratação, atendimento médico, jurídico) terão:

- **Revisão humana** disponível conforme LGPD Art. 20
- **Explicabilidade** da decisão para o titular afetado
- **Audit log** completo da decisão
- **Métricas de viés** monitoradas periodicamente

### 5.4 Fornecedores de IA

Contratos com fornecedores de IA conterão obrigatoriamente:

- Cláusulas de proteção de dados (LGPD)
- Cláusulas de soberania (quando aplicável)
- Cláusulas de auditoria (direito de auditoria)
- Cláusulas de continuidade (em caso de descontinuação)
- Cláusulas de responsabilidade civil

### 5.5 Treinamento e capacitação

Colaboradores que utilizam IA em sua função terão acesso a:

- Capacitação inicial sobre uso responsável de IA
- Atualizações anuais sobre mudanças regulatórias e tecnológicas
- Canais de dúvida e reporte de incidentes

---

## 6. RESPOSTA A INCIDENTES

### 6.1 Tipos de incidente

- **Vazamento de dados** (LGPD)
- **Decisão inadequada de IA com impacto material**
- **Viés algorítmico identificado**
- **Falha de fornecedor crítico**
- **Reclamação formal** (ANPD, regulador setorial)

### 6.2 Procedimento padrão

1. Identificação e contenção (Owner técnico)
2. Notificação ao Comitê de IA (até 24h)
3. Análise de impacto (até 48h)
4. Comunicação à ANPD se aplicável (até 72h, conforme LGPD Art. 48)
5. Comunicação a titulares afetados se aplicável
6. Plano de ação e remediação
7. Revisão pós-incidente (postmortem)

Runbook detalhado em `runbook-anpd-72h.md`.

---

## 7. AUDITORIA E MONITORAMENTO

A [NOME DA EMPRESA] realizará:

- **Auditoria interna trimestral** dos sistemas em produção
- **Auditoria externa anual** (recomendada quando aplicável)
- **Monitoramento contínuo** de incidentes e reclamações
- **Métricas de viés** mensais para sistemas com impacto em pessoas

Resultados são reportados ao Comitê de IA e ao Conselho/Diretoria.

---

## 8. SANÇÕES

Violações desta política são tratadas conforme política disciplinar da [NOME DA EMPRESA]. Casos graves podem resultar em desligamento, comunicação a órgão regulador e/ou medidas judiciais.

---

## 9. REFERÊNCIAS

- Lei Geral de Proteção de Dados (Lei 13.709/2018)
- Marco Civil da Internet (Lei 12.965/2014)
- ISO/IEC 42001:2023 — AI Management Systems
- NIST AI RMF (referência técnica)
- [Regulação setorial aplicável: BACEN, CFM, OAB, ANS, CVM, etc.]
- Política de Segurança da Informação da [NOME DA EMPRESA]
- Política de Proteção de Dados da [NOME DA EMPRESA]

---

## 10. APROVAÇÃO

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| Sponsor executivo (CEO) | | | |
| Owner técnico (CTO) | | | |
| Jurídico/DPO | | | |
| Conselho (quando aplicável) | | | |

---

## CONTROLE DE VERSÕES

| Versão | Data | Mudanças | Aprovador |
|---|---|---|---|
| 1.0 | [DATA] | Versão inicial | Comitê de IA |

---

*Este é um template baseado em práticas observadas em empresas brasileiras adotando IA com governança séria. Não é parecer jurídico. Antes de adotar como política oficial, valide com jurídico interno e ajuste ao contexto da casa.*
