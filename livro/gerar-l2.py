#!/usr/bin/env python3
"""
Produção da edição DIGITAL do Livro 2 — Deep Claude.

Gera, a partir do manuscrito canônico em deep-claude/livro/:
  1. _build/L2-consolidado.md   (paths de imagem -> file:// absolutos)
  2. Deep-Claude-EDICAO-DIGITAL.pdf   (pandoc -> weasyprint, 16x24cm)
  3. Deep-Claude-EDICAO-DIGITAL.html  (HTML navegavel autocontido, SVG embutido)

Sem sangria de grafica (edicao digital). Capa SVG embutida como pagina 1.
"""
import subprocess
import os
import re
import base64
from pathlib import Path

BASE = Path(__file__).resolve().parent  # .../deep-claude/livro
BUILD = BASE / "_build"
BUILD.mkdir(exist_ok=True)

TITULO = "Deep Claude"
SUBTITULO = "O Currículo Executivo do Ecossistema Anthropic"
AUTOR = "Fabio Garcia"
ANO = "2026"

CAPA_SVG = BASE / "00-paratexto" / "imagens" / "capa-deep-claude-dark.svg"
CONTRACAPA_SVG = BASE / "00-paratexto" / "imagens" / "contracapa-deep-claude.svg"

# ---- ORDEM CANONICA (confirmada contra L2-PT-04-sumario.md e build existente) ----
PARATEXTO_FRENTE = [
    ("00-paratexto/L2-01-conexao-com-livro-1.md", "Conexão com o Livro 1"),
    ("00-paratexto/L2-PT-01-dedicatoria.md", "Dedicatória"),
    ("00-paratexto/L2-PT-02-prefacio.md", "Prefácio"),
    ("00-paratexto/L2-PT-03-como-ler.md", "Como Ler Este Livro"),
    ("00-paratexto/L2-PT-04-sumario.md", "Sumário"),
]

# Capitulos 1..45 na ordem (inclui C05b apos C05 e C20b apos C20). C47 entra DEPOIS do APX-J.
CAPS_1_45 = [
    "L2-C01-executivos", "L2-C02-entendendo-claude", "L2-C03-anatomia-conversa",
    "L2-C04-modelos-claude", "L2-C05-quando-usar-modelos", "L2-C05b-quando-claude-quando-nao",
    "L2-C06-tokens-contexto", "L2-C07-personas-modos", "L2-C08-cowork", "L2-C09-claude-code",
    "L2-C10-claude-web", "L2-C11-desktop", "L2-C12-mobile", "L2-C13-projects", "L2-C14-artifacts",
    "L2-C15-claude-design", "L2-C16-research", "L2-C17-web-search", "L2-C18-voice",
    "L2-C19-scheduled-tasks", "L2-C20-team", "L2-C20b-enterprise",
    "L2-C21-connectors-dispatch-routines", "L2-C22-api-sdks", "L2-C23-tool-use",
    "L2-C24-extended-thinking", "L2-C25-prompt-avancado", "L2-C26-prompt-caching",
    "L2-C27-embeddings", "L2-C28-rag", "L2-C29-claude-mcp", "L2-C30-mcp-avancado",
    "L2-C31-skills", "L2-C32-subagents-workflows", "L2-C33-computer-use", "L2-C34-vision",
    "L2-C35-evaluations", "L2-C36-llmops", "L2-C37-casos-juridicos", "L2-C38-casos-saude",
    "L2-C39-casos-financeiros", "L2-C40-casos-saas-suporte", "L2-C41-casos-rh-mkt-educacao",
    "L2-C42-governanca-executiva", "L2-C43-adocao-institucional", "L2-C44-roi-metricas",
    "L2-C45-seguranca-compliance-lgpd",
]

CORPO = [(f"02-capitulos/{c}.md", c) for c in CAPS_1_45]
CORPO += [
    ("04-apendices/L2-APX-J-apendice-vivo.md", "Cap 46 — Apêndice Vivo"),
    ("02-capitulos/L2-C47-repositorio-acompanhante.md", "Cap 47 — Repositório Acompanhante"),
    ("04-apendices/L2-APX-K-modos-de-falha.md", "Apêndice K — 9 Modos de Falha"),
]

PARATEXTO_FUNDO = [
    ("00-paratexto/L2-PT-05-sobre-o-autor.md", "Sobre o Autor"),
    ("00-paratexto/L2-PT-06-agradecimentos.md", "Agradecimentos"),
    ("00-paratexto/L2-PT-07-colofao-digital.md", "Colofão"),
]

ORDEM = PARATEXTO_FRENTE + CORPO + PARATEXTO_FUNDO


def resolver_img(conteudo: str, arquivo_origem: Path, modo: str) -> str:
    """modo='file' -> file:// absoluto (PDF). modo='data' -> data URI base64 (HTML)."""
    dir_origem = arquivo_origem.parent

    def sub(match):
        alt = match.group(1)
        link = match.group(2)
        if link.startswith(("http://", "https://", "data:")):
            return match.group(0)
        abs_path = (dir_origem / link).resolve()
        if not abs_path.exists():
            return match.group(0)
        if modo == "file":
            return f"![{alt}](file://{abs_path})"
        # data URI
        raw = abs_path.read_bytes()
        ext = abs_path.suffix.lower()
        mime = {".svg": "image/svg+xml", ".png": "image/png",
                ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}.get(ext, "application/octet-stream")
        b64 = base64.b64encode(raw).decode("ascii")
        return f"![{alt}](data:{mime};base64,{b64})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", sub, conteudo)


def folha_de_rosto():
    return (
        '<div class="title-page">\n'
        f'<div class="tp-title">{TITULO}</div>\n'
        f'<div class="tp-sub">{SUBTITULO}</div>\n'
        f'<div class="tp-series">Volume 2 da série <em>Inteligência Aumentada</em></div>\n'
        f'<div class="tp-thesis">Modelos passam. Método fica.</div>\n'
        f'<div class="tp-author">{AUTOR}</div>\n'
        f'<div class="tp-year">{ANO} · Edição digital</div>\n'
        "</div>\n"
    )


def consolidar(modo: str) -> Path:
    print(f"Consolidando ({modo})...")
    # Sem title/author no frontmatter: evita o bloco de título automático do
    # pandoc (que vinha antes da capa). A folha de rosto é a nossa .title-page.
    out = ["---", "lang: pt-BR", "---", ""]

    # Capa como pagina 1 (so no PDF; no HTML usamos imagem no topo tambem)
    if CAPA_SVG.exists():
        if modo == "file":
            out.append('<div class="cover-page">')
            out.append(f'<img src="file://{CAPA_SVG.resolve()}" class="cover-image" alt="Capa"/>')
            out.append("</div>\n")
        else:
            b64 = base64.b64encode(CAPA_SVG.read_bytes()).decode("ascii")
            out.append('<div class="cover-page">')
            out.append(f'<img src="data:image/svg+xml;base64,{b64}" class="cover-image" alt="Capa"/>')
            out.append("</div>\n")

    out.append(folha_de_rosto())

    faltando = []
    for rel, nome in ORDEM:
        p = BASE / rel
        if not p.exists():
            faltando.append(rel)
            print(f"  ✗ FALTA: {rel}")
            continue
        c = p.read_text(encoding="utf-8")
        c = resolver_img(c, p, modo)
        out.append('\n\n<div class="page-break"></div>\n\n')
        out.append(c)
        print(f"  ✓ {nome}")

    if CONTRACAPA_SVG.exists() and modo == "file":
        out.append('\n\n<div class="cover-page">')
        out.append(f'<img src="file://{CONTRACAPA_SVG.resolve()}" class="cover-image" alt="Contracapa"/>')
        out.append("</div>\n")

    dest = BUILD / (f"L2-consolidado-{modo}.md")
    dest.write_text("\n".join(out), encoding="utf-8")
    if faltando:
        print(f"  !! {len(faltando)} arquivo(s) faltando")
    return dest


CSS_PDF = """
@page { size: 16cm 24cm; margin: 2cm 1.8cm;
  @bottom-center { content: counter(page); font-family: sans-serif; font-size: 9pt; color: #6b7280; }
  @top-left { content: string(chapter); font-family: sans-serif; font-size: 8pt; color: #9ca3af; font-style: italic; } }
@page :first { margin: 0; @bottom-center { content: none; } @top-left { content: none; } }
body { font-family: "Liberation Serif","DejaVu Serif",Georgia,serif; font-size: 11pt; line-height: 1.55; color: #0d1b2a; text-align: justify; hyphens: auto; }
.cover-page { width: 16cm; height: 24cm; margin: 0; padding: 0; page-break-after: always; page-break-inside: avoid; }
.cover-image { width: 16cm; height: 24cm; margin: 0; padding: 0; display: block; }
.title-page { page-break-after: always; text-align: center; padding-top: 5cm; }
.title-page .tp-title { font-size: 40pt; font-weight: 700; color: #0d1b2a; letter-spacing: -1pt; }
.title-page .tp-sub { font-size: 15pt; color: #1b263b; font-style: italic; margin-top: 10pt; }
.title-page .tp-series { font-size: 11pt; color: #6b7280; margin-top: 28pt; }
.title-page .tp-thesis { font-size: 13pt; color: #E97451; font-weight: 700; margin-top: 40pt; }
.title-page .tp-author { font-size: 16pt; color: #0d1b2a; margin-top: 60pt; font-weight: 600; }
.title-page .tp-year { font-size: 10pt; color: #6b7280; margin-top: 6pt; }
h1,h2,h3,h4 { font-family: "Liberation Serif","DejaVu Serif",Georgia,serif; font-weight: 700; color: #0d1b2a; string-set: chapter content(); page-break-after: avoid; }
h1 { font-size: 24pt; border-bottom: 2pt solid #E97451; padding-bottom: 8pt; page-break-before: always; letter-spacing: -0.5pt; }
h2 { font-size: 17pt; color: #1b263b; margin-top: 22pt; border-left: 3pt solid #E97451; padding-left: 10pt; }
h3 { font-size: 13pt; margin-top: 16pt; }
p { margin: 0 0 9pt 0; orphans: 3; widows: 3; }
blockquote { margin: 14pt 0; padding: 10pt 14pt; border-left: 3pt solid #E97451; background: #fefce8; font-style: italic; page-break-inside: avoid; }
ul,ol { margin: 8pt 0 12pt 0; padding-left: 22pt; }
li { margin-bottom: 4pt; }
table { width: 100%; border-collapse: collapse; margin: 14pt 0; font-size: 9.5pt; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th { background: #0d1b2a; color: #fef3c7; padding: 6pt 8pt; text-align: left; font-family: sans-serif; font-weight: 700; font-size: 8.5pt; }
td { padding: 5pt 8pt; border-bottom: 0.5pt solid #d1d5db; vertical-align: top; }
tr:nth-child(even) td { background: #fafafa; }
code { font-family: "DejaVu Sans Mono",monospace; font-size: 9.5pt; background: #f3f4f6; padding: 1pt 4pt; border-radius: 2pt; }
pre { background: #0d1b2a; color: #fef3c7; padding: 12pt; border-radius: 4pt; font-size: 8.5pt; line-height: 1.45; white-space: pre-wrap; word-wrap: break-word; }
pre code { background: transparent; color: #fef3c7; padding: 0; }
img { max-width: 100%; height: auto; display: block; margin: 14pt auto; page-break-inside: avoid; }
a { color: #D97706; text-decoration: none; }
.page-break { page-break-after: always; }
strong { color: #0d1b2a; font-weight: 700; }
hr { border: none; border-top: 1pt solid #E97451; margin: 18pt auto; width: 60%; opacity: 0.6; }
"""

CSS_HTML = """
:root { --ink:#0d1b2a; --accent:#E97451; --cream:#fefce8; }
* { box-sizing: border-box; }
body { font-family: Georgia,"Times New Roman",serif; max-width: 860px; margin: 0 auto; padding: 40px 28px 120px; line-height: 1.7; color: var(--ink); background: #fff; }
.cover-page { text-align: center; margin: 0 0 40px; }
.cover-image { max-width: 420px; width: 100%; box-shadow: 0 8px 30px rgba(0,0,0,.18); border-radius: 4px; }
.title-page { text-align: center; padding: 30px 0 50px; border-bottom: 2px solid #eee; margin-bottom: 30px; }
.title-page .tp-title { font-size: 3em; font-weight: 700; letter-spacing: -1px; }
.title-page .tp-sub { font-size: 1.2em; font-style: italic; color: #1b263b; margin-top: 8px; }
.title-page .tp-series { color: #6b7280; margin-top: 18px; }
.title-page .tp-thesis { color: var(--accent); font-weight: 700; margin-top: 24px; font-size: 1.1em; }
.title-page .tp-author { font-size: 1.3em; font-weight: 600; margin-top: 40px; }
.title-page .tp-year { color: #6b7280; }
h1 { font-size: 1.9em; border-bottom: 3px solid var(--accent); padding-bottom: .25em; margin-top: 2.4em; scroll-margin-top: 20px; }
h2 { font-size: 1.4em; color: #1b263b; border-left: 4px solid var(--accent); padding-left: 12px; margin-top: 1.6em; }
h3 { font-size: 1.15em; color: #1b263b; }
blockquote { border-left: 4px solid var(--accent); background: var(--cream); padding: .7em 1.1em; margin: 1.3em 0; font-style: italic; }
table { border-collapse: collapse; width: 100%; margin: 1.3em 0; font-size: .93em; }
th,td { border: 1px solid #ddd; padding: 8px 11px; text-align: left; vertical-align: top; }
th { background: var(--ink); color: var(--cream); }
tr:nth-child(even) td { background: #fafafa; }
code { background: #f4f4f4; padding: 1px 5px; border-radius: 3px; font-size: .9em; font-family: "SFMono-Regular",Consolas,monospace; }
pre { background: var(--ink); color: var(--cream); padding: 16px; border-radius: 6px; overflow-x: auto; font-size: .85em; line-height: 1.5; }
pre code { background: transparent; color: var(--cream); }
img { max-width: 100%; height: auto; display: block; margin: 1.4em auto; }
a { color: #1a5276; text-decoration: none; }
hr { border: none; border-top: 1px solid #ddd; margin: 2em 0; }
#TOC { background: #faf9f6; border: 1px solid #e0ddd0; padding: 1.2em 1.6em; border-radius: 8px; margin: 1.5em 0; }
#TOC a { color: var(--ink); }
"""


def gerar_pdf():
    md = consolidar("file")
    html = BUILD / "L2-pdf.html"
    css = BUILD / "L2-pdf.css"
    css.write_text(CSS_PDF, encoding="utf-8")
    subprocess.run([
        "pandoc", str(md),
        "-f", "markdown+raw_html+definition_lists+fenced_code_blocks+pipe_tables",
        "-t", "html5", "--standalone", "-o", str(html),
        "--metadata=lang:pt-BR",
    ], check=True)
    import weasyprint
    pdf = BASE / "Deep-Claude-EDICAO-DIGITAL.pdf"
    weasyprint.HTML(filename=str(html), base_url=str(BASE)).write_pdf(
        str(pdf), stylesheets=[weasyprint.CSS(filename=str(css))])
    mb = pdf.stat().st_size / (1024 * 1024)
    print(f"\n✓ PDF: {pdf} ({mb:.2f} MB)")
    return pdf


def gerar_html():
    md = consolidar("data")
    out = BASE / "Deep-Claude-EDICAO-DIGITAL.html"
    subprocess.run([
        "pandoc", str(md),
        "-f", "markdown+raw_html+definition_lists+fenced_code_blocks+pipe_tables",
        "-t", "html5", "--standalone", "--toc", "--toc-depth=1",
        "-o", str(out),
        "--metadata=lang:pt-BR",
    ], check=True)
    # injeta CSS inline + <title> da aba
    html = out.read_text(encoding="utf-8")
    html = html.replace("</head>", f"<title>{TITULO} · {SUBTITULO}</title><style>{CSS_HTML}</style></head>")
    out.write_text(html, encoding="utf-8")
    mb = out.stat().st_size / (1024 * 1024)
    print(f"\n✓ HTML: {out} ({mb:.2f} MB)")
    return out


if __name__ == "__main__":
    import sys
    alvo = sys.argv[1] if len(sys.argv) > 1 else "all"
    if alvo in ("pdf", "all"):
        gerar_pdf()
    if alvo in ("html", "all"):
        gerar_html()
