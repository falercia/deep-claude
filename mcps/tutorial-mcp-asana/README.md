# Tutorial: Asana MCP

> Como instalar e usar o servidor MCP oficial do Asana com Claude.
> Calibrado para uso corporativo brasileiro.
> Versão 1.0 — 2026-07

---

## Para que serve

O servidor MCP do Asana expõe os principais recursos da plataforma de gestão de projetos para Claude:

- Listar e ler tasks
- Criar tasks com atribuição, prazo, projeto
- Atualizar status de tasks
- Listar projetos e portfólios
- Buscar workspaces e teams

Casos típicos para CTO/Tech Lead:

- "Cria uma task no projeto X com prazo amanhã e atribui ao João"
- "Quais tasks estão atrasadas no sprint atual?"
- "Resume todas as tasks de bug abertas na última semana"

## Pré-requisitos

- Conta Asana com acesso ao workspace
- Personal Access Token (PAT) do Asana
- Claude Code instalado, ou Cowork conectado

## Instalação

### 1. Gerar Personal Access Token no Asana

1. Acesse https://app.asana.com/0/my-apps
2. Clique em "Personal Access Tokens"
3. Crie um novo token com nome descritivo (ex: "Claude Integration")
4. Copie o token gerado (atenção: você só verá uma vez)

### 2. Instalar servidor MCP

Verifique disponibilidade no MCP Registry da Anthropic (ver Apêndice Vivo `/apendice-vivo/MODELOS.md` para registry atualizado).

```bash
# Via npm (exemplo — verificar nome oficial no Registry)
npm install -g @anthropic/mcp-asana

# Ou via instalação manual de servidor próprio
git clone https://github.com/[repo-oficial-asana-mcp]
cd asana-mcp
npm install
```

### 3. Configurar Claude Code

Edite `~/.claude/config.json` (ou via UI do Claude Code):

```json
{
  "mcpServers": {
    "asana": {
      "command": "node",
      "args": ["/caminho/para/asana-mcp/index.js"],
      "env": {
        "ASANA_PAT": "seu_pat_aqui",
        "ASANA_WORKSPACE_ID": "seu_workspace_id"
      }
    }
  }
}
```

Reinicie o Claude Code.

### 4. Verificar instalação

```bash
claude mcp list
# Deve listar "asana" como ativo
```

No chat, pergunte:

> "Liste meus projetos no Asana"

Se Claude responder com a lista, está funcionando.

## Casos de uso

### Caso 1 — Triagem de tasks atrasadas

**Prompt**:

> "Liste todas as tasks atrasadas no projeto Atlas atribuídas ao meu time, agrupadas por responsável"

Claude usa o MCP para:
1. Buscar projeto Atlas
2. Filtrar tasks com prazo expirado
3. Agrupar por assignee
4. Apresentar tabela resumida

### Caso 2 — Criação em lote

**Prompt**:

> "Para cada bug que mencionei na conversa, crie uma task no projeto Bugs com severidade no título e prazo de 7 dias"

Claude itera, cria tasks e devolve confirmação.

### Caso 3 — Síntese executiva

**Prompt**:

> "Resume o status do projeto Atlas: tasks por status, prazos críticos próximos, blockers identificados"

Claude consulta o projeto e estrutura resposta executiva.

## Pegadinhas comuns

**Token com escopo amplo demais**. PAT no Asana é all-or-nothing. Se sua casa exige privilégio mínimo, use conta de serviço dedicada com acesso só aos workspaces necessários.

**Rate limit**. Asana tem limite de ~150 req/min. Para volumes altos, considere batching e cache.

**Privacidade**. Tasks contendo dados sensíveis (clientes, financeiro) podem virar contexto do LLM. Evalue se o caso justifica.

**Soberania**. API do Asana é em datacenters americanos. Para dados sensíveis sob LGPD, avalie alternativas com soberania nacional ou anonimização pré-prompt.

## Quando NÃO usar

- **Casos enterprise com dados altamente sensíveis** sem revisão jurídica
- **Automação de aprovações críticas** sem revisão humana
- **Substituição completa do PM** (skill é apoio, não substituição)

## Limitações

- Sem suporte para Asana Goals (em algumas versões)
- Sem suporte para Portfolios em planos não-corporate
- Comentários em tasks têm formatação limitada na API

## Conexão com o livro

- **Cap 28 — MCP Fundamentos**
- **Cap 29 — MCP Avançado**
- **Cap 20 — Connectors / Dispatch / Routines** (alternativa via Cowork)

## Referências

- Asana API: https://developers.asana.com/docs
- MCP Spec: https://modelcontextprotocol.io/
- Anthropic Registry: ver Apêndice Vivo

## Versão

1.0 — 2026-07
