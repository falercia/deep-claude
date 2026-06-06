# Skill — dashboard-azure-devops

> Skill para gerar dashboards executivos a partir do Azure DevOps.
> Versão 1.0 — 2026-07

---

## Para quem é

Para CTOs, Heads de Engenharia, Tech Leads e Gerentes de Engenharia que usam Azure DevOps e precisam de visão executiva consolidada em ciclos curtos (semana, sprint, mês).

## Como instalar

### Em Claude Code

```bash
ln -s /caminho/para/deep-claude/skills/dashboard-azure-devops ~/.claude/skills/dashboard-azure-devops
```

### Configuração de credenciais

Crie Personal Access Token (PAT) no Azure DevOps com escopos:

- `vso.work` (work items)
- `vso.code` (repositórios)
- `vso.build` (pipelines)
- `vso.release` (releases)

Armazene em variável de ambiente:

```bash
export AZURE_DEVOPS_PAT="seu_pat_aqui"
export AZURE_DEVOPS_ORG="sua_org"
```

## Como usar

Após instalar e configurar credenciais:

> "Gera dashboard DORA do projeto Atlas referente à última quinzena"
> "Indicadores executivos do time de plataforma do mês"
> "Relatório de velocity dos times de produto trimestre 3"

## Saída

Bloco DORA Metrics + Velocity + Quality + Síntese executiva.

## Limitações

- Funciona com ADO Cloud (não testado em Server)
- Não cobre Boards Classic (usa apenas Agile/Scrum/Basic)
- Requer dados mínimos no ADO (sem dados, sem dashboard)

## Conexão com o livro

- Cap 9 — Claude Code
- Cap 22 — Tool Use
- Cap 35 — LLMOps

## Versão

1.0 — 2026-07
