# MAPA DO PROJETO — Série "Inteligência Aumentada"

> Leia isto primeiro. Este documento existe para que ninguém, humano ou sessão de IA, se perca entre as pastas da série. Uma cópia idêntica vive em cada pasta do projeto. Atualizado em: 25/08/2026.

---

## A série em uma linha

Dois livros com uma tese: **"Modelos passam. Método fica."** O corpo dos livros é atemporal (princípios, frameworks, julgamento) e todo número volátil (preço, versão, benchmark, regulação) vive em apêndices vivos datados, com fonte primária por linha.

| Livro | Título | Papel | Onde vive |
|---|---|---|---|
| **L1** | Inteligência Aumentada · Os 9 Invariantes da IA | O método, vendor-neutral, multi-vendor por definição | Manuscrito: repo privado `inteligencia-aumentada-os-invariantes` · Publicação: repo público `inteligencia-aumentada` |
| **L2** | Deep Claude · Currículo Executivo do Ecossistema Anthropic | O produto, específico de Claude. É o "livro vivo" da série | Repo público `deep-claude`, tudo dentro |

---

## As três pastas e o papel de cada uma

### 1. `~/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes`
**Repositório git privado** (`git@github.com:falercia/inteligencia-aumentada-os-invariantes.git`, branch `main`). É a fonte da verdade do **manuscrito do L1**: capítulos, frameworks, apêndices, paratexto, pipeline `gerar-l1.py` (prepare → chunk 0-9 → merge → html), changelogs editoriais, `_revisao-editorial/`, `_posicionamento/` e `_lancamento/`.

É privado porque carrega o scan competitivo. Por isso a publicação do L1 sai pelo repo do companion, não daqui. **Não chamar de "rascunho": é repo, e o que se edita aqui precisa ser commitado.**

### 2. `~/Documents/Repositorios/Github falercia/deep-claude`
**Repositório git público.** Duas camadas no mesmo lugar:
- `livro/` — manuscrito completo do L2, apêndices (incl. `L2-APX-J-apendice-vivo.md`), edição digital publicada e pipeline `gerar-l2.py`.
- `apendice-vivo/` (raiz) — **camada pública de números da série** (MODELOS, PRECOS, BENCHMARKS, REGULACAO, JANELAS-SLA, FONTES, CHANGELOG-APENDICE). É para cá que o repo do L1 aponta. A checagem mensal atualiza esta pasta.
- Mais `labs/ prompts/ skills/ mcps/ governance/ lancamento/`.

### 3. `~/Documents/Repositorios/Github falercia/inteligencia-aumentada`
**Repositório git público.** Renomeado em 25/08/2026, antes se chamava `inteligencia-aumentada-recursos`. O GitHub mantém redirect permanente do nome antigo; **nunca criar repo novo com o nome antigo**, isso mataria o redirect.
- `livro/` — a edição digital publicada do L1 (PDF, HTML, capa e `gerar-l1.py`).
- `apendice-vivo/` — **só um ponteiro** para `deep-claude/apendice-vivo/`. Nunca duplicar números aqui.
- Mais `prompts/ evals/ agents/ datasets/ notebooks/ mcp/ ferramentas/ fontes/ governance/ repos-curados/`.

### Pastas que não são projeto
`Github falercia/_orfa-17ago-DUPLICATA` é bancada morta, conteúdo duplicado, descartável. `Personal/Livros/Ebook IA/Livro-2-Deep-Claude` é rascunho **stale** do L2; o canônico é `deep-claude/livro/`.

---

## Distribuição: como o leitor chega no livro

**Os dois links permanentes da série.** Nunca envelhecem, servem para LinkedIn, QR code, slide e assinatura de e-mail:

```
https://github.com/falercia/inteligencia-aumentada/releases/latest/download/Inteligencia-Aumentada-L1-Os-Invariantes.pdf
https://github.com/falercia/deep-claude/releases/latest/download/Inteligencia-Aumentada-L2-Deep-Claude.pdf
```

**Nomes de arquivo congelados.** É o nome fixo que faz `latest/download` funcionar. A versão vai no corpo da release e no CHANGELOG, **jamais no nome do arquivo**.

| | PDF | HTML |
|---|---|---|
| L1 | `Inteligencia-Aumentada-L1-Os-Invariantes.pdf` | `Inteligencia-Aumentada-L1-Os-Invariantes-web.html` |
| L2 | `Inteligencia-Aumentada-L2-Deep-Claude.pdf` | `Inteligencia-Aumentada-L2-Deep-Claude-web.html` |

**Três camadas com papéis distintos.** README é a vitrine permanente, com capa, botões de download e bloco "Baixar" no topo, antes de qualquer texto editorial. A página de release é o snapshot da versão, com download em primeiro lugar e link para o changelog. O CHANGELOG é o log técnico. Nunca colar changelog de engenharia como corpo de release.

**Publicação é automática.** Cada repo tem `.github/workflows/release.yml`, que dispara ao empurrar a tag, **aborta se o PDF ou o HTML estiverem ausentes ou menores que 500 KB**, monta o corpo a partir da seção correspondente do CHANGELOG e anexa os arquivos. Não se cria release na mão.

**Tags.** L2 usa SemVer puro (`vX.Y.Z`). L1 tem duas linhas convivendo no mesmo repo, `livro-vX.Y` para o livro e `vX.Y.Z` para artefatos do companion; por isso o workflow do L1 dispara nas duas e **anexa o livro em toda release**, senão uma release só de artefato viraria "Latest" sem PDF e quebraria os links permanentes.

---

## O que montar por tipo de tarefa

| Tarefa | Montar |
|---|---|
| Checagem mensal dos apêndices vivos | `Livro-1-Os-Invariantes` + `deep-claude` (+ `inteligencia-aumentada` se for fechar release) |
| Revisão editorial ou escrita do L1 | `Livro-1-Os-Invariantes` |
| Qualquer trabalho no L2 | `deep-claude` |
| Publicar nova edição do L1 | `Livro-1-Os-Invariantes` + `inteligencia-aumentada` |
| Atualizar números públicos | `deep-claude` (pasta `apendice-vivo/`) |

A pasta `Github falercia` não fica montada por padrão. Pedir acesso com o caminho completo e esperar a aprovação no desktop.

---

## Regras permanentes (não quebrar)

1. **Fonte única de números.** No livro: L1-APX-J (Trilha do Número) é a camada multi-vendor, L2-APX-J cobre só a família Claude. No público: `deep-claude/apendice-vivo/`. Nunca duplicar o mesmo número em dois lugares editáveis.
2. **Número só com fonte primária.** Sem fonte oficial, não tabula, declara a lacuna. Agregador ou imprensa entra apenas com marcador explícito de fonte secundária.
3. **Corpo atemporal.** Fato datado não entra em capítulo, entra no apêndice. No capítulo entra apenas o padrão durável.
4. **Vendor-neutral no L1.** Mecanismo de fornecedor específico vai para o L2 ou para o apêndice; o L1 trata como padrão de mercado.
5. **Backup antes de editar apêndice vivo:** cópia `.bak-AAAAMMDD` ao lado do arquivo. Está no `.gitignore`, não commitar.
6. **Commit no repo certo.** L2 no `deep-claude`. Companion e releases do L1 no `inteligencia-aumentada`. Manuscrito do L1 no repo privado. O push é sempre do Fabio.
7. **Aplicar não é entregar.** Toda rodada fecha com `git status` limpo nos repos envolvidos, não só com o PDF gerado. Em ago/2026 uma revisão inteira ficou aplicada em disco e não commitada por duas semanas.
8. **Nome de arquivo publicado é congelado.** Renomear entregável quebra todo link já compartilhado.
9. **Changelog em dois níveis.** Editorial, com fonte por item, nos changelogs de revisão. De leitor, em linguagem direta, na página "O Que Mudou Nesta Edição" dentro dos livros e nas release notes.

---

## Fluxos padrão

**Checagem mensal.** Ler L1-APX-J e L2-APX-J → verificar fontes oficiais (Anthropic pricing e news, vendors, Câmara, ANPD, EU AI Act) → relatório com diff proposto → após aprovação, aplicar nos dois APX-J e em `deep-claude/apendice-vivo/` → registrar nos changelogs → commit nos repos envolvidos.

**Nova edição do L1.** Editar no repo do manuscrito → `gerar-l1.py prepare`, `chunk 0..9`, `merge`, `html` → copiar PDF, HTML e o gerador para `inteligencia-aumentada/livro/` **com os nomes canônicos** → nova seção no `CHANGELOG.md` → commit → `git tag -a livro-vX.Y` → `git push origin livro-vX.Y`. O workflow publica a release sozinho.

**Nova edição do L2.** Editar em `deep-claude/livro/` → `python3 livro/gerar-l2.py` → nova seção no `CHANGELOG.md` → commit → `git tag -a vX.Y.Z` → push da tag. O workflow publica.

---

## Estado em 25/08/2026

- **L1**: `livro-v1.2` publicada, com README de vitrine, capa, nomes canônicos e workflow. A revisão de 12/ago (C19 proveniência, APX-J com watermarking, Sonnet 5 em $2/$10, Reg. UE 2026/1744, paratexto "O Que Mudou") finalmente commitada no repo do manuscrito.
- **L2**: `v1.1.1` publicada, mesma estrutura de distribuição. APX-J v0.4.
- **`deep-claude/apendice-vivo/`**: snapshot de 12/ago. Pendentes: BENCHMARKS e JANELAS-SLA aguardando scores auditados por terceiros, e cotação USD/BRL.
- **Sobras conhecidas**: `PUSH-INSTRUCTIONS-v1.1.0.md` e `CHANGELOG-v1.1.0.md` na raiz do `inteligencia-aumentada` são andaimes de junho já executados. O paratexto "Sobre o Autor" do L2 teve o nome do repo do L1 corrigido no fonte, mas o PDF publicado só reflete isso na próxima regeneração.
- **Próxima checagem mensal**: setembro/2026. Gatilhos: documentação de detecção de marcas d'água da Anthropic, ARC-AGI 3 e OSWorld 2.0 auditados, PL 2338 na ficha da Câmara, usage credits no dashboard, tier research-grade do GPT-5.6.
