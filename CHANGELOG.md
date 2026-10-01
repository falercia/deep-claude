# Changelog

Todas as mudanças relevantes deste repositório são registradas aqui, em ordem cronológica reversa, com data, autor e fonte primária quando aplicável.

O formato segue [Keep a Changelog](https://keepachangelog.com/) e o versionamento segue [Semantic Versioning](https://semver.org/).

---

## [1.2.0] — 2026-10-01

**Ciclo de setembro e outubro: geração Claude 5.1/5.5, cobrança além do token e três correções de interpretação.**

### Adicionado

- **L2-APX-J → v0.5**: Fable 5.1 e Mythos 5.1 (01/set, cache read US$ 0,25), Opus 5.5 (22/set, US$ 4/20) e Sonnet 5.5 (28/set, US$ 2/10); breaking changes de API da geração 5.x; betas de API; bloco "Cobrança deixou de ser só por token" (session-hour, residência 1,1x, ferramentas, Fast mode); salvaguardas como produto (Life Sciences Verification Program, Enterprise Frontier Safeguards); Model Hardware Standard; segunda camada do watermark (SynthID-Text, API de detecção em private preview); anti-destilação e effort por superfície
- `/apendice-vivo`: snapshot 2026-10-01 (MODELOS, PRECOS, REGULACAO, README e CHANGELOG-APENDICE), com GPT-6 e Gemini 3.8 Flash na camada pública
- Página "O Que Mudou Nesta Edição" com a seção de outubro

### Corrigido

- **Usage credits** (L2-APX-J e `/apendice-vivo/PRECOS.md`): Max e premium com Fable incluído até 50% dos limites semanais, sem data de fim; Pro e standard em usage credits, promoção encerrada em 19/07 (não 07/07)
- **Multiplicador de cache** "válido para toda a família": exceção do Fable 5.1 e Mythos 5.1 (0,025x)
- **Efeito Bruxelas por custo** no L2-APX-J e na seção 45.3.6 do Cap. 45: a razão declarada é limitação técnica de escopo regional
- **PL 2338** na camada pública: o registro de parecer em maio não é confirmado pela ficha da Câmara ("Aguardando Parecer")
- Erro de omissão do check de 01/09 registrado: afirmou que não havia modelo Claude novo no dia do Fable 5.1

### Pendente (declarado)

- `BENCHMARKS.md` e `JANELAS-SLA.md` seguem no snapshot de 18/06, aguardando scores auditados de terceiros; scores de setembro são autorreportados
- Haiku 5.5 (anunciado, não lançado); tokenizer do Opus 5.5 e do Fable 5.1; divergência entre retenção de 30 dias e retenção zero no Fable 5.1; defaults de plano; número da Lei 15.352/2026; cotação USD/BRL

---

## [1.1.1] — 2026-08-24

**Revisão da camada de distribuição: o leitor precisa saber onde clicar.**

### Adicionado

- README com capa, badges de download e bloco "Baixar" no topo, antes de qualquer texto editorial
- `.github/RELEASE_TEMPLATE.md`: cabeçalho fixo das notas de release, com tabela de download em primeiro lugar
- `.github/workflows/release.yml`: publicação automática ao empurrar tag `v*`, com gate que aborta se o PDF ou o HTML estiverem ausentes ou truncados, e corpo montado a partir da seção correspondente deste changelog

### Alterado

- **Nomes canônicos dos entregáveis, congelados a partir desta versão**: `Inteligencia-Aumentada-L2-Deep-Claude.pdf` e `Inteligencia-Aumentada-L2-Deep-Claude-web.html`, substituindo `Deep-Claude-EDICAO-DIGITAL.*`. O nome fixo é o que faz `releases/latest/download/` funcionar como link permanente, compartilhável sem envelhecer
- `livro/gerar-l2.py` passa a gravar com os nomes canônicos
- Árvore de `livro/` no README corrigida para a estrutura real (`00-paratexto`, `02-capitulos`, `03-casos`, `04-apendices`)
- Convenção de tags unificada em SemVer puro (`vX.Y.Z`). A tag legada `livro-v1.0` permanece como histórico e não se repete

### Corrigido

- `.gitignore` passa a cobrir os intermediários `livro/_build/L2-*` e os backups no padrão `.bak-AAAAMMDD`, que apareciam como untracked a cada sessão

---

## [1.1.0] — 2026-08-17

**Ciclo de agosto: watermarking, Sonnet 5 consolidado e sincronização da camada pública de números.**

### Adicionado

- **Livro / corpo**: seção 45.3.6 (marcação de conteúdo gerado: watermarking e proveniência de saída — "a marca prova processamento, não autoria"); Padrão 6 no Cap. 5 (roteamento também é continuidade; salvaguarda é parâmetro vivo); avisos de custo por tarefa vs. por token e fast mode no Cap. 4
- **Livro / paratexto**: página "O Que Mudou Nesta Edição" (changelog a nível de leitor), registrada no build
- **`/apendice-vivo` (camada pública)**: linha "Art. 50 na prática (watermarking)" em REGULACAO.md; Opus 5, Sonnet 5 e família GPT-5.6 em MODELOS.md e PRECOS.md
- MAPA-DO-PROJETO.md: orientação da série (papel de cada pasta/repo, o que montar, regras e fluxos)

### Alterado

- **L2-APX-J → v0.4**: Sonnet 5 consolidado em $2/$10 (aumento de 01/09/2026 **cancelado** pela Anthropic); recalibração das salvaguardas de biologia do Fable 5 (07/08, fallbacks bio −85%); marcação de conteúdo gerado (modelos ≥ 02/08/2026, mundial); placeholders de famílias concorrentes substituídos por referência cruzada ao L1-APX-J (fonte única de números da série)
- `/apendice-vivo`: snapshot 2026-08-12 (cobre também o ciclo de julho, não executado — nota de honestidade editorial no CHANGELOG-APENDICE.md)
- Edição digital regenerada (PDF + HTML)

### Pendente (declarado)

- BENCHMARKS.md e JANELAS-SLA.md no snapshot de 18/06, aguardando scores auditados por terceiros (classe Mythos/Opus 5; ARC-AGI 3, OSWorld 2.0)
- Documentação técnica de detecção de marcas d'água (prometida pela Anthropic)

---

## [1.0.0] — 2026-07 (planejado)

### Adicionado

- Estrutura inicial do repositório com sete pastas principais
- README.md raiz com mapa editorial completo
- CONTRATO.md com princípios de contribuição
- Licenciamento dual (MIT para código, CC-BY 4.0 para conteúdo)
- `/apendice-vivo` seed para junho de 2026
- READMEs estruturados para cada pasta
- `.github/ISSUE_TEMPLATE` com modelos por categoria

### Princípios estabelecidos

- Cadência mensal declarada para `/apendice-vivo` (dias 1-7)
- Errata pública via changelog datado
- Fonte primária obrigatória em cada item do Apêndice Vivo
- Sem autopromoção; sem material de venda no corpo do repositório

---

## [0.1.0] — 2026-06-06

### Adicionado

- Esqueleto inicial criado com sete pastas
- README.md raiz na primeira versão
- LICENSE-MIT e LICENSE-CC-BY
- .gitignore base
- CHANGELOG.md inicial

---

## Errata pública

*Quando informação anterior estava errada, errata explícita aqui com data, descrição e correção. Não removida silenciosamente do histórico.*

Nenhuma errata até o momento.

---

## Cadência de atualizações

| Pasta | Cadência |
|---|---|
| `/apendice-vivo` | Mensal (dias 1-7 de cada mês) |
| `/labs` | Semestral, com lançamentos de versão minor |
| `/prompts` | Conforme demanda, com versionamento por prompt |
| `/skills` | Conforme evolução do ecossistema Claude |
| `/mcps` | Conforme evolução do MCP Registry da Anthropic |
| `/governance` | Anual, com revisão por demanda regulatória |
| `/lancamento` | Conforme campanhas editoriais |
