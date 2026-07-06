# Changelog — Atualização de rodada de modelos (2026-07-05)

**Motivo:** Sonnet 5 (30/jun) e o retorno de Fable 5 / Mythos 5 (redeploy 1/jul, com novo modelo de precificação por *usage credits* a partir de 7/jul) saíram antes do lançamento do L2. Como o L2 é o volume vivo (Invariante 3 — Camada Dupla), a atualização entra no **Apêndice Vivo (APX-J)**, não espalhada pelo corpo.

**Fonte primária (consultada 2026-07-05, número por linha):**
- [Pricing oficial](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anúncio Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) (30/jun)
- [Anúncio Fable 5 / Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) (9/jun)
- [Redeploy do Fable 5](https://www.anthropic.com/news/redeploying-fable-5) (30/jun → 1/jul; corte de créditos 7/jul)
- [Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)

## O que mudou

### APX-J — Apêndice Vivo (bloco principal)
- Snapshot bumpado **v0.1 (31/mai) → v0.2 (05/jul)**; nota de método (número por linha, nada estimado).
- **§1.1 Família Claude** populada:
  - Tabela de lineup + preços por MTok: Fable 5 ($10/$50), Mythos 5 (restrito, $10/$50), Opus 4.8 ($5/$25), Sonnet 5 intro ($2/$10 até 31/ago) e padrão ($3/$15 a partir de 1/set), Haiku 4.5 ($1/$5); batch, cache read, IDs de API.
  - Multiplicadores de cache (5min 1,25× / 1h 2× / read 0,1×).
  - **Tier de fronteira (classe Mythos) acima de Opus** — nota de rodapé oficial: Mythos-class fica acima do Opus; Fable = versão com salvaguardas, Mythos = sem salvaguardas de cyber (restrito).
  - **Tokenizer novo** (Opus 4.7+, Fable 5, Mythos 5, Sonnet 5): mesmo texto → ~1,0–1,35× mais tokens; intro do Sonnet 5 calibrado p/ custo-neutro vs Sonnet 4.6.
  - **Modelo de precificação por *usage credits*** (o ponto que o Fabio pediu): tabela plano-a-plano (Pro/Max/Team/Enterprise premium: incluído até 50% dos limites semanais até 7/jul, depois créditos; Enterprise standard: créditos desde o dia 1; API: metered; marketplaces: CCU, 100 CCU = US$1). Box do que a Anthropic **não** publicou (conversão crédito→dólar). Linha do tempo do Fable (dois cortes; o de 23/jun evaporou no blackout de exportação).
  - Box "Leitura durável": o padrão que fica (tier de fronteira surge acima do topo; acesso migra de assinatura fixa p/ crédito medido; a decisão durável é a política de roteamento — Inv. 4 sobre Inv. 3).
- **§5 Padrões de preço**: tabela por tier ancorada nos números Claude correntes; padrão a reter (razão input:output 1:5; degraus dobram/halvam).
- Tabela de controle de versão: linha v0.2 registrada.

### Corpo (retoques leves de consistência — o durável fica)
- **C02** (linha do tempo): trio Opus/Sonnet/Haiku descrito como espinha dorsal, "agora com uma camada de fronteira acima (classe Mythos)"; aponta p/ APX-J.
- **C04** (todos os modelos Claude): novo parágrafo "tier de fronteira (classe Mythos) acima do trio" em 4.3.1 + linha no resumo executivo. Preserva a analogia do carpinteiro e a tese encaixe>preço; nomes/preços/cobrança remetidos ao APX-J.
- **C05** (quando usar): exemplos de versão atualizados (Fable 5, Opus 4.8, Sonnet 5, Haiku 4.5) + menção ao mecanismo de cobrança vigente.

### Entregáveis
- `Deep-Claude-EDICAO-DIGITAL.pdf` (990 págs) e `.html` regerados via `gerar-l2.py`.

## Deliberadamente NÃO feito
- Não populei números de concorrentes (GPT, Gemini, Grok) nem líderes de benchmark — sem fonte primária confirmada nesta rodada; ficam para v0.3 (marcado no apêndice). Princípio: não fabricar número.
- Nada de preço/versão espalhado pelo corpo além dos retoques de consistência — a tese "método > catálogo" exige que o volátil more só no APX-J.
