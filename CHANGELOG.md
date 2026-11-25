# Changelog

Todas as mudanças relevantes deste repositório são registradas aqui, em ordem cronológica reversa, com data, autor e fonte primária quando aplicável.

O formato segue [Keep a Changelog](https://keepachangelog.com/) e o versionamento segue [Semantic Versioning](https://semver.org/).

---

## [1.2.3] — 2026-11-25

**Edição de 25 de novembro de 2026: o topo da família Claude baixou de preço, e o Claude virou lugar de trabalho.**

### O que mudou para quem lê

- **Fable 5.2 e Mythos 5.2, lançados em 9 de novembro, custam US$ 8/40 por milhão de tokens**, 20% abaixo do Fable 5.1. É a primeira vez que o tier de fronteira fica mais barato de uma geração para a outra. A leitura de cache cai para US$ 0,20, e o topo ganha **Fast mode** (US$ 16/80, até 2,5x mais rápido).
- **O Claude saiu do chat.** Claude Sheets e Claude Whiteboards entraram em beta em todos os planos pagos (10/nov), o Claude Data, antigo Dashboards, ficou disponível para todos com métricas certificadas pelo time de dados, e o **Claude Meetings** começou a entrar em chamadas do Google Meet para Team e Enterprise (12/nov). O apêndice traz o que cada um faz, os limites que a própria Anthropic declara e o default de governança por plano.
- **Datas que pedem ação.** O Sonnet 4.5 e o Fast mode do Opus 4.8 saem em 30 de novembro; o Opus 4.5 sai em 22 de janeiro de 2027. A página oficial passou a publicar a data mínima de retirada de Fable 5, Opus 4.8, Opus 5 e Sonnet 5.
- **Integração ficou mais estrita.** A regra que proíbe editar o histórico preservando o raciocínio vale agora para todas as contas de API, e o raciocínio do Fable 5.2 é descartado se a conversa muda de modelo.
- **Retenção e planos, sem ambiguidade.** O Fable 5.2 exige retenção de 30 dias; retenção zero passa pelo Enterprise Frontier Safeguards, em beta desde 23/nov. A tabela de usage credits foi reescrita a partir do Help Center, com a divergência do anúncio sobre o plano Pro declarada.
- **Dois erros de método corrigidos no corpo.** O Capítulo 4 deixou de carregar razões de custo fixas entre tiers e de recomendar o Sonnet como ponto de partida; o texto ensina a regra que dura, comece pelo menor tier que passa na sua avaliação.
- **Fora da família Claude**, a camada pública `/apendice-vivo` registra o GPT-6.2 Astra (US$ 8/40, o mesmo preço do Fable 5.2) e Sol, as janelas de background da OpenAI (30% a 40% mais baratas para quem aceita esperar), o Gemini 4 Argon dobrando de preço em 1º de dezembro e o PL 2338 com 45 projetos apensados, ainda sem parecer.

### Registro técnico

- **L2-APX-J → v0.8**: lineup com Fable 5.2 e Mythos 5.2; bloco "Geração 5.2" com os eventos de 29/10 a 23/11 (Usage and Cost Analytics API, Message threads, Managed Agents auto-hospedado, Linked billing, EFS) e as mudanças de integração (prefixo, thinking fora do par 5.2, advisor, computer use, retenção); bloco "Produto" (Sheets, Whiteboards, Data, conectores interativos, Meetings); pisos de retirada e aposentadorias; marca d'água estendida a sete modelos anteriores, com a ressalva de parâmetros de amostragem; Seções 5 e 6 reescritas (degrau Fable para Opus volta a 2x)
- **Corrigido**: usage credits (Help Center), divergência de retenção aberta desde a v0.5, Capítulo 4 (razões de custo e ponto de partida), Seção 5 do APX-J
- `/apendice-vivo`: snapshot 2026-11-25 (MODELOS, PRECOS, REGULACAO, README e CHANGELOG-APENDICE)
- Página "O Que Mudou Nesta Edição" com a seção de 25 de novembro

### Pendente (declarado)

- Data de fim da oferta de lançamento do Fable 5.2; lista de modelos com retenção zero no EFS; status do Haiku 4.5 (piso de retirada vencido); defaults de plano; Usage Policy 2026 e Cyber Mission; ANPD e Lei 15.352/2026; `BENCHMARKS.md` e `JANELAS-SLA.md` aguardando scores auditados

---

## [1.2.2] — 2026-11-01

**Reconferência mensal de novembro: família Claude sem mudança de preço, camada pública atualizada.**

### Adicionado

- **L2-APX-J → v0.7**: reconferência da família Claude contra a página oficial de pricing e a visão geral de modelos (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, Sonnet 5, Opus 5, Haiku 4.5: sem mudança); multiplicadores de cache reconfirmados; tokenizer de "4.7 e posteriores" confirmado na página de pricing; posts de 09/10 a 01/11 registrados
- `/apendice-vivo`: snapshot 2026-11-01 (MODELOS, PRECOS, REGULACAO, README e CHANGELOG-APENDICE), com Gemini 4 Argon (US$ 2/10 até 30/11, US$ 4/20 a partir de 01/12), GPT-6.1 Terra (US$ 1/5) e PL 2338 com 40 apensadas
- Página "O Que Mudou Nesta Edição" com a seção de 1º de novembro

### Pendente (declarado)

- Conteúdo dos posts de 06/10 e 08/10 (Cyber Verification Program, Usage Policy 2026, Cyber Mission); usage credits no Help Center; página de deprecações; número da Lei 15.352/2026 e andamento da ANPD (a lista de notícias carrega dinamicamente e não foi lida); data de publicação do Reg. (UE) 2026/1744 no Jornal Oficial; preço do Gemini 4 Argon sem data de lançamento em fonte primária; Gemini 3.8 Pro não verificado; `BENCHMARKS.md` e `JANELAS-SLA.md` aguardando scores auditados
- No corpo, o Capítulo 4 (razão de custo Haiku versus Opus) segue com decisão editorial pendente

---

## [1.2.1] — 2026-10-09

**Reconferência mensal de outubro: Haiku 5.5 e uma errata de cache.**

### Adicionado

- **L2-APX-J → v0.6**: Haiku 5.5 (07/10, US$ 0,10/0,50 até 100k tokens de prompt e US$ 0,50/2,50 acima, contexto de 1M, retirada não antes de 07/10/2027), breaking change de parâmetros de amostragem, tokenizer, anúncios de política e segurança de 06/10 e 08/10
- `/apendice-vivo`: snapshot 2026-10-09 (MODELOS, PRECOS, REGULACAO, README e CHANGELOG-APENDICE), com o aviso do aumento de tarifa do Gemini Flash em 01/01/2027
- Página "O Que Mudou Nesta Edição" com a seção de 9 de outubro

### Corrigido

- **Cache read do Sonnet 5.5** (L2-APX-J e `/apendice-vivo/PRECOS.md`): US$ 0,10 por MTok (0,05x do input), e não US$ 0,20

### Pendente (declarado)

- Conteúdo dos posts de Usage Policy 2026 e Cyber Verification Program; usage credits no Help Center; tokenizer do Opus 5.5 e do Fable 5.1; retenção de 30 dias versus retenção zero no Fable 5.1; número da Lei 15.352/2026; Reg. (UE) 2026/1744 no Jornal Oficial; `BENCHMARKS.md` e `JANELAS-SLA.md` aguardando scores auditados
- No corpo, o Capítulo 4 (tier Haiku) diz que o custo é "cerca de vinte vezes menos" que o Opus. Com o Haiku 5.5 a US$ 0,10 contra US$ 4 do Opus 5.5 a razão é outra; decisão editorial pendente: remover a razão e remeter ao Apêndice Vivo

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
