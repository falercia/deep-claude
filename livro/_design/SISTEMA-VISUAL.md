# Sistema Visual — Deep Claude (diagramas)

**Decisão (2026-06-18):** diagramas **vetoriais (SVG)**, identidade coerente, no padrão DDIA/HBR. Vetorial imprime perfeito, escala e é editável/rebrandável. Sem arte raster gerada por IA (data rápido e destoa de livro de método).

## Paleta (design tokens)

| Token | Hex | Uso |
|---|---|---|
| tinta-ardósia | `#1B2A33` | texto principal, nós-âncora, fundo de destaque |
| tinta-suave | `#44525C` | setas, texto secundário em nós escuros |
| dourado (casa) | `#C2912C` | acento, régua de título, Opus, ênfase |
| dourado claro | `#E2C879` | gradiente da régua |
| teal apoio | `#2E7D8A` | secundário, Haiku, camada "consulta", baixo risco |
| terracota risco | `#B5532F` | alerta, risco, fronteira de governança, preview |
| papel | `#FBF8F1` | fundo do frame |
| linha | `#E6DFC9` / `#CFC8B6` | bordas, hairlines |
| muted | `#7C7768` | legenda |

Fills suaves: dourado `#FBF6EA`/`#EADfBF` · teal `#EFF6F7`/`#CFE3E6` · risco `#F0DDD2`/`#E7CDBE` · neutro `#F1ECE0`/`#D8D0BD`.

## Tipografia
Stack: `'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif`.
- Kicker (nº + invariante): 12.5px, **700**, `letter-spacing 2.5`, dourado, MAIÚSCULAS.
- Título do diagrama: 23px **700** tinta-ardósia.
- Rótulos de nó: 14–15px **700**; subtexto 11.5–12.5px muted.
- Legenda de rodapé: 12.5px itálico muted.

## Componentes
- **Frame:** `rect rx=16 fill=#FBF8F1 stroke=#E6DFC9`, viewBox largura 880.
- **Régua de título:** `rect 86×3.5 rx=1.75 fill=url(#goldRule)` sob o título.
- **Nó/caixa:** `rect rx=10–14`, fill branco, stroke da cor-tema, sombra suave (`feDropShadow dy=2 stdDeviation=3.5 opacity=.12`).
- **Setas:** `marker` triangular 7×6, cor tinta-suave/tema; `stroke-width 2.2`.
- **Badge numerado:** círculo r=14 preenchido cor-tema, número branco **700**.
- **Headers de painel/banda:** barra superior preenchida cor-tema com texto branco.
- **Pílulas/chips:** `rect rx=10–12`, fill suave, texto 11–12px cor-tema.

## Catálogo de tipos (validados no piloto)
1. **Conceito** — `cap-46-img-01-camada-dupla` (Livro vs Repositório → decisão).
2. **Anatomia/stack** — `cap-08-img-01-superficies-acesso` (4 camadas, eixo de risco).
3. **Ciclo/loop** — `cap-08-img-02-ciclo-supervisao` (ring com centro + ring tracejado).
4. **Árvore de decisão** — `cap-05-img-01-arvore-decisao-modelos` (SIM/NÃO).
5. **Arquitetura em camadas** — `cap-28-img-01-mcp-corporativo` (bandas + governança).
6. **Pipeline** — `cap-27-img-01-pipeline-rag` (duas raias: indexação/consulta).
7. **Loop binário** — `cap-22-img-01-ciclo-agentico` (2 nós + fronteira).
8. **Matriz 2×2** — `cap-05-img-02-portfolio-roteamento` (eixos complexidade×volume).

## Convenções de cor por Invariante (opcional, para coesão)
Inv. 6 Autonomia → dourado/risco · Inv. 1 Plausibilidade → terracota de alerta · Inv. 4 Encaixe → trio Opus(dourado)/Sonnet(tinta)/Haiku(teal) · Inv. 3 Camada Dupla → dourado(livro)/teal(repo).

## Regras
- Toda figura é **autocontida**: kicker + título + diagrama + legenda dentro do SVG. No Markdown só `![Diagrama N.x — Título](imagens/slug.svg)` com linha em branco antes/depois.
- Perecível (números) **não** entra na arte como verdade — usar rótulos ("~5-10%") ou "valores no Apêndice Vivo".
- Validar todo SVG com `xmllint --noout`.
- Nomeação: `cap-NN-img-XX-slug.svg` (NN canônico; 19b para o capítulo b).
