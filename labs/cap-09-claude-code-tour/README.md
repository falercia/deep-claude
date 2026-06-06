# Lab — Capítulo 9: Claude Code Tour

> Tour executável de 30 minutos do Claude Code para desenvolvedor brasileiro.
> Versão 1.0 — 2026-07

---

## Objetivo

Você vai sair deste lab capaz de:

- Instalar Claude Code
- Autenticar e fazer primeira sessão
- Navegar em um codebase real com o Claude Code
- Usar slash commands principais
- Configurar um hook simples
- Instalar e usar um skill
- Conectar um MCP

## Pré-requisitos

- macOS 13+, Linux moderno, ou Windows 11 com WSL2
- Node.js 20+ instalado
- Git
- Editor de código (VS Code, Cursor, ou outro)
- Conta Anthropic com créditos (USD 5 são suficientes para o tour)

## Tempo estimado

30 minutos.

## Passos

### Passo 1 — Instalação (5 min)

```bash
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | sh

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

Verifique:

```bash
claude --version
```

### Passo 2 — Autenticação (3 min)

```bash
claude
```

Na primeira vez, abre browser para login. Use conta Anthropic.

### Passo 3 — Primeira sessão (5 min)

Clone um repositório de exemplo:

```bash
git clone https://github.com/anthropics/anthropic-cookbook.git
cd anthropic-cookbook
claude
```

Dentro do Claude Code, peça:

> "Resume a estrutura deste repositório e identifica os 3 exemplos mais úteis para alguém começando com Claude"

Observe como o Claude lê arquivos, agrega informação e estrutura resposta.

### Passo 4 — Slash commands (5 min)

Dentro do Claude Code, experimente:

- `/help` — lista comandos disponíveis
- `/model` — alterna entre Opus / Sonnet / Haiku
- `/cost` — mostra custo da sessão atual
- `/clear` — limpa contexto
- `/agents` — lista subagentes disponíveis

### Passo 5 — Configurar um hook (5 min)

Hooks são scripts que rodam em eventos do Claude Code.

Crie `~/.claude/hooks/on-session-start.sh`:

```bash
#!/bin/bash
echo "[$(date)] Sessão iniciada em $(pwd)" >> ~/claude-sessions.log
```

```bash
chmod +x ~/.claude/hooks/on-session-start.sh
```

Reinicie o Claude Code. A cada sessão, log é gravado.

### Passo 6 — Instalar um skill (5 min)

Use o skill `analise-juridica-br` deste repositório (para teste):

```bash
mkdir -p ~/.claude/skills
ln -s /caminho/para/deep-claude/skills/analise-juridica-br ~/.claude/skills/analise-juridica-br
```

Dentro do Claude Code, peça:

> "Analise este contrato de exemplo: [cole um contrato fictício]"

O skill ativa e estrutura a análise.

### Passo 7 — Conectar um MCP (2 min)

Edite `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/Users/seu-user/Documents"]
    }
  }
}
```

Reinicie Claude Code.

```bash
/mcp list
```

Deve listar `filesystem` ativo. Agora o Claude pode ler `~/Documents` via MCP.

## Validação

Você completou o lab quando:

- ✅ Claude Code instalado e funcional
- ✅ Sessão iniciada e usada em codebase real
- ✅ Slash commands explorados
- ✅ Hook configurado e funcionando
- ✅ Skill instalado e acionado
- ✅ MCP conectado e usado

## Próximos passos

- Lab Cap 21 — Primeira chamada à API
- Lab Cap 30 — Construir skill do zero
- Cap 9 do livro para fluxos profissionais avançados

## Conexão com o livro

- Cap 9 — Claude Code (fundamentação completa)
- Cap 30 — Claude Skills
- Cap 28-29 — MCP

## Versão

1.0 — 2026-07
