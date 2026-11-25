# Modelos — Snapshot

> **Snapshot 2026-11-25**
> Atualizado em: 2026-11-25 (Claude Fable 5.2 e Mythos 5.2; GPT-6.2 Astra e Sol; Gemini 4 Argon GA em 13/10 — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-11-01
> Próxima atualização: dezembro/2026 (checagem mensal)
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Famílias rastreadas

| Família | Fornecedor | Tier alto | Tier médio | Tier baixo | Open weights |
|---|---|---|---|---|---|
| **Claude** | Anthropic | Fable/Mythos (fronteira) / Opus | Sonnet | Haiku | Não |
| **GPT** | OpenAI | GPT-6.2 Astra | GPT-6.2 Sol / GPT-6.1 Terra | GPT-6 Luna | Não |
| **Gemini** | Google DeepMind | Gemini 4 Argon / Gemini 3.1 Pro | Gemini Flash (família 3.x) | Gemini Flash-Lite | Não (varia) |
| **Llama** | Meta | 405B+ | 70B | 8B | Sim |
| **Mistral** | Mistral AI | Large | Medium | Small | Parcial |
| **Qwen** | Alibaba | Max | Plus | Turbo | Sim |
| **DeepSeek** | DeepSeek | R-series | V-series | — | Sim |

---

## Claude — geração 4.x/5 e classe Mythos (Anthropic)

Anthropic mantém múltiplas gerações ativas. Em novembro/2026, a estrutura tem três camadas: a classe de fronteira Mythos (Fable 5.2 / Mythos 5.2 desde 09/11) acima do trio de trabalho, o tier Opus (Opus 5.5 como topo e ponto de partida recomendado) e os tiers Sonnet/Haiku (Sonnet 5.5 e Haiku 5.5).

### Modelos correntes (novembro 2026)

| Modelo | API ID (Claude API) | Posicionamento | Janela de contexto |
|---|---|---|---|
| **Claude Fable 5.2** | `claude-fable-5-2` | Fronteira (09/nov/2026); raciocínio exigente e agentes de horizonte longo; Fast mode disponível; effort padrão high; exige retenção de 30 dias salvo autorização ou EFS | 1M tokens (saída 128K) |
| **Claude Mythos 5.2** | `claude-mythos-5-2` | Mesmo modelo do Fable 5.2, para organizações verificadas (Cyber Verification Program, Life Sciences Verification Program ou Claude Security no Enterprise) | 1M tokens (saída 128K) |
| **Claude Fable 5.1** (geração anterior) | `claude-fable-5-1` | Fronteira de set/2026; retirada não antes de 01/set/2027 | 1M tokens (saída 128K) |
| **Claude Mythos 5.1** (geração anterior) | — | Mesma classe, acesso restrito | 1M tokens |
| **Claude Opus 5.5** | `claude-opus-5-5` | Topo do tier Opus (GA 22/set/2026) e ponto de partida recomendado pela Anthropic; thinking sempre ligado, effort padrão medium; retirada não antes de 22/set/2027 | 1M tokens (saída 128K) |
| **Claude Sonnet 5.5** | `claude-sonnet-5-5` | Equilíbrio velocidade/inteligência (GA 28/set/2026); retirada não antes de 28/set/2027 | 1M tokens (saída 128K) |
| **Claude Fable 5** | `claude-fable-5` | Fronteira de jun/2026 (geração anterior); retirada não antes de 09/jun/2027 | 1M tokens |
| **Claude Mythos 5** | `claude-mythos-5` | Mesmo modelo do Fable, salvaguardas de cyber removidas; restrito (Project Glasswing) | 1M tokens |
| **Claude Opus 5** | `claude-opus-5` | Tier Opus de jul/2026; recebe a resposta das consultas de biologia bloqueadas no Fable (inclusive 5.2); retirada não antes de 24/jul/2027 | 1M tokens |
| **Claude Opus 4.8** | `claude-opus-4-8` | Tier Opus da geração anterior; recebe a resposta das consultas de cibersegurança bloqueadas no Fable (inclusive 5.2); Fast mode removido em 30/nov/2026; retirada não antes de 28/mai/2027 | 1M tokens (200K no Microsoft Foundry) |
| **Claude Sonnet 5** | `claude-sonnet-5` | Tier balanceado de jul/2026; retirada não antes de 30/jun/2027 | 1M tokens |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | Geração anterior do tier balanceado, ainda ativa | 1M tokens |
| **Claude Haiku 5.5** | `claude-haiku-5-5` | Tier pequeno (GA 07/out/2026); volume e latência; primeiro Haiku com effort ajustável (padrão medium) e thinking adaptativo; retirada não antes de 07/out/2027 | 1M tokens (saída 128K) |
| **Claude Haiku 4.5** (geração anterior) | `claude-haiku-4-5-20251001` / alias `claude-haiku-4-5` | Geração anterior; ativo, com piso de retirada (15/out/2026) já vencido e sem aposentadoria anunciada | 200K tokens |

· fonte: https://platform.claude.com/docs/en/about-claude/models/overview e https://platform.claude.com/docs/en/about-claude/model-deprecations · data: 2026-11-25.

**Aposentadorias marcadas.** Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) sai da Claude API em 30/11/2026 (migração para Sonnet 5.5). Claude Opus 4.5 (`claude-opus-4-5-20251101` e `claude-opus-4-5`) foi depreciado em 23/11/2026 e sai em 22/01/2027 (migração para Opus 5.5). Política declarada: aviso mínimo de 60 dias. Fonte: https://platform.claude.com/docs/en/about-claude/model-deprecations

**Geração 5.2 (nov/2026).** Fable 5.2 e Mythos 5.2 em 09/11: primeiro corte de preço do tier de fronteira (US$ 8/40, ante 10/50 no 5.1), Fast mode a US$ 16/80 sem cabeçalho beta, verificação de prefixo do thinking em todas as contas de API, thinking descartado se a conversa migra para fora do par 5.2, advisor restrito ao par 5.2, cerca de 55% menos bloqueios desnecessários que no 5.1. Fontes: https://www.anthropic.com/claude-fable-and-mythos-5-2 e https://platform.claude.com/docs/pt-BR/release-notes/overview

**Nota sobre Claude Fable 5 e Mythos 5.** Lançados em 09/06/2026. Timeline do Fable 5: controles de exportação dos EUA suspenderam o acesso global de 12 a 30/06; redeploy mundial em 01/07; migração para usage credits nos planos pagos em 07/07. Requisições sensíveis sofrem fallback automático: cibersegurança → Opus 4.8; biologia dual-use (virologia, toxicologia, design molecular) → Opus 5. Em 07/08/2026, a Anthropic recalibrou o classificador de biologia, reduzindo fallbacks de biologia em ~85% — salvaguarda é parâmetro vivo, muda sem release de modelo. Mythos 5 tem acesso restrito via Project Glasswing (aprovação necessária).

**Geração 5.1/5.5 (set/2026).** Fable 5.1 e Mythos 5.1 em 01/set, Opus 5.5 em 22/set e Sonnet 5.5 em 28/set. Breaking changes comuns: tool use forçado retorna erro 400, thinking do Opus 5.5 não pode ser desligado, blocos de thinking presos a modelo e conversa, e nova ferramenta de computer use (`computer_toolset_20260801`). Salvaguardas viraram produto: Life Sciences Verification Program (17/set) e Enterprise Frontier Safeguards (01/set). Model Hardware Standard (27/ago) em research preview. Fontes: docs de cada modelo em platform.claude.com/docs/en/models/ e anthropic.com/news.

**Marcação de conteúdo (watermarking).** Modelos Claude lançados a partir de 02/08/2026 embutem watermark estatístico imperceptível no texto gerado e metadados de proveniência C2PA em arquivos suportados, em todas as superfícies, mundialmente (compromisso sob o Artigo 50(2) do EU AI Act, anunciado em 11/08/2026). A marca prova processamento, não autoria. Método: versão do SynthID-Text (Google DeepMind, *Nature*, 2024); aplicação global porque a Anthropic ainda não tem forma durável de escopo regional (razão declarada em 14/08). API de detecção em private preview desde 01/09/2026. Em novembro, a marca foi estendida a modelos anteriores: Mythos 5, Opus 4.7 e Sonnet 4.6 (03/11) e Opus 4.6, Opus 4.5, Sonnet 4.5 e Haiku 4.5 (16/11); nesses de 16/11 e no Sonnet 4.6, `temperature`, `top_p` ou `top_k` fora do padrão podem gerar texto sem marca. Fontes: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content e https://platform.claude.com/docs/pt-BR/release-notes/overview

**Mecânica de versionamento.** A partir da geração 4.6, os IDs de modelo usam formato sem data (ex.: `claude-sonnet-4-6`) que é snapshot fixo, não ponteiro dinâmico. Modelos anteriores à geração 4.6 usam data explícita (ex.: `claude-haiku-4-5-20251001`). Aliases convenientes (ex.: `claude-haiku-4-5`) apontam para a revisão corrente — conveniente para desenvolvimento, perigoso em produção sem teste de regressão.

---

## GPT — geração corrente (OpenAI)

### Modelos correntes (novembro 2026)

| Modelo | Posicionamento | Observação |
|---|---|---|
| **GPT-6.2 Astra** | Flagship (17/11/2026); raciocínio e código mais exigentes | Substitui o GPT-6 Astra como topo |
| **GPT-6.2 Sol** | Código do dia a dia e fluxos de agentes (17/11/2026) | Substitui o GPT-6.1 Sol |
| **GPT-6.1 Terra** | Tier balanceado | Elegível às janelas de background |
| **GPT-6 Luna** | Tier de volume | Elegível às janelas de background |
| **GPT-6 Astra** (geração anterior) | Flagship de 03/09/2026 | |
| **GPT-6.1 Sol** (geração anterior) | Flagship de eficiência de 29/09/2026 | |
| **GPT-5.6 Sol** | Geração anterior | Preço promocional até 30/11/2026 |

· fonte: https://developers.openai.com/api/docs/pricing e https://developers.openai.com/api/docs/changelog · data: 2026-11-25. Linhas GPT-5.6 Terra e Luna e GPT-5.5 Pro retiradas: não aparecem nas páginas oficiais lidas.

**Mudança de contrato no GPT-6.2.** A Responses API descarta itens de raciocínio quando o histórico é editado no meio da conversa ou o modelo é trocado; as `instructions` de topo passam a ser anexadas depois do `input`. Fonte: https://developers.openai.com/api/docs/guides/latest-model

**Nota sobre GPT-4o.** Descontinuado no ChatGPT em 13/02/2026; continua disponível via API.

---

## Gemini — geração corrente (Google DeepMind)

### Modelos correntes (novembro 2026: Argon e 3.8 Flash; 2.5 de junho 2026)

| Modelo | API ID | Posicionamento | Janela de contexto |
|---|---|---|---|
| **Gemini 3.1 Pro** | `gemini-3.1-pro` | Flagship (release 19/02/2026); multimodal, agêntico | 2M tokens |
| **Gemini 4 Argon** | `gemini-4-argon` | GA em 13/10/2026; modelo mais capaz da linha para código complexo, agentes, matemática e ciência; preço dobra em 01/12/2026 | **[a confirmar]** |
| **Gemini 3.8 Flash** | — | GA (set/2026); agentes e código; contexto 1M, saída 64K | 1M tokens |
| **Gemini 2.5 Pro** | `gemini-2.5-pro` | Raciocínio complexo e coding; stable release | 1M tokens |
| **Gemini 2.5 Flash** | `gemini-2.5-flash` | Raciocínio híbrido; velocidade + thinking budgets | 1M tokens |
| **Gemini 2.5 Flash-Lite** | `gemini-2.5-flash-lite` | Menor custo e mais eficiente; alto volume | TBD (a confirmar) |

· fonte: https://ai.google.dev/gemini-api/docs/pricing e https://ai.google.dev/gemini-api/docs/changelog · data: 2026-11-25 (Argon, 3.8 Flash, 3.1 Pro), 2026-06-18 (linhas 2.5). Gemini 4 Neon, Carbon e Hydrogen, citados por fontes secundárias, não aparecem no changelog nem na página de preços oficiais lidos em 25/11 e não entram.

---

## Modelos open-source relevantes

Para CTOs avaliando alternativas com soberania total de dados, modelos abertos com pesos disponíveis são opção. Lista atualizada:

| Modelo | Tamanho | Forte em |
|---|---|---|
| Llama (Meta) | 8B, 70B, 405B+ | Generalista, multilingue |
| Mistral | 7B-Large | Eficiência |
| Qwen (Alibaba) | 7B-72B | Multilingue, código |
| DeepSeek | 67B+ | Raciocínio, matemática |

---

## Mudanças recentes

- **2026-11-25**: Claude Fable 5.2 e Mythos 5.2 (09/11); aposentadorias do Sonnet 4.5 (30/11) e do Opus 4.5 (22/01/2027); pisos de retirada publicados; marca d'água estendida a modelos anteriores. GPT-6.2 Astra e Sol (17/11). Gemini 4 Argon com GA confirmado em 13/10.
- **2026-11-01**: Claude sem mudança de lineup. Gemini 4 Argon e GPT-6.1 Terra aparecem nas páginas oficiais de pricing; datas de lançamento não constam nas páginas.
- **2026-10-09**: Claude Haiku 5.5 (GA 07/10, `claude-haiku-5-5`, 1M de contexto, tokenizer novo, `temperature`, `top_p` e `top_k` não padrão retornam erro 400).
- **2026-10-01**: Fable 5.1, Opus 5.5 e Sonnet 5.5; GPT-6 Astra e 6.1 Sol; Gemini 3.8 Flash; watermark com API de detecção em private preview.
- **2026-08-12**: snapshot atualizado — Claude Opus 5 (GA 24/07) e Sonnet 5 adicionados; timeline do Fable 5 (blackout jun, redeploy 01/07, usage credits 07/07, recalibração bio 07/08); watermarking (modelos ≥ 02/08); família GPT-5.6 (Sol/Terra/Luna, 09/07, corte 30/07); Gemini 3.1 Pro consolidado como flagship.
- **2026-06-18**: snapshot populado com dados correntes — modelos identificados com API IDs e janelas de contexto confirmadas por fonte primária (Anthropic docs, Google AI pricing).
- **2026-06-09**: Anthropic lança Claude Fable 5 (disponibilidade ampla) e Claude Mythos 5 (Project Glasswing, acesso limitado).
- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**Como contribuir.** Observou modelo lançado ou mudança não capturada? Abra issue com label `errata` ou `nova-fonte`. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

- Anthropic Models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- OpenAI Models: https://developers.openai.com/api/docs/models/all
- Google Gemini Models: https://ai.google.dev/gemini-api/docs/models
- Google Gemini Pricing: https://ai.google.dev/gemini-api/docs/pricing

Ver [`FONTES.md`](./FONTES.md) para lista completa com links de docs oficiais.
