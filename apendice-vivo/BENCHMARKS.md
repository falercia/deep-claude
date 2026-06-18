# Benchmarks — Snapshot

> **Snapshot 2026-06-18 · rascunho para conferência do autor**
> Atualizado em: 2026-06-18 (populamento com dados correntes — ver CHANGELOG-APENDICE.md)
> Atualizado anteriormente: 2026-06-06 (seed inicial)
> Próxima atualização: 2026-07-01 a 2026-07-07
> Fonte: ver [`FONTES.md`](./FONTES.md)

---

## Princípio de leitura

Benchmarks oferecem comparação estruturada entre modelos, mas precisam ser lidos com critério. Pontos-chave:

**O número isolado não decide.** Modelo com 75% em SWE-bench pode ser pior na sua aplicação real se sua distribuição de casos é diferente do benchmark. Use benchmark para narrow down de candidatos, decida com eval próprio (Cap 34 do livro).

**Cherry-picking de configuração.** Fornecedores reportam resultados com configuração que favorece (extended thinking, system prompt customizado, retries). Compare resultados com mesma configuração.

**Saturação.** Quando benchmark fica saturado (modelos atingem 95%+), perde poder discriminativo. Comunidade lança benchmarks novos. Apêndice Vivo segue novos benchmarks conforme tração.

---

## SWE-bench Verified

**O que mede.** Capacidade de resolver issues reais de repositórios GitHub Python. Considerado benchmark central para agentes de engenharia de software.

**Como ler.** Score % indica taxa de issues resolvidas corretamente em conjunto verificado de ~500 casos.

**Estado junho 2026.** Benchmark com forte saturação no topo: Claude Mythos 5 e Fable 5 atingiram 95%+. Os leaderboards múltiplos (SWE-bench oficial, vals.ai, llm-stats.com) mostram resultados ligeiramente distintos por configuração de scaffolding.

| Modelo | Score (SWE-bench Verified) | Configuração | Fonte/Data |
|---|---|---|---|
| **Claude Mythos 5** | ~95,5% | — | morphllm.com / 2026-06-18 |
| **Claude Fable 5** | ~95,0% | — | morphllm.com / 2026-06-18 |
| **Claude Opus 4.8** | ~88,6% | — | morphllm.com / 2026-06-18 |
| **Claude Opus 4.7** | ~82,0% | — | morphllm.com / 2026-06-18 |
| **GPT-5.5** | ~82,6% | — | morphllm.com / 2026-06-18 |
| **Gemini 3.5 Flash** | ~78,8% | — | morphllm.com / 2026-06-18 |

· fonte: https://www.morphllm.com/claude-benchmarks · data: 2026-06-18

**Atenção.** Scores acima são de terceiros (morphllm.com). Para scores verificados pelo leaderboard oficial, consultar diretamente https://www.swebench.com/verified.html — o site oficial usa JavaScript dinâmico e os números exatos dependem de configuração de scaffolding (agente usado). Confirmar antes de citar em contexto executivo.

**Score mini-SWE-agent v2.** O mini-SWE-agent open source marcou 65% em julho/2025, referência para benchmarking de agentes customizados.
· fonte: https://www.swebench.com/ (news section) · data: 2026-06-18

---

## GPQA Diamond

**O que mede.** Perguntas de pós-graduação em física, química e biologia elaboradas por PhDs. Difícil mesmo para especialistas sem internet: PhDs sem web access acertam ~65%.

**Como ler.** Score % indica taxa de acerto no conjunto "diamond" (~198 questões).

**Estado junho 2026.** Benchmark em estado de saturação avançada. Topo da faixa: 93-94%.

| Modelo | Score GPQA Diamond | Configuração | Fonte/Data |
|---|---|---|---|
| **Gemini 3.1 Pro Preview** | ~94,1-94,3% | — | WebSearch (benchlm.ai, artificialanalysis.ai) / 2026-06-18 |
| **GPT-5.5 (xhigh)** | ~93,5% | — | WebSearch / 2026-06-18 |
| **Claude Opus 4.7 (Adaptive)** | ~94,2% | Adaptive thinking | WebSearch / 2026-06-18 |
| **Claude Opus 4.8** | ~93,6% | — | WebSearch / 2026-06-18 |
| **Claude Opus 4.6** | ~91,3% | — | WebSearch / 2026-06-18 |

· fonte: https://artificialanalysis.ai/evaluations/gpqa-diamond · data: 2026-06-18

**Atenção.** Scores acima obtidos via WebSearch — confirmar no leaderboard oficial https://artificialanalysis.ai/evaluations/gpqa-diamond antes de uso executivo. Variações entre fontes existem por diferença de versão, configuração e data de avaliação.

---

## AIME (Matemática Olímpica)

**O que mede.** American Invitational Mathematics Examination — raciocínio matemático profundo, problemas de olimpíada. AIME 2025 tornou-se referência principal em 2025/2026.

**Como ler.** Score % ou número de acertos (15 questões por edição típica).

**Estado junho 2026.** Benchmark em saturação para os top models: GPT-5.2 e Gemini 3 Pro atingiram 100% em AIME 2025 segundo fontes agregadas.

| Modelo | Score AIME 2025 | Fonte/Data |
|---|---|---|
| **GPT-5.2** | ~100% | WebSearch (lmcouncil.ai) / 2026-06-18 |
| **Gemini 3 Pro** | ~100% | WebSearch (lmcouncil.ai) / 2026-06-18 |
| **Kimi K2 Thinking** | ~99,1% | WebSearch / 2026-06-18 |
| **Claude Opus 4.x** | TBD (a confirmar) | Fonte primária não encontrada / 2026-06-18 |

· fonte: https://lmcouncil.ai/benchmarks (via WebSearch) · data: 2026-06-18

**Atenção.** Scores acima de fontes agregadas de terceiros. Para scores Claude em AIME, verificar em https://www.anthropic.com/research ou nos model cards de lançamento.

---

## MMLU-Pro

**O que mede.** Conhecimento geral em 14 áreas (matemática, física, biologia, etc.) com perguntas de múltipla escolha mais difíceis que MMLU original.

**Como ler.** Score % indica taxa de acerto.

**Estado junho 2026.** Benchmark em processo de saturação nos modelos top (~85%+). Poder discriminativo decaindo.

| Modelo | Score MMLU-Pro | Fonte/Data |
|---|---|---|
| Claude Opus 4.x | TBD (a confirmar) | Fonte primária não encontrada / 2026-06-18 |

· fonte: https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro · data: 2026-06-18

---

## LiveCodeBench

**O que mede.** Capacidade de gerar código funcional para problemas algorítmicos, com atualização mensal para evitar data contamination.

**Como ler.** Score % indica pass rate.

**Estado junho 2026.** Mais discriminativo que HumanEval (saturado).

| Modelo | LiveCodeBench Score | Fonte/Data |
|---|---|---|
| Modelos topo | TBD (a confirmar) | Leaderboard dinâmico / 2026-06-18 |

· fonte: https://livecodebench.github.io/ · data: 2026-06-18

**Nota.** O leaderboard LiveCodeBench é atualizado mensalmente. Consultar diretamente para scores correntes.

---

## Benchmarks emergentes (2026)

A comunidade de IA produz benchmarks novos conforme os antigos saturam:

- **SWE-bench Pro** (2026) — extensão com tarefas mais longas e complexas; Claude Fable 5 lidera com ~80,3% conforme morphllm.com
- **CodeClash** (11/2025) — avalia LMs como desenvolvedores orientados a objetivos, não apenas tarefas
- **TerminalBench** — uso de shell e ferramentas
- **MLE-bench** — engenharia de machine learning
- **AIME-2026** — edição 2026 do benchmark matemático olímpico

---

## Como o leitor usa

**Para escolha de tier**: benchmark é critério inicial. Sonnet 4.6 típico cobre 70-80% dos casos com qualidade comparável a Opus em benchmarks gerais. Use eval próprio para validar no seu domínio (Cap 34).

**Para acompanhamento de evolução**: leia mensalmente o changelog deste arquivo para ver se houve mudança significativa. Modelo novo que ganha 5+ pontos em SWE-bench em geração anterior pode justificar migração.

**Para discussão executiva**: tenha em mãos 2-3 benchmarks comparáveis quando defender escolha de stack. Argumento estruturado é mais sólido.

---

## Mudanças recentes

- **2026-06-18**: snapshot populado com dados correntes de SWE-bench, GPQA Diamond e AIME, obtidos via pesquisa web e fontes primárias. Notas de cautela adicionadas onde fonte é agregador terceiro.
- **2026-06-06**: snapshot seed criado.

---

## Notas editoriais

**Cautelar editorial.** Vários scores neste snapshot vêm de agregadores web (morphllm.com, lmcouncil.ai, artificialanalysis.ai), não diretamente dos leaderboards oficiais dinâmicos (que usam JavaScript e não são acessíveis via fetch estático). O autor deve confirmar os números chave contra os leaderboards oficiais antes da publicação.

**Como contribuir.** Observou benchmark novo relevante ou resultado não capturado? Abra issue com label `nova-fonte`. Veja [CONTRATO.md](../CONTRATO.md).

---

## Fontes primárias

- SWE-bench (oficial): https://www.swebench.com/
- SWE-bench Verified (leaderboard): https://www.swebench.com/verified.html
- GPQA leaderboard (Artificial Analysis): https://artificialanalysis.ai/evaluations/gpqa-diamond
- GPQA (HuggingFace): https://huggingface.co/datasets/Idavidrein/gpqa
- MMLU-Pro: https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro
- LiveCodeBench: https://livecodebench.github.io/
- LM Council (benchmarks agregados): https://lmcouncil.ai/benchmarks
- Papers With Code (rankings): https://paperswithcode.com/
- morphllm Claude benchmarks: https://www.morphllm.com/claude-benchmarks

Ver [`FONTES.md`](./FONTES.md) para lista completa.
