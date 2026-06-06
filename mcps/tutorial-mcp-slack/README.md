# Tutorial: Slack MCP

> Como instalar e usar o servidor MCP oficial do Slack com Claude.
> Calibrado para uso corporativo brasileiro.
> Versão 1.0 — 2026-07

---

## Para que serve

Expõe principais recursos do Slack para Claude:

- Ler mensagens de canais
- Enviar mensagens
- Buscar histórico
- Listar canais e usuários
- Criar/atualizar threads

Casos típicos:

- "Envia uma mensagem no canal #release-comms anunciando o deploy de hoje"
- "Resume as últimas 50 mensagens do canal #engenharia"
- "Quais ações foram acordadas na thread Y do canal Z?"

## Pré-requisitos

- Workspace Slack onde você é admin (ou tem permissão de criar app)
- Claude Code ou Cowork

## Instalação

### 1. Criar Slack App

1. Acesse https://api.slack.com/apps
2. "Create New App" > "From scratch"
3. Nome: "Claude Integration" (ou nome da casa)
4. Workspace de destino

### 2. Configurar permissões (OAuth Scopes)

Em **Bot Token Scopes**, adicione (escopo mínimo para uso típico):

- `channels:read`
- `channels:history`
- `chat:write`
- `users:read`
- `groups:read` (se canais privados)

**Não adicione** escopos que não vai usar. Princípio do menor privilégio.

### 3. Instalar app no workspace

Em "Install App", clique em "Install to Workspace".

Copie o **Bot User OAuth Token** (começa com `xoxb-`).

### 4. Configurar Claude Code

Edite `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "slack": {
      "command": "node",
      "args": ["/caminho/para/slack-mcp/index.js"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-seu-token-aqui",
        "SLACK_TEAM_ID": "Tseuteamid"
      }
    }
  }
}
```

Reinicie Claude Code.

### 5. Verificar

```bash
claude mcp list
```

No chat:

> "Liste os canais do meu workspace Slack"

## Casos de uso

### Caso 1 — Resumo executivo de canal

**Prompt**:

> "Resume as últimas 100 mensagens do canal #engenharia-leads, destacando decisões, blockers e próximos passos"

Claude lê histórico e produz síntese estruturada.

### Caso 2 — Comunicação proativa

**Prompt**:

> "Anuncia no canal #release-comms o deploy de hoje às 14h: versão 4.2.0, com release notes em [URL]"

Claude formata e envia.

### Caso 3 — Análise de thread

**Prompt**:

> "Identifica as decisões e responsáveis acordados na thread iniciada por @joao em #produto, ontem"

Claude busca a thread e extrai estrutura de decisão.

## Pegadinhas comuns

**Bot user no canal**. O bot só lê canais onde foi convidado (`/invite @nome-do-bot`).

**Rate limit**. Slack tem limites por tier. Tier 1 e 2 são generosos; tier 3 e 4 podem precisar batching.

**Mensagens efêmeras**. Não são acessíveis via API histórica. Algumas DMs também não.

**Privacidade**. Canais privados e DMs podem conter informação sensível. Avalie escopo do bot com cuidado.

**Soberania**. Slack opera em datacenters globais. Para dados sob LGPD restritiva, avalie políticas.

## Quando NÃO usar

- **Mensagens diretas (DMs) sensíveis** sem consentimento dos envolvidos
- **Substituição de comunicação humana** em casos críticos (incidentes, conflitos)
- **Automação de aprovações** sem revisão humana

## Limitações

- Sem suporte completo a Slack Connect entre workspaces (em algumas versões)
- Reações em mensagens podem ter cobertura parcial
- Huddles e Canvases não são cobertos

## Conexão com o livro

- Cap 28 — MCP Fundamentos
- Cap 29 — MCP Avançado
- Cap 39 — Casos SaaS + Suporte (comunicação interna em SaaS)

## Referências

- Slack API: https://api.slack.com/
- MCP Spec: https://modelcontextprotocol.io/

## Versão

1.0 — 2026-07
