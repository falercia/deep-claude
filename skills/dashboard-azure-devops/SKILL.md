---
name: dashboard-azure-devops
description: Skill para gerar dashboards executivos a partir de dados do Azure DevOps. Acionar quando usuário pedir "dashboard Azure DevOps", "métricas do sprint", "indicadores de engenharia", "DORA metrics", "velocity do time" ou similar, em contexto de gestão de engenharia.
version: 1.0
---

# Dashboard Azure DevOps

## Quando ativar

Acione quando o usuário pedir indicadores executivos de engenharia a partir do Azure DevOps:

- "Gera um dashboard das sprints recentes"
- "Indicadores de velocity"
- "DORA metrics do time"
- "Lead time, MTTR, deployment frequency"
- "Visão executiva da engenharia"
- "Relatório quinzenal para diretoria"

**Não ative** para:

- Operações de criação/edição em ADO (use MCP específico)
- Debug de pipelines (use ferramenta de CI)
- Gestão de bugs individuais (use UI do ADO)

## O que faz

Produz visão executiva consolidada com 4 blocos:

1. **DORA Metrics**: Deployment Frequency, Lead Time for Changes, MTTR, Change Failure Rate
2. **Velocity e previsibilidade**: story points concluídos, previsibilidade vs planejado, debt acumulada
3. **Quality**: bugs em aberto, bugs por severidade, escape rate (bugs em produção)
4. **Síntese executiva**: 3-5 frases para CTO/CFO

## Configurações

```xml
<contexto>
  <organizacao>{{nome_da_org}}</organizacao>
  <projetos>{{lista_de_projetos}}</projetos>
  <periodo>{{semana | quinzena | mes | trimestre}}</periodo>
  <audiencia>{{tech_leads | C_level}}</audiencia>
</contexto>
```

## Dependências

Skill assume acesso ao Azure DevOps via:

- API REST com PAT (Personal Access Token)
- Ou MCP oficial do Azure DevOps (quando disponível)

Configure credenciais antes de uso.

## Saída esperada

Tabela executiva + comentário curto + sinalização de alertas (red flags).

Exemplo de bloco DORA:

| Métrica | Valor | Tendência | Status |
|---|---|---|---|
| Deployment Frequency | 4.2/dia | ↑ vs sprint anterior | Elite |
| Lead Time for Changes | 1.8 dias | → estável | High |
| MTTR | 4.5h | ↓ melhorou | Elite |
| Change Failure Rate | 8% | ↑ piorou | High |

**Síntese**: time mantém cadência elite em deployment frequency e MTTR; CFR subiu 3 pontos no último ciclo, sugerindo revisar testes de regressão antes de release.

## Modelo recomendado

- Claude Sonnet (suficiente para análise estruturada)
- Temperature 0.0 (consistência em métricas)

## Conexões

- Cap 9 — Claude Code (uso em pipeline)
- Cap 35 — LLMOps (observabilidade)
- Cap 22 — Tool Use (chamadas a APIs externas)
