# Runbook — Incidente de Segurança em IA: comunicação à ANPD em 72h

> **Runbook executivo para incidente de segurança envolvendo dados pessoais em sistema de IA.**
> LGPD Art. 48 exige comunicação à ANPD em prazo razoável (interpretado como 72h pelos guias da ANPD).
> Calibrado para o contexto brasileiro corporativo.

---

## QUANDO ACIONAR ESTE RUNBOOK

Acione este runbook imediatamente quando identificar qualquer evento que possa configurar incidente de segurança com dados pessoais em sistema de IA:

- Vazamento de dados pessoais (interno ou externo)
- Acesso não autorizado a logs/prompts contendo PII
- Exposição inadvertida de PII em resposta de IA (incluindo em outputs vetorizados ou cache)
- Decisão automatizada com impacto material sem mecanismo de revisão
- Comprometimento de credencial ou chave de API que dá acesso a dados pessoais
- Reclamação ou comunicação de titular afetado
- Vulnerabilidade descoberta (em vez de incidente consumado): consultar com DPO se aplica este runbook

**Critério decisor**: dúvida razoável de que houve incidente? → acione. Melhor superestimar e desescalar do que subestimar.

---

## RELÓGIO DA LGPD ART. 48

A LGPD Art. 48 § 1º exige comunicação à ANPD "em prazo razoável", e a ANPD interpretou esse prazo como **72 horas** a partir da identificação do incidente.

O relógio começa quando há **identificação razoável** do incidente, não quando há confirmação plena. Identificação razoável + incerteza = comunicar.

**Janela**:

| Hora | Ação |
|---|---|
| T+0 | Identificação razoável |
| T+0 a T+2h | Contenção emergencial |
| T+2h a T+24h | Análise inicial + notificação interna |
| T+24h a T+48h | Análise técnica completa + decisão de comunicação |
| T+48h a T+72h | Preparação e envio da comunicação à ANPD |

---

## EQUIPE DE RESPOSTA A INCIDENTES

| Papel | Responsável | Contato |
|---|---|---|
| **Incident Commander** (IC) | [Owner técnico do sistema] | [contato 24/7] |
| **Líder técnico** | [Senior eng + DBA] | [contato] |
| **DPO / Jurídico** | [DPO ou Jurídico Sênior] | [contato] |
| **Comunicação** | [Head de Comunicação] | [contato] |
| **C-level sponsor** | [CTO] | [contato] |
| **Suporte ANPD** | [Jurídico especializado em LGPD] | [contato] |

---

## PASSO A PASSO

### FASE 1 — Identificação e Contenção (T+0 a T+2h)

**Objetivo**: parar o sangramento.

- [ ] **Acionar Incident Commander** (telefone, não chat)
- [ ] **Documentar tudo** desde o primeiro minuto: timestamps, descobertas, hipóteses, ações
- [ ] **Conter**: revogar credenciais comprometidas, desabilitar sistema afetado se necessário, isolar dados afetados
- [ ] **Preservar evidências**: snapshots de logs, screenshots, exports de bancos
- [ ] **Não excluir nada** sob hipótese alguma — preservação de evidências é obrigatória
- [ ] **Notificar** time de segurança da informação interno

**Decisão de FASE 1**: o incidente é real ou alarme falso? Se real, prosseguir. Se falso, documentar e encerrar.

---

### FASE 2 — Notificação interna e análise inicial (T+2h a T+24h)

**Objetivo**: dimensionar o incidente.

- [ ] **Notificar Comitê de IA** (e-mail formal + chamada de alinhamento)
- [ ] **Notificar C-level sponsor** (CEO/CTO conforme criticidade)
- [ ] **Iniciar análise de impacto**:
  - Quantos titulares afetados?
  - Que tipo de dados foram afetados? (identificação, contato, financeiro, sensível Art. 11?)
  - Houve tratamento por terceiros?
  - Houve transferência internacional?
  - Há prejuízo material identificado?
- [ ] **Convocar reunião de gabinete de crise** (IC + DPO + Jurídico + C-level)
- [ ] **Documentar tudo** em registro centralizado (planilha ou ferramenta de IR)

---

### FASE 3 — Análise técnica e decisão (T+24h a T+48h)

**Objetivo**: ter os fatos para a decisão de comunicar.

- [ ] **Concluir análise forense** quando aplicável
- [ ] **Confirmar quantitativo de titulares afetados**
- [ ] **Confirmar tipos de dados** envolvidos
- [ ] **Avaliar risco aos titulares** (alto/médio/baixo)
- [ ] **Identificar causa raiz** preliminar
- [ ] **Decisão de comunicação à ANPD**:
  - Houve afetação de dados pessoais? sim → comunicar
  - Houve risco relevante aos titulares? sim → comunicar
  - Dúvida razoável? → comunicar (melhor pecar por excesso)

A decisão é colegiada: IC + DPO + Jurídico + C-level. Documentar critério.

---

### FASE 4 — Comunicação à ANPD (T+48h a T+72h)

**Objetivo**: cumprir LGPD Art. 48 dentro do prazo.

- [ ] **Acessar portal ANPD** para comunicação de incidente: https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicacao-de-incidente-de-seguranca
- [ ] **Preencher formulário** com:
  - Descrição da natureza do incidente
  - Categorias e quantidade de titulares afetados
  - Categorias e quantidade de registros afetados
  - Medidas técnicas e de segurança utilizadas (antes e durante)
  - Riscos relacionados ao incidente
  - Medidas adotadas para reverter ou mitigar
  - Tempo decorrido entre identificação e comunicação
- [ ] **Anexar evidências** quando disponíveis (sem expor dados de titulares)
- [ ] **Enviar dentro da janela 72h**
- [ ] **Documentar comprovante de envio**

---

### FASE 5 — Comunicação a titulares afetados (quando aplicável)

LGPD Art. 48 § 2º exige comunicação aos titulares quando o incidente puder acarretar risco ou dano relevante.

- [ ] **Avaliar com Jurídico** se comunicação a titulares é obrigatória
- [ ] **Preparar comunicação clara, transparente** (sem juridiquês):
  - O que aconteceu
  - Quais dados foram afetados
  - Quais riscos
  - O que está sendo feito
  - O que o titular pode fazer
  - Canal de contato para dúvidas
- [ ] **Enviar** pelo canal apropriado (e-mail, app, SMS conforme contexto)
- [ ] **Manter canal de atendimento** ativo para responder dúvidas

---

### FASE 6 — Postmortem e melhoria contínua (T+72h+)

**Objetivo**: aprender e evitar repetição.

- [ ] **Postmortem técnico** com causa raiz e timeline
- [ ] **Postmortem de governança** sobre detecção e resposta
- [ ] **Plano de ação** com responsáveis e prazos
- [ ] **Atualização do AI Card** do sistema afetado
- [ ] **Atualização desta política/runbook** com aprendizados
- [ ] **Comunicação ao Comitê de IA** sobre aprendizados

---

## TEMPLATES DE COMUNICAÇÃO

### Template: notificação interna inicial

```
ASSUNTO: [URGENTE] Possível incidente de segurança em [SISTEMA]

A equipe de [SISTEMA] identificou em [TIMESTAMP] possível incidente de
segurança envolvendo dados pessoais. Equipe de resposta foi acionada.

Status: em contenção / em análise / sob controle
Impacto preliminar: [titulares afetados estimados]
Próximo update: [hora]

Incident Commander: [Nome]
```

### Template: comunicação aos titulares (estrutura)

```
Prezado(a) [Nome do titular],

Em [DATA], identificamos uma falha de segurança que afetou alguns dos
seus dados pessoais sob nossa responsabilidade.

O que aconteceu: [descrição clara, sem juridiquês]
Quais dados: [tipos específicos]
Quais riscos: [risco específico se aplicável]
O que estamos fazendo: [medidas adotadas]
O que você pode fazer: [orientações práticas]

Dúvidas: [canal de contato dedicado]

Reportamos este incidente à Autoridade Nacional de Proteção de Dados
(ANPD) em [DATA], conforme LGPD.

[Nome do responsável], [função]
[Empresa]
```

### Template: comunicação à ANPD (estrutura)

O formulário oficial cobre os campos. Manter linguagem:
- Factual, sem evasivas
- Cronológica, com timestamps
- Específica em números (titulares, registros)
- Transparente sobre medidas adotadas

---

## CHECKLIST FINAL DO IC

Antes de fechar o incidente (após Fase 6):

- [ ] Causa raiz identificada e mitigada
- [ ] Comunicação ANPD enviada (ou decisão documentada de não comunicar com justificativa)
- [ ] Comunicação a titulares enviada (ou decisão de não comunicar)
- [ ] Postmortem completo arquivado
- [ ] Plano de ação aprovado pelo Comitê de IA
- [ ] AI Card atualizado
- [ ] Lições aprendidas comunicadas a stakeholders relevantes

---

## REFERÊNCIAS

- LGPD Art. 48 (comunicação de incidente)
- LGPD Art. 49 (medidas urgentes para prevenir riscos)
- ANPD — Guia Orientativo sobre comunicação de incidente: https://www.gov.br/anpd/pt-br
- ANPD — Resoluções aplicáveis (verificar mais recente)

---

## CONTROLE DE VERSÕES

| Versão | Data | Mudanças | Aprovador |
|---|---|---|---|
| 1.0 | [DATA] | Versão inicial | Comitê de IA |

---

*Template baseado em práticas observadas em incidentes reais reportados publicamente e em guias da ANPD. Não é parecer jurídico. Antes de adotar, valide com jurídico interno especializado em LGPD.*
