# Banca Editorial Adversarial — Deep Claude (21/06/2026)

*Parecer aterrado no manuscrito real (47 caps, ~205k palavras, 107 diagramas, Apêndice Vivo J, 80 links ao Livro 1). Não é genérico: cada crítica cita capítulo. A régua não é a média dos livros de IA — é Co-Intelligence, DDIA, Accelerate, Competing in the Age of AI.*

---

## VEREDITO SOBRE AS SUAS 6 DIRETRIZES (a sua pergunta: "quais seguir")

| # | Diretriz do prompt | Veredito | Por quê (aterrado no manuscrito) |
|---|---|---|---|
| 1 | Mais "guerra" / "20 cagadas" | **SEGUIR — reformatado** | A falha hoje é difusa (13 caps têm "quando evitar", mas postmortem concentrado ≈3). Mas "20 cagadas" como listicle flerta com o risco de revista. Faça melhor: **9 modos de falha, um por Invariante violado** + box recorrente "POSTMORTEM". Mais durável, mais citável, on-thesis. |
| 2 | Benchmark competitivo GPT/Gemini/local | **SEGUIR o critério — REJEITAR os números no corpo** | Os números cross-vendor JÁ vivem no Apêndice Vivo (Seções 1-5). Colocar "Claude X% > GPT em benchmark Y" no corpo é exatamente o apodrecimento que "Modelos passam" condena. Crie um **capítulo de decisão durável "Quando Claude, quando não"** por critério de tarefa, apontando ao Apêndice para o número. |
| 3 | Mais material visual | **MAJORITARIAMENTE FEITO — seguir só as lacunas** | Já há **107 diagramas**. Anatomia, contexto, Opus/Sonnet/Haiku, adoção, governança, valor×complexidade, camada dupla — todos existem. Faltam de verdade **3**: mapa unificado do ecossistema, matriz risco×autonomia (genérica), pipeline de uso seguro corporativo. Não adicione diagrama por adicionar. |
| 4 | Mais voz autoral (CTO) | **SEGUIR — prioridade #1** | **Zero ocorrências** de 1ª pessoa executiva no manuscrito inteiro. É a alavanca mais difícil de copiar e está vazia. Maior ROI de diferenciação do livro. |
| 5 | Evitar enciclopédia | **SEGUIR — disciplina contínua** | Risco concentrado na Parte 2 (8-21, produto-a-produto) e em trechos da Parte 3. Veredito por parte na seção 8. |
| 6 | Conexão com Livro 1 | **JÁ FORTE — refinar** | 80 links ao L1. O que falta não é quantidade, é **callback conceitual explícito** em 5-6 pontos-chave (não link solto). |

**Resumo do veredito:** das 6, a #4 (voz autoral) é a de maior impacto e está zerada; a #2 precisa ser desarmada (critério sim, benchmark no corpo não); a #3 já está 90% feita. Não execute o prompt ao pé da letra — ele empurraria o livro para catálogo comparativo datado, o oposto da tese.

---

## 1. DIAGNÓSTICO GERAL

O Deep Claude já é tecnicamente sólido, bem estruturado (Invariante por capítulo), fortemente ilustrado e — depois do reforço prático desta semana — denso em aplicação. O problema **não** é falta de conteúdo. São três:

1. **Ausência de autor.** O livro é impecavelmente impessoal. Lê-se como um currículo brilhante escrito por um comitê, não como o julgamento de um CTO que já sangrou nessas decisões. Isso o torna excelente e **copiável**. A voz é a única coisa que um concorrente não consegue clonar — e ela está desligada.
2. **"Claude falando de Claude".** Fora do Apêndice, quase não há posicionamento honesto sobre *onde Claude não é a escolha*. Isso fragiliza a autoridade: um leitor executivo desconfia de quem só elogia a própria casa.
3. **Falha sanitizada.** A pedagogia do erro existe ("quando evitar"), mas é morna. Faltam histórias de fracasso que doam — o tipo de coisa que faz o leitor pensar "esse já apanhou, posso confiar".

Se os três forem resolvidos, o livro sai de "ótima documentação curada" para "referência com assinatura".

---

## 2. O QUE JÁ ESTÁ FORTE (não mexer)

- **Arquitetura Invariante-por-capítulo.** Cada capítulo ancora num dos 9 Invariantes do L1. É o esqueleto que impede virar catálogo. Mantém.
- **Camada Dupla funcionando.** Perecível (versões/preços/benchmarks) no Apêndice Vivo e no repo; corpo durável. É a defesa estrutural contra o apodrecimento. Mantém e protege.
- **Reforço prático (esta semana).** 47 caps com "situação→o que fazer→ponto de julgamento" + exercício. Bom. Não inflar mais.
- **Sistema visual.** 107 diagramas vetoriais coerentes. Acima da média do mercado.
- **Cap 15 Claude Design e Cap 8 Cowork** como templates de nível.

---

## 3. OS 10 MAIORES RISCOS EDITORIAIS

1. **Risco de commodity por ausência de voz.** Sem autor, qualquer um reproduz o livro com a próxima documentação. (raiz de tudo)
2. **Risco de fanboy.** Sem "quando NÃO Claude" no corpo, perde-se credibilidade executiva.
3. **Risco de catálogo na Parte 2.** 14 capítulos produto-a-produto (8-21) podem ler como índice de features. Precisam de fio condutor mais forte que "mais um produto".
4. **Risco de apodrecimento se o prompt for seguido ao pé da letra** (benchmarks de versão no corpo).
5. **Falha morna.** Pedagogia do erro existe mas não marca.
6. **Parte 3 (engenharia) com risco de "doc reescrita".** Tool Use, MCP, RAG, Embeddings podem soar como tradução da documentação se não ancorarem em decisão/custo/governança.
7. **Excesso de simetria.** Todo capítulo tem a mesma estrutura (conceito→analogia→técnica→quando usar→exemplo→prática→limitações→conexões→resumo→UAU). Previsível demais pode cansar; capítulos-âncora deveriam quebrar o molde.
8. **Apêndice Vivo como ponto único de falha de confiança.** Se os números do Apêndice estiverem TBD/desatualizados na publicação, a promessa "Camada Dupla" vira boleto. (já sinalizado em pendências)
9. **Densidade pós-sweep.** Alguns capítulos podem ter ficado longos; risco de fadiga. Precisa de passe de galé seletivo.
10. **Casos (37-41) ainda lêem como ilustração, não como guerra.** Bons, mas falta a cicatriz real.

---

## 4. OS 20 AJUSTES DE MAIOR IMPACTO (ordenados por ROI)

1. **Ligar a voz do autor.** Criar o box recorrente **"DA CADEIRA DO CTO"** — 1 por capítulo-chave (não em todos), com o julgamento executivo do autor em 1ª pessoa. Começar pelos caps 8, 9, 15, 42, 43, 44, 45.
2. **Capítulo novo "Quando Claude, quando não"** (decisão cross-vendor durável, aponta ao Apêndice para número). Ver seção 5.
3. **Capítulo/Apêndice "Os 9 Modos de Falha"** — um por Invariante violado. Ver seção 5 e 6.
4. **Box "POSTMORTEM" recorrente** nos capítulos de maior risco operacional (Cowork, Code, MCP, RAG, Automação, Governança).
5. **Diagrama: Mapa unificado do ecossistema** (Cowork/Code/Web/Projects/Artifacts/Design/Skills/MCP) — o "você está aqui". Falta de verdade.
6. **Diagrama: Matriz risco×autonomia** (genérica, o eixo visual do Invariante 6). Falta de verdade.
7. **Reposicionar a Parte 2** com um fio condutor: não "14 produtos", mas "uma superfície por nível de autonomia e contexto". Abertura de parte reescrita.
8. **Seções "Como eu, CTO, usaria isto"** em 6 pontos executivos: due diligence, M&A, turnaround, avaliação de adoção, liderar time sem teatro de IA, decisão de build vs buy. Ver seção 5.
9. **Endurecer a falha nos casos (37-41):** cada caso ganha um "o que quase deu errado e por quê" ancorado no Invariante do setor.
10. **Parte 3: amarrar cada capítulo técnico a uma decisão de custo/governança** no parágrafo de abertura, para não soar como documentação.
11. **Callbacks conceituais explícitos ao L1** em 6 pontos (não link: parágrafo que invoca "Modelos passam, método fica", custo composto, governança indelegável).
12. **Quebrar a simetria** em 3-4 capítulos-âncora (8, 15, 42): estrutura própria, mais ensaística.
13. **Box "TEATRO DE IA"** — sinais de que a adoção virou encenação (vaidade de métrica, prompt-theater, piloto eterno). Cap 43.
14. **Matriz "valor×esforço de governança"** para priorização de casos de uso corporativos (cap 42 ou 43).
15. **Diagrama: pipeline de uso seguro corporativo** (dados→escopo→aprovação→eval→produção). Parcial hoje; consolidar.
16. **Galé seletiva** nos capítulos que incharam no sweep (cortar 10-15% sem perder aplicação).
17. **Reduzir a Parte 2 onde for catálogo:** fundir capítulos finos (Desktop+Mobile? Web+Voice?) se não sustentarem peso próprio. Ver seção 8.
18. **Abrir cada Parte com uma página de tese** (por que esta parte existe, em 1ª pessoa).
19. **Glossário de antipadrões** no fim (referência rápida dos modos de falha).
20. **Frase-assinatura por capítulo:** cada capítulo fecha com uma sentença citável (alguns já têm; padronizar). É o que vira post no LinkedIn e constrói autoridade.

---

## 5. NOVOS CAPÍTULOS SUGERIDOS (só os que sobrevivem 10 anos)

| Proposta | Onde | Veredito | Justificativa |
|---|---|---|---|
| **"Quando Claude, quando não"** | Parte 1, novo cap ~5b ou expansão do Cap 5 | **CRIAR** | Critério de tarefa (profundidade de raciocínio, ecossistema de ferramentas, governança/residência de dado, custo, latência) — model-agnóstico. Número vai ao Apêndice. Mata o "fanboy". |
| **"Os 9 Modos de Falha do Claude na Empresa"** | Parte 5 ou Apêndice | **CRIAR** | Um modo por Invariante violado. Durável, citável, hard-to-copy. Substitui com classe o "20 cagadas". |
| **"Como um CTO avalia adoção de Claude"** | Parte 4, expandir Cap 42/43 | **FUNDIR, não criar** | O conteúdo cabe em Governança/Adoção com a voz autoral ligada. Capítulo novo seria redundante. |
| "Claude em M&A / due diligence / turnaround" | — | **NÃO criar capítulo; virar boxes "DA CADEIRA DO CTO"** | Capítulo inteiro por cenário viraria nicho. Como boxes de autoridade nos caps de caso e governança, rende mais. |
| "Como liderar time sem teatro de IA" | Cap 43 (Adoção) | **VIRAR SEÇÃO + box "TEATRO DE IA"** | Forte, mas é seção dentro de Adoção, não capítulo. |

---

## 6. BOXES "GUERRA REAL" (formato e onde)

Formato proposto — **box "POSTMORTEM"** (rotular *composto ilustrativo*, como os demais cenários do livro, por honestidade):
> ⚠️ **POSTMORTEM — [título da falha]**
> O que tentaram · O que deu errado · **O Invariante violado** · O que teria evitado.

Alvos (1 por capítulo de risco):
- Cap 8 Cowork — **"A pasta-raiz que vazou"**: escopo de acesso amplo demais. (Inv. 6)
- Cap 9 Code — **"O agente que refatorou o que não devia"**: autonomia sem revisão. (Inv. 6)
- Cap 6/13 Contexto — **"O projeto que morreu por excesso de contexto"**: context rot, decisão de menos. (Inv. 2)
- Cap 25 Prompt — **"Os 300 prompts que ninguém manteve"**: prompt como ativo sem governança. (Inv. 9)
- Cap 29/30 MCP — **"O conector que mandou e-mail pro cliente errado"**: ação externa irreversível. (Inv. 6/8)
- Cap 36 LLMOps — **"O eval que media o fácil"**: termômetro errado. (Inv. 7)
- Cap 43 Adoção — **"O piloto eterno"** e **"o teatro de IA"**: adoção sem método. (Inv. 8)
- Cap 28 RAG — **"A seguradora que achava que tinha RAG"** (já existe como exemplo; promover a postmortem).

---

## 7. DIAGRAMAS (só o que falta — o resto já existe)

| Diagrama pedido | Já existe? | Ação |
|---|---|---|
| Anatomia da conversa | ✅ cap-03 | nada |
| Hierarquia de contexto | ✅ cap-06/03 | nada |
| Fluxo Opus/Sonnet/Haiku | ✅ cap-05 (×2) | nada |
| Canvas de adoção | ✅ cap-43 (×2) | nada |
| Arquitetura de governança | ✅ cap-42/23 | nada |
| Matriz valor×complexidade | ✅ cap-05/40/44 | nada |
| Camada dupla | ✅ cap-47 | nada |
| **Mapa unificado do ecossistema** | ❌ | **CRIAR** (orientação "você está aqui") |
| **Matriz risco×autonomia (genérica)** | ❌ (só cap-33 específico) | **CRIAR** (eixo visual do Inv. 6) |
| **Pipeline de uso seguro corporativo** | 🟡 parcial (cap-36/42) | **CONSOLIDAR** num diagrama-canônico |

Veredito #3: **não é "mais visual", é "3 diagramas-chave a mais".** O livro já é visual.

---

## 8. CORTES E FUSÕES (manter / cortar / fundir / mover / virar)

| Alvo | Veredito |
|---|---|
| Parte 2 — caps 11 Desktop e 12 Mobile | **AVALIAR FUSÃO** se nenhum sustenta peso próprio ("Claude onde você está: desktop e mobile"). |
| Parte 2 — caps 17 Web Search e 16 Research | **MANTER separados** (Invariantes/funções distintas), mas reforçar a fronteira. |
| Parte 3 — trechos de Tool Use/MCP/Embeddings que listam parâmetros | **MOVER lista para Apêndice/repo; manter no corpo só o critério de decisão.** |
| "Quando evitar" repetitivo em alguns caps | **FUNDIR** com o ponto de julgamento da seção prática onde redundar. |
| Casos 37-41 | **TRANSFORMAR** o desfecho em postmortem (a cicatriz, não só o sucesso). |
| Tabelas de feature longas (Parte 2) | **VIRAR DIAGRAMA ou mover ao Apêndice** — feature muda, diagrama de critério dura. |
| Simetria estrutural rígida | **QUEBRAR** em 3-4 caps-âncora. |

---

## 9. CONEXÃO COM O LIVRO 1 (já 80 links — subir o nível)

Já há ligação estrutural. O upgrade é de **link → callback conceitual** em 6 pontos:
- Abertura da Parte 1: invocar **"Modelos passam. Método fica."** explicitamente como porta de entrada do volume.
- Cap 6/13 (contexto): amarrar a **custo composto** (Inv. 5) — contexto caro é custo que compõe.
- Cap 8/9/15/29 (autonomia): amarrar a **governança indelegável** (Inv. 8), não só ao Inv. 6.
- Cap 35/36 (eval/LLMOps): amarrar à **Pirâmide da Avaliação** (F8) com callback, não link.
- Cap 42/43 (governança/adoção): **adoção com método** vs licença — citar o L1 diretamente.
- Fecho (Cap 47): reafirmar a Camada Dupla como o pacto dos dois livros.

---

## 10. PLANO DE REVISÃO EM 7 DIAS

| Dia | Foco | Entregável |
|---|---|---|
| 1 | **Voz autoral.** Definir o tom "DA CADEIRA DO CTO" + escrever os 6-8 boxes prioritários (caps 8, 9, 15, 42, 43, 44). | Boxes prontos; padrão definido. |
| 2 | **Capítulo "Quando Claude, quando não"** (critério durável, aponta ao Apêndice). | Cap novo redigido. |
| 3 | **"9 Modos de Falha"** + 6 boxes POSTMORTEM nos caps de risco. | Cap/apêndice + boxes. |
| 4 | **3 diagramas que faltam** (ecossistema, risco×autonomia, pipeline seguro) no sistema visual. | 3 SVGs premium. |
| 5 | **Endurecer casos 37-41** (postmortem por setor) + box "Teatro de IA" (cap 43). | Casos revisados. |
| 6 | **Galé seletiva** (cortar 10-15% onde inchou) + fusões da seção 8 + callbacks L1. | Manuscrito enxuto. |
| 7 | **Verificação + rebuild + frases-assinatura** por capítulo. | Build final; QA de links/numeração. |

---

### A pergunta que importa
Não é "o livro está bom?". Está. É: **"daqui a 5 anos, alguém ainda cita este livro — ou cita a documentação que ele resumiu?"** Hoje, o que garante a primeira resposta é a voz do autor e os modos de falha. Os dois estão subexplorados. É aí que está o salto de "muito bom" para "referência nacional".
