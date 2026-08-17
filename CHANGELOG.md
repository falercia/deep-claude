# Changelog

Todas as mudanças relevantes deste repositório são registradas aqui, em ordem cronológica reversa, com data, autor e fonte primária quando aplicável.

O formato segue [Keep a Changelog](https://keepachangelog.com/) e o versionamento segue [Semantic Versioning](https://semver.org/).

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
