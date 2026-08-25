#!/usr/bin/env python3
"""
Regenera ler/index.html a partir do HTML do livro em livro/.

Por que existe: o arquivo que o GitHub Pages serve em /ler/ é uma cópia tratada
do HTML gerado pelo gerar-l2.py. Sem este script, publicar uma edição nova
atualizaria o PDF da release e deixaria a página de leitura na versão antiga,
sem nenhum aviso.

Uso: python3 scripts/atualizar-ler.py     (a partir da raiz do repositório)
Roda sozinho no GitHub Actions sempre que livro/*-web.html muda na main.
"""

import glob
import os
import re
import sys

# ---------------------------------------------------------------- configuração
FONTE_GLOB = 'livro/Inteligencia-Aumentada-L2-*-web.html'
DESTINO = 'ler/index.html'
TITULO = 'Deep Claude · Currículo Executivo do Ecossistema Anthropic'
ROTULO = 'Livro 2 · Deep Claude'
PDF = ('https://github.com/falercia/deep-claude/releases/latest/'
       'download/Inteligencia-Aumentada-L2-Deep-Claude.pdf')
TAMANHO_MINIMO = 500_000  # o mesmo gate do release.yml, contra build quebrado

BARRA = """
<style id="ia-barra-css">
  :root{--ia-bg:#17181A;--ia-fg:#F6F4EF;--ia-suave:#9B968B;--ia-rule:#3A3C40;--ia-acento:#E9683C}
  #ia-barra{position:fixed;top:0;left:0;right:0;z-index:9999;background:rgba(23,24,26,.96);
    -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--ia-rule);
    font-family:'IBM Plex Sans',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;color:var(--ia-fg)}
  #ia-barra .ia-wrap{max-width:1120px;margin:0 auto;padding:0 20px;height:46px;display:flex;align-items:center;
    justify-content:space-between;gap:12px}
  #ia-barra a{color:var(--ia-suave);text-decoration:none;font-size:13px;font-weight:500;padding:6px 10px;
    border-radius:6px;white-space:nowrap;transition:.18s}
  #ia-barra a:hover{color:var(--ia-fg)}
  #ia-barra .ia-pdf{background:var(--ia-acento);color:#17181A;font-weight:600}
  #ia-barra .ia-pdf:hover{background:#F07E56;color:#17181A}
  #ia-barra .ia-rot{font-family:'IBM Plex Mono',ui-monospace,Menlo,monospace;font-size:10.5px;letter-spacing:.14em;
    text-transform:uppercase;color:var(--ia-suave);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  #ia-espaco{height:46px}
  @media (max-width:640px){#ia-barra .ia-rot{display:none}}
  @media print{#ia-barra,#ia-espaco{display:none}}
</style>
<div id="ia-barra"><div class="ia-wrap">
  <a href="../">&#8592; Página do livro</a>
  <span class="ia-rot">__ROTULO__</span>
  <a class="ia-pdf" href="__PDF__">Baixar o PDF</a>
</div></div>
<div id="ia-espaco"></div>
"""


def main():
    achados = sorted(glob.glob(FONTE_GLOB))
    if not achados:
        sys.exit('ERRO: nenhum arquivo casa com %s. Gere o livro antes.' % FONTE_GLOB)
    fonte = achados[0]

    tamanho = os.path.getsize(fonte)
    if tamanho < TAMANHO_MINIMO:
        sys.exit('ERRO: %s tem apenas %d bytes, build provavelmente quebrado.' % (fonte, tamanho))

    html = open(fonte, encoding='utf-8').read()

    # 1. título de verdade, o pandoc deixa o nome do arquivo de origem
    html = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITULO, html, count=1, flags=re.S)

    # 2. viewport, para o livro não abrir com zoom de desktop no celular
    if '<meta name="viewport"' not in html:
        html = html.replace(
            '<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1">', 1)

    # 3. barra fixa com volta para a landing e download do PDF
    barra = BARRA.replace('__ROTULO__', ROTULO).replace('__PDF__', PDF)
    html, n = re.subn(r'(<body[^>]*>)', lambda m: m.group(1) + barra, html, count=1)
    if n != 1:
        sys.exit('ERRO: não encontrei a tag <body> em %s.' % fonte)

    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    anterior = open(DESTINO, encoding='utf-8').read() if os.path.exists(DESTINO) else None
    if anterior == html:
        print('Nada a fazer, %s já está em dia com %s.' % (DESTINO, fonte))
        return

    open(DESTINO, 'w', encoding='utf-8').write(html)
    print('Atualizado %s a partir de %s (%.2f MB).' % (DESTINO, fonte, len(html) / 1024 / 1024))


if __name__ == '__main__':
    main()
