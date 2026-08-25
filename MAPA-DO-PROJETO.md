# MAPA DO PROJETO — Série "Inteligência Aumentada"

> Leia isto primeiro. Este documento existe para que ninguém — humano ou sessão de IA — se perca entre as pastas da série. Uma cópia idêntica vive em cada pasta do projeto. Atualizado em: 17/08/2026.

---

## A série em uma linha

Dois livros com uma tese: **"Modelos passam. Método fica."** O corpo dos livros é atemporal (princípios, frameworks, julgamento); todo número volátil (preço, versão, benchmark, regulação) vive em apêndices vivos datados, com fonte primária por linha.

| Livro | Título | Papel | Onde vive |
|---|---|---|---|
| **L1** | Os Invariantes da IA (Inteligência Aumentada) | O método, vendor-neutral. Multi-vendor por definição | Rascunho: pasta `Livro-1-Os-Invariantes` · Distribuição: releases do repo `inteligencia-aumentada` |
| **L2** | Deep Claude | O produto, específico de Claude. É o "livro vivo" da série | Repo `deep-claude`, pasta `livro/` |

---

## As quatro pastas e o papel de cada uma

### 1. `~/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes` (rascunho do L1)
Fonte da verdade **de trabalho** do manuscrito do L1: capítulos, frameworks, apêndices, paratexto, pipeline de build (`gerar-l1.py`: prepare → chunk 0-9 → merge → html). Não é repositório git. É aqui que se edita o L1.
Contém também: changelogs editoriais das revisões, backups `.bak-AAAAMMDD`, builds em `_build*`.

### 2. `~/Documents/Repositorios/Github falercia/deep-claude` (repo público do L2 — O REPO VIVO)
Duas camadas:
- `livro/` — manuscrito completo do L2, apêndices (incl. `L2-APX-J-apendice-vivo.md`), edição digital (PDF/HTML) e pipeline `livro/gerar-l2.py`. Edita-se e commita-se direto aqui.
- `apendice-vivo/` (raiz) — **camada pública de números da série** (MODELOS, PRECOS, BENCHMARKS, REGULACAO, JANELAS-SLA, FONTES, CHANGELOG-APENDICE). É para cá que o repo do L1 aponta. Checagem mensal atualiza esta pasta.

### 3. `~/Documents/Repositorios/Github falercia/inteligencia-aumentada` (repo público acompanhante do L1)
Recursos práticos do L1: agents, prompts, evals, datasets, ferramentas, governance. Regras:
- `apendice-vivo/` daqui é **só um ponteiro** para o `deep-claude/apendice-vivo/` — nunca duplicar números aqui.
- `livro/` daqui carrega a edição digital corrente do L1 (PDF/HTML) para distribuição.
- **Cada edição do livro = tag/release** no padrão `livro-vX.Y` (ex.: `livro-v1.0`, `livro-v1.1`). Release notes = seção correspondente do `CHANGELOG.md`.

### 4. `~/Documents/Repositorios/Github falercia/inteligencia-aumentada` (repo privado do manuscrito L1 — A CRIAR)
Reservado para versionar o manuscrito completo do L1 (espelho do rascunho, estrutura `livro/`). Em 17/08/2026 ainda **não tem git inicializado**. Enquanto não existir, o rascunho (pasta 1) é a única fonte do manuscrito.

---

## O que montar por tipo de tarefa (Cowork/Claude)

| Tarefa | Montar |
|---|---|
| Checagem mensal dos apêndices vivos (task agendada) | `Livro-1-Os-Invariantes` + `deep-claude` (+ `-recursos` se for fechar release) |
| Revisão editorial / escrita do L1 | `Livro-1-Os-Invariantes` |
| Qualquer trabalho no L2 (texto, apêndice, build) | `deep-claude` |
| Publicar nova edição do L1 | `Livro-1-Os-Invariantes` + `inteligencia-aumentada` |
| Atualizar números públicos (preços, modelos, regulação) | `deep-claude` (pasta `apendice-vivo/`) |

---

## Regras permanentes (não quebrar)

1. **Fonte única de números.** No livro: L1-APX-J (Trilha do Número) é a camada multi-vendor; L2-APX-J cobre só a família Claude. No público: `deep-claude/apendice-vivo/`. Nunca duplicar o mesmo número em dois lugares editáveis.
2. **Número só com fonte primária.** Sem fonte oficial, não tabula — declara a lacuna. Agregador/imprensa entra apenas com marcador explícito de fonte secundária.
3. **Corpo atemporal.** Fato datado não entra em capítulo; entra no apêndice. No capítulo entra apenas o padrão durável (ex.: "a marca prova processamento, não autoria").
4. **Vendor-neutral no L1.** Mecanismo de fornecedor específico vai para o L2 ou para o apêndice; o L1 trata como padrão de mercado.
5. **Backup antes de editar apêndice vivo:** cópia `.bak-AAAAMMDD` ao lado do arquivo (não commitar).
6. **Commit no repo certo.** L2 → `deep-claude`. Recursos e releases do L1 → `-recursos`. Manuscrito L1 → pasta de rascunho (e futuramente repo privado). Push é sempre do Fabio (credenciais).
7. **Changelog em dois níveis.** Editorial (com fonte por item) nos changelogs de revisão; leitor (linguagem direta) na página "O Que Mudou Nesta Edição" dentro dos livros e nas release notes.

---

## Fluxos padrão

**Checagem mensal (task agendada "check-mensal-apendice-vivo-l2"):** ler L1-APX-J e L2-APX-J → verificar fontes oficiais (Anthropic pricing/news, vendors, Câmara/ANPD, EU AI Act) → relatório com diff proposto → após aprovação: aplicar nos dois APX-J + `deep-claude/apendice-vivo/` + registrar nos changelogs.

**Nova edição do L1:** editar rascunho → `gerar-l1.py prepare` → `chunk 0..9` → `merge` → `html` → copiar PDF/HTML/gerar-l1.py para `-recursos/livro/` → seção nova no `CHANGELOG.md` → commit + tag `livro-vX.Y` → push com tags → release no GitHub.

**Atualização do L2:** editar em `deep-claude/livro/` → `python3 livro/gerar-l2.py` (gera PDF+HTML) → commit (inclui os builds) → push.

---

## Estado em 17/08/2026

- L1: rev. 12/ago publicada como `livro-v1.1` no `-recursos`; corpo com C19 §proveniência; APX-J com watermarking, Sonnet 5 $2/$10 consolidado, Reg. UE 2026/1744.
- L2: APX-J v0.4; corpo com §45.3.6 (watermarking), Padrão 6 (C05), fast mode/custo-por-tarefa (C04); edição digital regenerada.
- `deep-claude/apendice-vivo/`: snapshot 12/ago (pendentes: BENCHMARKS e JANELAS-SLA aguardando scores auditados; cotação USD/BRL).
- Próxima checagem mensal: setembro/2026 (gatilhos: detecção de marcas d'água da Anthropic, ARC-AGI 3 / OSWorld 2.0 auditados, PL 2338 na ficha da Câmara, usage credits no dashboard).
