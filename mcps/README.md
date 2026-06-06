# MCP — Model Context Protocol

> Tutoriais de uso de servidores MCP oficiais e exemplos próprios para integração com Claude.

---

## Por que esta pasta existe

A obra *Deep Claude*, nos Capítulos 28-29, apresenta MCP como protocolo de integração padrão entre Claude e sistemas externos. Esta pasta carrega tutoriais práticos de uso de servidores MCP oficiais (do MCP Registry da Anthropic e da comunidade) e exemplos próprios de integração ao ecossistema brasileiro.

MCP é o padrão de integração que substituiu "agente que faz tudo via API direta" pelo "agente que descobre ferramentas via protocolo padronizado". Para a fundamentação completa, ver Caps 28-29 do livro.

---

## O que vive aqui

```
mcps/
  README.md                          — este arquivo
  tutorial-mcp-registry-anthropic/   — como navegar e instalar do registry
  tutorial-mcp-stdio-vs-sse/         — diferença entre transports
  exemplo-mcp-simples-python/        — servidor MCP "Hello World" em Python
  exemplo-mcp-com-claude-code/       — integração MCP + Claude Code
  exemplo-mcp-asana-via-claude/      — uso de MCP oficial Asana
```

---

## Cobertura inicial — v1.0 (jul/2026)

Tutoriais para 3 MCPs oficiais relevantes para o leitor brasileiro:

| Tutorial | MCP coberto | Caso de uso |
|---|---|---|
| `tutorial-mcp-asana` | Asana Official MCP | Gestão de projetos |
| `tutorial-mcp-slack` | Slack Official MCP | Comunicação interna |
| `tutorial-mcp-google-drive` | Google Drive MCP | Documentos corporativos |

Cada tutorial cobre:
- Instalação
- Autenticação (OAuth ou token)
- Casos de uso típicos
- Pegadinhas comuns
- Quando NÃO usar

---

## Cobertura roadmap

### v1.1 — out/2026

| Tutorial | MCP |
|---|---|
| `tutorial-mcp-azure-devops` | Azure DevOps (popular no mercado brasileiro corporativo) |
| `tutorial-mcp-notion` | Notion |
| `tutorial-mcp-figma` | Figma (para produtos) |
| `exemplo-mcp-proprio-asaas` | MCP próprio para Asaas (fintech BR) |

### v1.2 — jan/2027

| Tutorial | MCP |
|---|---|
| Padrões avançados: chained tools, parallel execution, error recovery |
| Casos de uso enterprise: SSO, escopos restritivos, audit log |

---

## Princípios

**Tutoriais executáveis.** Cada tutorial tem passos numerados, comandos reais, screenshots quando relevante.

**Segurança em primeiro lugar.** Cada tutorial inclui seção "Quando NÃO usar" e cuidados com credenciais.

**Foco no caso brasileiro.** Priorizamos MCPs relevantes para o stack corporativo brasileiro (Asaas, Azure DevOps, ferramentas governamentais).

**Custos explicitados.** Quando uso de MCP gera custo (API calls, storage, etc.), explicitamos.

---

## MCPs oficiais relevantes

Lista curada de MCPs oficiais com tração:

### Anthropic
- **Claude MCP Server Registry**: https://github.com/anthropics/
- **MCP Servers Reference**: https://github.com/modelcontextprotocol/servers

### Empresas (oficiais)
- **GitHub MCP**: github.com/github/github-mcp-server
- **Slack MCP**: anthropic registry
- **Linear MCP**: linear.app docs
- **Notion MCP**: notion.so docs
- **Asana MCP**: anthropic registry

### Brasil
*MCPs específicos para empresas brasileiras estão emergindo. Esta seção será atualizada conforme tração.*

---

## Como contribuir

Você é mantenedor ou usuário de MCP relevante e quer contribuir com tutorial?

1. Abra issue com label `novo-mcp` e descrição
2. Aguarde alinhamento
3. Abra PR com tutorial completo + exemplos
4. Tutorial passa por revisão editorial

Veja [CONTRATO.md](../CONTRATO.md) para princípios completos.

---

## Capítulos relacionados

- **Cap 28 — MCP Fundamentos**: protocolo, arquitetura, padrões
- **Cap 29 — MCP Avançado**: integração com Claude Code, padrões enterprise
- **Cap 20 — Connectors/Dispatch/Routines**: outra forma de integração no Claude Web/Cowork

---

## Referências oficiais

- **Spec MCP**: https://modelcontextprotocol.io/
- **Servidores oficiais**: https://github.com/modelcontextprotocol/servers
- **Quickstart Anthropic**: https://docs.anthropic.com/en/docs/build-with-claude/mcp
