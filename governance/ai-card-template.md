# AI Card — [NOME DO SISTEMA]

> **Template de ficha institucional de sistema de IA.**
> Preenchido pelo Owner técnico, validado pelo Comitê de IA.
> Revisado a cada 6 meses ou mediante mudança material.

---

## 1. IDENTIFICAÇÃO

| Campo | Valor |
|---|---|
| **Nome do sistema** | [Nome interno] |
| **Código** | AIC-[ÁREA]-[NÚMERO] |
| **Versão** | 1.0 |
| **Owner técnico** | [Nome — função] |
| **Owner de negócio** | [Nome — função] |
| **Sponsor executivo** | [C-level responsável] |
| **Data de aprovação** | [DATA] |
| **Próxima revisão** | [DATA + 6 meses] |
| **Status** | [Proposta / Homologação / Produção / Descontinuado] |

---

## 2. PROPÓSITO E CASO DE USO

### 2.1 Descrição
[Descreva o sistema em 3-5 frases: o que faz, para quem, qual o ganho esperado]

### 2.2 Caso de uso primário
[Cenário concreto de uso]

### 2.3 Casos de uso secundários
[Outros cenários aplicáveis]

### 2.4 Casos de uso vedados
[Explicitamente o que o sistema NÃO deve fazer]

---

## 3. ARQUITETURA TÉCNICA

### 3.1 Modelos utilizados

| Modelo | Fornecedor | Versão | Endpoint |
|---|---|---|---|
| [Ex: claude-sonnet-4.x] | Anthropic | [versão_datada] | [Bedrock SP / API direta] |

### 3.2 Componentes

- **Frontend / Interface**: [como usuário interage]
- **Backend / Orquestração**: [stack utilizado]
- **Banco de dados**: [se aplicável]
- **Banco vetorial / RAG**: [se aplicável]
- **Tool use / Function calling**: [ferramentas conectadas]
- **MCPs conectados**: [se aplicável]
- **Skills utilizados**: [se aplicável]

### 3.3 Soberania de dados
[Onde os dados são processados; Bedrock SP, AWS regional, API global, etc.]

---

## 4. DADOS

### 4.1 Dados de entrada

| Tipo de dado | Origem | PII? | Sensível (LGPD Art. 11)? |
|---|---|---|---|
| [Ex: prompt do usuário] | [Ex: interface web] | sim/não | sim/não |
| [Ex: documento anexado] | [Ex: upload] | sim/não | sim/não |

### 4.2 Dados de saída
[O que o sistema produz; texto, classificação, score, etc.]

### 4.3 Base legal LGPD (se PII envolvido)
[Art. 7 inciso aplicável: consentimento, legítimo interesse, execução de contrato, etc.]

### 4.4 Retenção de dados
[Tempo de retenção de logs, prompts, outputs]

### 4.5 Anonimização
[Quais dados são anonimizados antes do prompt; estratégia de mitigação]

---

## 5. MÉTRICAS DE DESEMPENHO

### 5.1 Métricas técnicas

| Métrica | Valor atual | Meta | Frequência de medição |
|---|---|---|---|
| Latência p50 | | | |
| Latência p95 | | | |
| Taxa de erro | | | |
| Custo por chamada | | | |

### 5.2 Métricas de qualidade

| Métrica | Valor atual | Meta | Frequência |
|---|---|---|---|
| Score em golden set | | ≥ 85% | Mensal |
| Taxa de revisão humana negativa | | < 10% | Mensal |
| NPS de usuário (se aplicável) | | | Trimestral |

### 5.3 Métricas de viés (para sistemas com impacto em pessoas)

| Métrica | Valor atual | Meta | Frequência |
|---|---|---|---|
| Distribuição de aprovações por variável protegida | | Paridade ±10% | Mensal |
| Reclamações de discriminação | | 0 | Mensal |

---

## 6. RISCOS E LIMITAÇÕES

### 6.1 Riscos identificados

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| [Ex: alucinação em domínio crítico] | M | A | [Revisão humana obrigatória + golden set] |
| [Ex: viés algorítmico] | M | A | [Auditoria mensal + variáveis protegidas excluídas] |
| [Ex: falha de fornecedor] | B | A | [Multi-modelo gateway] |

### 6.2 Limitações conhecidas
- [Domínios em que o sistema não funciona bem]
- [Casos onde a saída é menos confiável]
- [Dependências externas críticas]

### 6.3 Casos de escalonamento para humano
[Quando o sistema obrigatoriamente escala para revisão humana]

---

## 7. COMPLIANCE E REGULAÇÃO

| Norma | Aplicável? | Tratamento |
|---|---|---|
| LGPD (geral) | Sim/Não | [Como respeitada] |
| LGPD Art. 11 (sensíveis) | Sim/Não | [Como respeitada] |
| LGPD Art. 20 (decisão automatizada) | Sim/Não | [Mecanismo de revisão] |
| Setorial (BACEN/CFM/OAB/ANS/CVM/...) | Sim/Não | [Como respeitada] |
| ISO 42001 (referência) | Sim/Não | [Aderência] |
| EU AI Act (se opera Europa) | Sim/Não | [Categoria de risco] |

---

## 8. INCIDENTES E APRENDIZADOS

### 8.1 Histórico de incidentes
[Tabela de incidentes registrados, data, descrição, ação tomada]

### 8.2 Postmortems
[Links para postmortems se aplicável]

### 8.3 Mudanças aplicadas a partir de incidentes
[Aprendizados incorporados]

---

## 9. CONTINUIDADE E DESCOMISSIONAMENTO

### 9.1 Plano de continuidade
[O que acontece se o fornecedor descontinua o modelo; estratégia de fallback]

### 9.2 Critérios de descomissionamento
[Sob quais condições o sistema seria desligado]

### 9.3 Plano de descomissionamento
[Como dados, logs e dependências serão tratados ao desligar]

---

## 10. APROVAÇÕES

### 10.1 Análise técnica
| Papel | Nome | Data | Parecer |
|---|---|---|---|
| Owner técnico | | | |
| Arquiteto/Líder técnico | | | |

### 10.2 Análise jurídica
| Papel | Nome | Data | Parecer |
|---|---|---|---|
| Jurídico/DPO | | | |

### 10.3 Comitê de IA
| Papel | Nome | Data | Decisão |
|---|---|---|---|
| Sponsor executivo | | | |
| Owner técnico (CTO) | | | |
| Representante jurídico | | | |
| Representante de dados | | | |
| Representante de negócio | | | |

**Decisão**: [Aprovado / Aprovado com ressalvas / Rejeitado / Aguardando ajustes]

**Ressalvas (se aplicável)**:
[Lista de ressalvas a serem endereçadas]

---

## CONTROLE DE VERSÕES

| Versão | Data | Mudanças | Aprovador |
|---|---|---|---|
| 1.0 | [DATA] | Versão inicial | Comitê de IA |

---

*Template baseado em práticas observadas em empresas brasileiras com governança madura de IA. Baseado em ISO 42001:2023 e LGPD. Adapte ao contexto da casa.*
