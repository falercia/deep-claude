# Tutorial: Google Drive MCP

> Como instalar e usar o servidor MCP do Google Drive com Claude.
> Calibrado para uso corporativo brasileiro.
> Versão 1.0 — 2026-07

---

## Para que serve

Expõe recursos do Google Drive para Claude:

- Listar e ler documentos (Docs, Sheets, Slides)
- Buscar arquivos por nome ou conteúdo
- Criar e editar documentos
- Compartilhar com usuários
- Mover, copiar, renomear arquivos

Casos típicos:

- "Lê o documento de RFC de M&A e me resume os pontos críticos"
- "Cria uma planilha com os indicadores do quarter"
- "Busque todos os documentos com a palavra 'arquitetura' criados no último mês"

## Pré-requisitos

- Conta Google Workspace (corporativa recomendada)
- Acesso a Google Cloud Console (para criar credenciais OAuth)
- Claude Code ou Cowork

## Instalação

### 1. Criar projeto no Google Cloud Console

1. Acesse https://console.cloud.google.com/
2. Criar projeto (ex: "Claude Integration")
3. Ativar APIs: Google Drive API, Google Docs API, Sheets API

### 2. Configurar OAuth 2.0

1. APIs e Serviços > Credenciais
2. Criar credencial OAuth 2.0 (Desktop App)
3. Baixar o JSON de credenciais (`credentials.json`)

### 3. Configurar Claude Code

Edite `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "google-drive": {
      "command": "node",
      "args": ["/caminho/para/gdrive-mcp/index.js"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/caminho/para/credentials.json",
        "GOOGLE_TOKEN_PATH": "/caminho/para/token.json"
      }
    }
  }
}
```

### 4. Autenticação inicial

Primeira vez que rodar, o servidor abre URL OAuth no browser. Autentique-se. Token é salvo localmente.

### 5. Verificar

```bash
claude mcp list
```

No chat:

> "Liste os documentos modificados ontem no meu Drive"

## Casos de uso

### Caso 1 — Análise de documento

**Prompt**:

> "Lê o documento 'Arquitetura Atlas v3' do meu Drive e identifica trade-offs, decisões pendentes e dependências críticas"

Claude lê via MCP e estrutura análise.

### Caso 2 — Criação de planilha

**Prompt**:

> "Cria uma planilha 'Indicadores Q3' no Drive, com colunas: KPI, Valor, Meta, Status, Owner. Popula com os dados que discutimos"

Claude cria e popula.

### Caso 3 — Busca semântica

**Prompt**:

> "Buscar todos os documentos do Drive que tratem de migração para nuvem nos últimos 90 dias"

Claude busca, filtra e devolve lista organizada.

## Pegadinhas comuns

**OAuth com escopos amplos**. Google Drive tem escopos granulares. Use `drive.readonly` se só vai ler, em vez de `drive` (escrita também).

**Documentos compartilhados**. MCP só acessa documentos onde a conta autenticada tem permissão.

**Quotas**. Drive API tem quotas por projeto. Volume alto pode esgotar; considere quota incrementada via console.

**Dados sensíveis**. Documentos podem conter PII, contratos, dados financeiros. Avalie políticas LGPD da casa antes de uso.

**Soberania**. Google opera datacenters globais. Para dados altamente sensíveis sob LGPD, considere alternativas com soberania nacional.

**Versão do documento**. MCP lê versão atual; mudanças em tempo real podem gerar inconsistência se Claude estiver analisando enquanto alguém edita.

## Quando NÃO usar

- **Documentos com PII massiva** sem anonimização
- **Documentos confidenciais** sem revisão de escopo de acesso
- **Automação de aprovações** sem revisão humana
- **Substituição de DLP corporativo** (Data Loss Prevention)

## Limitações

- Google Workspace Education tem APIs limitadas
- Comentários em Docs têm cobertura parcial em algumas versões
- Documentos protegidos por IRM/DLP podem ser inacessíveis

## Conexão com o livro

- Cap 28 — MCP Fundamentos
- Cap 29 — MCP Avançado
- Cap 27 — RAG (Drive como fonte de conhecimento corporativo)
- Cap 44 — LGPD (cuidado com dados sensíveis)

## Referências

- Google Drive API: https://developers.google.com/drive/api
- Google Workspace Admin: https://admin.google.com/
- MCP Spec: https://modelcontextprotocol.io/

## Versão

1.0 — 2026-07
