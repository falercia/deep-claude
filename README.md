# deep-claude

> O ecossistema Claude na mesa do executivo brasileiro.
> Companheiro executável do livro **Deep Claude · Currículo Executivo do Ecossistema Anthropic** (Fabio Garcia, 2026).

[![Licença código](https://img.shields.io/badge/c%C3%B3digo-MIT-blue)](#licença)
[![Licença conteúdo](https://img.shields.io/badge/conte%C3%BAdo-CC--BY%204.0-lightgrey)](#licença)
[![Cadência Apêndice Vivo](https://img.shields.io/badge/ap%C3%AAndice%20vivo-mensal-orange)](./apendice-vivo/)

---

## Por que este repositório existe

A obra **Deep Claude** opera sob a Camada Dupla aplicada ao ecossistema Anthropic. O livro carrega o padrão durável — frameworks de decisão, arquiteturas de aplicação, vocabulário operacional, fluxos de adoção institucional. Este repositório carrega o que muda — modelos vigentes, preços, benchmarks, janelas de contexto, skills versionados, MCPs de referência, prompts setoriais executáveis, templates de governança.

Sem o livro, este repositório é catálogo sem mapa, com receitas que o leitor desentendido aplicará no contexto errado. Sem o repositório, o livro é vocabulário sem executável, com método que o leitor entendeu mas não consegue colocar em produção sem reescrever cada artefato. Juntos, os dois materializam o currículo executivo do ecossistema Claude, com o leitor que opera com os dois saindo com modelo mental sólido, ativos prontos para entrar em pipeline e calibração temporal mantida via Apêndice Vivo de cadência mensal.

Este repositório é também a outra metade da série iniciada por [`inteligencia-aumentada-recursos`](https://github.com/falercia/inteligencia-aumentada-recursos). O primeiro repositório carrega os Invariantes da IA aplicados em qualquer modelo; este carrega a vertical Claude. Quem usa os dois opera em patamar de domínio raro no mercado brasileiro.

---

## Para quem é

**Para o leitor do livro.** Você terminou *Deep Claude* e quer aterrissar o currículo executivo no seu time, com Apêndice Vivo para calibração mensal, prompts setoriais executáveis, skills prontos para Claude Code e Cowork, templates de governança. Está no lugar certo. Comece em [`/apendice-vivo`](./apendice-vivo/).

**Para o CTO ou Head de Tecnologia em adoção real.** Você precisa estabelecer governança formal de IA, decidir entre Opus, Sonnet e Haiku conforme caso, montar comitê de IA, construir AI cards por sistema. Está no lugar certo. Comece em [`/governance`](./governance/) e leia o [CONTRATO.md](./CONTRATO.md).

**Para o especialista do domínio que quer contribuir.** Você é advogado, médico, analista financeiro, profissional de RH, marketing ou educação, e identificou caso limítrofe que os prompts atuais não cobrem. Sua contribuição é o que faz este repositório virar referência calibrada por painel, não por autor único. Veja [Como contribuir](#como-contribuir).

---

## O que vive aqui

| Pasta | Conteúdo | Capítulos relacionados |
|---|---|---|
| [`/apendice-vivo`](./apendice-vivo/) | Modelos, preços, benchmarks, janelas de contexto, SLAs. Cadência mensal, changelog datado, errata pública | Cap 45 Apêndice Vivo · Cap 4 Modelos · Cap 5 Quando usar tier |
| [`/labs`](./labs/) | Exercícios práticos por capítulo, código executável, datasets de exemplo, scripts de validação | Cap 9, 21, 22, 27, 28, 29, 30, 31, 32, 33, 34, 35 |
| [`/prompts`](./prompts/) | Biblioteca de prompts setoriais executáveis: jurídico, saúde, finanças, SaaS, suporte, RH, marketing, educação | Cap 36-40 (casos por setor) |
| [`/skills`](./skills/) | Skills prontos para Claude Code e Cowork, organizados por domínio profissional | Cap 30 Claude Skills |
| [`/mcps`](./mcps/) | Tutoriais de uso de servidores MCP oficiais e exemplos próprios para integração | Cap 28, 29 MCP |
| [`/governance`](./governance/) | Templates de governança: política-quadro de IA, AI cards, RACI, atas de comitê, runbook ANPD | Cap 41-44 (Governança, Adoção, ROI, LGPD) |
| [`/lancamento`](./lancamento/) | Materiais de divulgação da obra: imagens, posts, threads, decks resumo, scripts de vídeo | Apoio editorial |

Cada pasta tem seu próprio `README.md` com instruções específicas, padrões de uso e exemplos práticos.

---

## Como começar em 60 segundos

```bash
git clone https://github.com/falercia/deep-claude.git
cd deep-claude
```

Três caminhos a partir daqui, conforme seu objetivo:

**1. Quero a referência viva atualizada.** Abra [`/apendice-vivo`](./apendice-vivo/) e leia o snapshot do mês corrente. Em cinco minutos você tem modelos vigentes, preços normalizados em USD e BRL, benchmarks atualizados e janelas de contexto por modelo. Atualizado todo mês entre os dias 1 e 7.

**2. Quero colocar em produção rápido.** Pegue o prompt setorial mais próximo do seu domínio em [`/prompts`](./prompts/), adapte a constituição ao seu contexto, instale o skill correspondente do seu stack em [`/skills`](./skills/), revise o template de governança em [`/governance`](./governance/) e leia os capítulos do livro indicados em cada pasta antes de operar.

**3. Quero contribuir.** Leia [CONTRATO.md](./CONTRATO.md) e abra uma issue com a categoria sugerida. Contribuições qualificadas com fonte primária são incorporadas em revisões futuras, com atribuição quando o contribuidor autoriza.

---

## Estado atual

**Versão 1.0 publicada em julho de 2026, com Apêndice Vivo seed, READMEs estruturados das sete pastas, prompts setoriais essenciais e templates de governança críticos.** Demais artefatos seguem roadmap de evolução versionada.

### Cobertura por pasta

| Pasta | v1.0 (jul/2026) | v1.1 (out/2026) | v1.2 (jan/2027) |
|---|---|---|---|
| `/apendice-vivo` | Seed completo | Atualização mensal contínua | Atualização mensal contínua |
| `/labs` | Labs base (Cap 9, 21, 30) | Labs API/Tool Use/RAG (Cap 22, 27) | Labs Computer Use/Vision/Evals (Cap 32, 33, 34) |
| `/prompts` | 5 prompts seed (1 por setor crítico) | Cobertura completa Cap 36-40 | Variantes regionais e por porte |
| `/skills` | 3 skills core | Cobertura por área de Claude Code | Cobertura para Cowork |
| `/mcps` | Tutoriais de 3 MCPs oficiais | Exemplos próprios e integrações | Padrões avançados |
| `/governance` | Templates essenciais | Cadernos por setor regulado | Runbooks de auditoria |
| `/lancamento` | Materiais do livro | Materiais de cursos e workshops | Materiais de mentorias |

---

## Ponte com `inteligencia-aumentada-recursos`

Este repositório é a segunda metade de um sistema editorial. O primeiro repositório, [`inteligencia-aumentada-recursos`](https://github.com/falercia/inteligencia-aumentada-recursos), carrega os Invariantes da IA aplicados de forma genérica, com 30 prompts profissionais multi-modelo, governança transversal e infraestrutura de evals. Este repositório, `deep-claude`, carrega a vertical específica do ecossistema Claude da Anthropic.

| Repositório | Foco | Público |
|---|---|---|
| `inteligencia-aumentada-recursos` | Invariantes da IA (padrão durável) | Profissional generalista |
| `deep-claude` | Ecossistema Claude (aplicação vertical) | Profissional Claude (vertical específica) |

**Como usar os dois juntos.** Aprenda os Invariantes em *Inteligência Aumentada* e seu repositório; aplique no ecossistema Claude com *Deep Claude* e este repositório; consulte os Apêndices Vivos de ambos para se manter calibrado no tempo.

---

## Princípios editoriais

**Idioma.** Português brasileiro em READMEs, documentação e comentários. Nomes técnicos em inglês onde for padrão da indústria (`skills`, `MCP`, `prompts`).

**Licenciamento dual.** Código sob MIT (máxima liberdade de uso, modificação e distribuição). Conteúdo textual sob CC-BY 4.0 (uso livre com atribuição). Ver [LICENSE-MIT](./LICENSE-MIT) e [LICENSE-CC-BY](./LICENSE-CC-BY).

**Cadência declarada.** Apêndice Vivo atualizado mensalmente (dias 1-7). Demais pastas conforme roadmap. Cadência declarada publicamente é compromisso editorial.

**Errata pública.** Quando informação anterior estava errada, errata explícita com correção no [CHANGELOG.md](./CHANGELOG.md). Honestidade temporal exige errata visível.

**Honestidade nas referências.** Cada item do Apêndice Vivo carrega fonte primária linkada para rastreabilidade. Sem fonte primária, item não entra.

**Sem autopromoção.** Repositório é instrumento de transformação do leitor, não vitrine do autor. Nenhuma sessão é vitrine pessoal.

---

## Como contribuir

Veja [CONTRATO.md](./CONTRATO.md) para os princípios de contribuição.

Em síntese:

1. Abra issue com a categoria correta (erro, sugestão de prompt, novo lab, errata em Apêndice Vivo).
2. Para mudanças textuais, basta a issue. Para código ou prompt novo, abra Pull Request.
3. Use fonte primária. Sem fonte primária linkada, contribuição não é incorporada.
4. Sem autopromoção. Contribuição é técnica, não marketing.

---

## Licença

**Código** (scripts, configurações, exemplos): [MIT](./LICENSE-MIT)

**Conteúdo textual** (READMEs, documentação, Apêndice Vivo, prompts): [CC-BY 4.0](./LICENSE-CC-BY)

Atribuição: Fabio Garcia, *Deep Claude · Currículo Executivo do Ecossistema Anthropic* (2026).

---

## Autor e contato

**Fabio Garcia** — CTO e Head de Tecnologia, autor da série *Inteligência Aumentada*.

- GitHub: [@falercia](https://github.com/falercia)
- Repositório do Livro 1: [`inteligencia-aumentada-recursos`](https://github.com/falercia/inteligencia-aumentada-recursos)
- Para sugestões, abra issue neste repositório.

---

> *"O livro carrega o método; o repositório carrega o código. Quem terminar o livro sem visitar o repositório aproveitou metade."*
> — *Deep Claude*, Capítulo 46
