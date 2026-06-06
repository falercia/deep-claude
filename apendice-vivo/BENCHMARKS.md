# Benchmarks — Snapshot

> Atualizado em: 2026-06-06 (seed inicial; lançamento oficial em 2026-07)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

Benchmarks oferecem comparação estruturada entre modelos, mas precisam ser lidos com critério. Pontos-chave:

**O número isolado não decide.** Modelo com 75% em SWE-bench pode ser pior na sua aplicação real se sua distribuição de casos é diferente do benchmark. Use benchmark para narrow down de candidatos, decida com eval próprio (Cap 34 do livro).

**Cherry-picking de configuração.** Fornecedores reportam resultados com configuração que favorece (extended thinking, system prompt customizado, retries). Compare resultados com mesma configuração.

**Saturação.** Quando benchmark fica saturado (modelos atingem 95%+), perde poder discriminativo. Comunidade lança benchmarks novos. Apêndice Vivo segue novos benchmarks conforme tração.

---

## Benchmarks rastreados

### SWE-bench Verified

**O que mede.** Capacidade de resolver issues reais de repositórios GitHub Python. Considerado o benchmark mais relevante para agentes de engenharia de software em 2026.

**Como ler.** Score % indica taxa de issues resolvidas corretamente em conjunto verificado de ~500 casos.

**Estado atual (referência).** Modelos top atingiam 60-75% em 2025, com tendência de avanço significativo em 2026.

| Modelo | Score | Configuração | Data |
|---|---|---|---|
| Claude Opus (geração corrente) | TBD | TBD | 2026-MM |
| Claude Sonnet (geração corrente) | TBD | TBD | 2026-MM |
| GPT topo (geração corrente) | TBD | TBD | 2026-MM |
| Gemini topo (geração corrente) | TBD | TBD | 2026-MM |

**Fonte:** https://www.swebench.com/

---

### MMLU-Pro

**O que mede.** Conhecimento geral em 14 áreas (matemática, física, biologia, etc.) com perguntas de múltipla escolha mais difíceis que MMLU original.

**Como ler.** Score % indica taxa de acerto.

**Estado atual.** Saturando em torno de 80-85% nos modelos top.

| Modelo | Score | Data |
|---|---|---|
| Claude Opus (geração corrente) | TBD | 2026-MM |
| Claude Sonnet (geração corrente) | TBD | 2026-MM |

**Fonte:** https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro

---

### GPQA Diamond

**O que mede.** Perguntas de pós-graduação em física, química e biologia. Difícil mesmo para PhDs sem internet.

**Como ler.** Score % indica taxa de acerto em conjunto difícil ("diamond").

**Estado atual.** Top em torno de 60-70%.

| Modelo | Score | Data |
|---|---|---|
| Claude Opus (geração corrente) | TBD | 2026-MM |

**Fonte:** https://huggingface.co/datasets/Idavidrein/gpqa

---

### HumanEval+ / LiveCodeBench

**O que mede.** Capacidade de gerar código funcional para problemas algorítmicos.

**Como ler.** Score % indica pass rate.

**Estado atual.** HumanEval saturado; LiveCodeBench (atualizado mensalmente para evitar data contamination) é mais discriminativo.

| Modelo | LiveCodeBench Score | Data |
|---|---|---|
| Claude Opus (geração corrente) | TBD | 2026-MM |

**Fonte:** https://livecodebench.github.io/

---

### Benchmarks emergentes (2026)

A comunidade de IA produz benchmarks novos conforme os antigos saturam. Apêndice Vivo segue conforme tração:

- **AIME-2026** (matemática olímpica)
- **TerminalBench** (uso de shell e ferramentas)
- **WebArena 2.0** (navegação web autônoma)
- **MLE-bench** (engenharia de machine learning)

---

## Como o leitor usa

**Para escolha de tier**: benchmark é critério inicial. Sonnet típico cobre 70-80% dos casos com qualidade comparável a Opus em benchmarks gerais. Use eval próprio para validar no seu domínio (Cap 34).

**Para acompanhamento de evolução**: leia mensalmente o changelog deste arquivo para ver se houve mudança significativa. Modelo novo que ganha 5+ pontos em SWE-bench em geração anterior pode justificar migração.

**Para discussão executiva**: tenha em mãos 2-3 benchmarks comparáveis quando defender escolha de stack. Argumento estruturado é mais sólido.

---

## Mudanças recentes

- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**TBD — Publicação oficial (2026-07).** Snapshot inicial estabelece estrutura. A publicação oficial em julho de 2026 trará scores específicos conforme leaderboard oficial de cada benchmark.

**Como contribuir.** Observou benchmark novo relevante ou resultado não capturado? Abra issue com label `nova-fonte`. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

- SWE-bench: https://www.swebench.com/
- MMLU-Pro: https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro
- GPQA: https://huggingface.co/datasets/Idavidrein/gpqa
- LiveCodeBench: https://livecodebench.github.io/
- Papers With Code (rankings): https://paperswithcode.com/

Ver [`FONTES.md`](./FONTES.md) para lista completa.
