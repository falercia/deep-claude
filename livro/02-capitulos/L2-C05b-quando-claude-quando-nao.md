# CAPÍTULO 5b
## QUANDO CLAUDE, QUANDO NÃO

---

> *"A escolha de ferramenta é um ato de método antes de ser um ato de preferência. Encaixe errado não é sinal de que a IA falhou — é sinal de que o profissional não leu a tarefa."*

---

> 🧭 **Por que este capítulo é a aplicação do Invariante 4 — Encaixe**
>
> O Capítulo 5 resolveu a pergunta interna à família Claude: dado que você já escolheu Claude, qual tier usar? Este capítulo recua um passo: **devia ser Claude?** A escolha entre Claude, outro modelo de fronteira, um modelo local ou open-weight, automação determinística ou nada de IA é uma decisão de encaixe entre tarefa e ferramenta — não de marca, não de familiaridade, não de entusiasmo com a última demonstração pública. Errar esse encaixe custa mais do que errar o tier: você aplica a ferramenta errada ao problema certo e cria um ativo de baixo valor com alto custo de manutenção.
>
> Âncora completa: **Framework 2 — Diagnóstico de Encaixe** → [L1-F2-encaixe-5.md](../../Livro-1-Os-Invariantes/03-frameworks/L1-F2-encaixe-5.md)

---

## 5b.1 — O CONCEITO INTUITIVO

A história do mercado de IA se repete: surge uma ferramenta nova, equipes adotam por antecipação, e seis meses depois alguém pergunta por que o custo subiu sem que a qualidade dos resultados tenha acompanhado. O diagnóstico correto é quase sempre o mesmo: a ferramenta foi aplicada a tarefas que não a pediam.

Claude é um modelo de linguagem de fronteira, projetado e otimizado para tarefas que exigem raciocínio profundo, geração fluente de linguagem natural, análise de ambiguidade, integração de contexto complexo e produção de saída com nuance. Quando a tarefa tem essas características, Claude performa com vantagem sustentável. Quando a tarefa não tem essas características, Claude tende a ser, ao mesmo tempo, caro demais, lento demais, e — paradoxalmente — impreciso demais: a riqueza probabilística do modelo se torna ruído onde o que a tarefa pede é exatidão determinística.

A decisão de encaixe não é lealdade de fornecedor. É uma pergunta técnica com dimensões econômicas, de governança e de risco: **esta tarefa, neste volume, com esta tolerância de erro, com esses dados, sob esta governança, se beneficia de Claude mais do que de qualquer alternativa disponível?**

Quando a resposta é sim, Claude é a escolha. Quando é não, este capítulo diz por quê — e o diz com honestidade.

---

## 5b.2 — OS CRITÉRIOS DURÁVEIS DE ENCAIXE

A tabela da seção seguinte operacionaliza esses critérios. Antes de chegar a ela, vale entender o que cada um mede — e por que são critérios, não checklist.

Os critérios abaixo são **estruturalmente duráveis**: não dependem de versões de modelos, preços correntes ou benchmarks do momento. Os números que os acompanham em decisões reais — custo por milhão de tokens, pontuação em evals, tamanho de janela de contexto — são voláteis e moram no [Apêndice Vivo (J)](../04-apendices/L2-APX-J-apendice-vivo.md).

### 5b.2.1 — Profundidade de raciocínio exigida

É o critério que mais diferencia Claude de alternativas. Tarefas que exigem raciocínio encadeado, manuseio de ambiguidade semântica, síntese de contexto heterogêneo e output com nuance favorecem modelos de fronteira. Tarefas que pedem resposta dentro de um espaço pequeno de possibilidades predefinidas — classificação binária, extração de campos com esquema fixo, roteamento por regra — não se beneficiam dessa profundidade: o raciocínio é irrelevante quando a resposta correta é "sim ou não" ou "campo A ou campo B".

Pergunta de triagem: **a tarefa exige que o modelo forme julgamento, ou apenas que ele reconheça e repita um padrão?**

### 5b.2.2 — Ecossistema de ferramentas e integração

Claude tem integração nativa com o ecossistema Anthropic — API, MCP, Claude Code, Artifacts, Cowork, Design, Research. Se o fluxo de trabalho se beneficia dessas integrações, ou se a organização já tem investimento acumulado em prompts e configurações Claude, o custo de migração para uma alternativa precisa entrar na conta. Se o ambiente técnico tem integrações consolidadas com outro ecossistema (Azure OpenAI com Microsoft 365, Gemini com Google Workspace), a balança inclina em outra direção. O critério não é "qual modelo é mais capaz em abstrato", mas "qual encaixe técnico produz menos fricção neste ambiente".

### 5b.2.3 — Governança, residência e sensibilidade do dado

Este critério frequentemente encerra a discussão antes dos outros entrarem. Dados pessoais sensíveis, registros de saúde, informações jurídicas privilegiadas e dados regulados impõem exigências de residência geográfica, isolamento de tenant e auditabilidade que a escolha do provedor e da modalidade de implantação controlam — não a escolha do modelo. Um modelo local ou open-weight on-premises é, para alguns regimes regulatórios, a única opção legalmente admissível, independentemente de qualquer comparação de capacidade.

Pergunta de triagem: **os dados desta tarefa podem sair do perímetro da organização? Sob qual regime legal?**

### 5b.2.4 — Custo e latência

Claude é precificado como serviço de fronteira — premium em relação a modelos menores e soluções determinísticas. Para tarefas de alto volume e baixa complexidade, a conta não fecha: a diferença de custo multiplicada pelo volume supera qualquer ganho de qualidade. Latência segue o mesmo raciocínio: Claude é adequado para uso interativo e pipelines de volume moderado; para resposta em dezenas de milissegundos em escala massiva, a arquitetura precisa de outra camada.

### 5b.2.5 — Reversibilidade e risco do erro

Tarefas onde o erro é irreversível ou de alto custo de correção pedem revisão humana na saída, independentemente do modelo. O Invariante 8 (Responsabilidade Indelegável) não é sobre modelos: a responsabilidade pelo output permanece com o humano que assina. Para tarefas onde o erro tem baixo custo de reversão e pode ser corrigido por amostragem, modelos menores ou automação determinística são candidatos legítimos.

### 5b.2.6 — Maturidade do caso de uso

Em exploração, a flexibilidade de Claude — lidar com inputs variados, produzir output rico para avaliação humana, adaptar formato — é vantagem clara. Em produção estável com volume alto e input bem-estruturado, a mesma flexibilidade pode ser custo desnecessário: o caso pode ter amadurecido até o ponto onde automação determinística — regras, workflow codificado, modelo menor fine-tuned — entrega o mesmo resultado a fração do custo e com muito mais previsibilidade.

---

## 5b.3 — TABELA DE DECISÃO: QUANDO CADA CAMINHO BRILHA

A tabela que segue é um instrumento de raciocínio, não uma prescrição automática. Leia as colunas como "quando esta opção tem vantagem comparativa" — e aplique os critérios da seção anterior para calibrar ao seu caso.

| Situação | Claude (fronteira, via API ou produto) | Outro modelo de fronteira (GPT, Gemini, outros) | Modelo local ou open-weight | Automação determinística (regras, scripts, workflows codificados) | Nada de IA |
|---|---|---|---|---|---|
| Tarefa exige raciocínio profundo, síntese de contexto heterogêneo, geração com nuance | **Brilha** — perfil natural do modelo | Candidato legítimo — compare por eval no seu caso | Raramente adequado em tarefas genuinamente complexas | Inadequado — a tarefa exige julgamento, não execução de regra | Inadequado para este perfil |
| Fluxo integra Claude Code, MCP, Cowork, Design ou ecossistema Anthropic | **Brilha** — integração nativa sem fricção | Custo de integração adicional | Sem integração nativa | Sem integração | Sem integração |
| Ambiente Microsoft 365 / Azure já consolidado na organização | Candidato, com custo de integração | **Brilha** — GPT4 via Azure OpenAI tem integração nativa | Candidato dependendo de infraestrutura | Candidato para casos maduros e bem-definidos | Candidato se o processo funciona sem IA |
| Dado sensível com restrição de residência ou regime regulatório rígido | Apenas se provedor atende a conformidade exigida | Apenas se provedor atende a conformidade exigida | **Brilha** — on-premises, sem saída de dados | N/A — dados nunca saem | Preferível à exposição de dado sensível a risco regulatório |
| Volume muito alto, tarefa simples (classificar, extrair campo fixo, rotear) | Custo elevado para o valor entregue | Custo elevado para o valor entregue | Candidato forte — fine-tune em modelo menor | **Brilha** — regra determinística entrega exatidão com custo próximo de zero | Candidato se a automação atual é suficiente |
| Requisito de latência em dezenas de milissegundos, escala massiva | Latência incompatível com o requisito | Latência incompatível com o requisito | **Brilha** — modelo local sem chamada de API | **Brilha** — sem overhead de LLM | Candidato |
| Caso de uso exploratório, entrada variada, saída para avaliação humana | **Brilha** — flexibilidade e riqueza de output | Candidato | Candidato com limitações de capacidade | Inadequado para exploração | Inadequado se há valor a extrair |
| Processo bem-definido, input estruturado, sem ambiguidade semântica | Superdimensionado para a tarefa | Superdimensionado para a tarefa | Candidato — fine-tune estreito pode ser superior | **Brilha** — exatidão e previsibilidade máximas | **Brilha** — se o processo manual funciona e o custo de automação não se paga |

> ⚠️ **Nota sobre benchmarks na tabela acima:** nenhuma célula cita número de benchmark porque benchmarks mudam a cada ciclo de lançamento. O que a tabela captura são vantagens estruturais — posicionamento por tipo de tarefa — que tendem a ser mais estáveis. Para comparações quantitativas no momento da sua decisão, consulte o [Apêndice Vivo (J)](../04-apendices/L2-APX-J-apendice-vivo.md).

---

## 5b.4 — PARA EXECUTIVOS

> 🎯 **PARA EXECUTIVOS**
>
> A pergunta que mais frequentemente não é feita nas reuniões de adoção de IA é: **precisamos mesmo de um modelo de fronteira para isso?** Equipes otimistas adotam Claude como padrão para toda nova iniciativa, e o custo sobe antes que o valor apareça.
>
> A disciplina executiva começa com três políticas de encaixe, antes de assinar qualquer contrato de plataforma.
>
> **Primeira:** estabeleça uma tipologia das suas tarefas antes de escolher modelo. Separe raciocínio profundo (síntese, análise, nuance) de trabalho estruturado de alto volume (classificação, extração, roteamento). A primeira categoria justifica modelos de fronteira; a segunda raramente. Essa separação, feita uma vez, orienta dezenas de decisões de arquitetura.
>
> **Segunda:** custo total não é custo de API. Inclua integração, manutenção de prompts, revisão humana, governança de dado e eventual fine-tuning de alternativa. Modelos menores parecem baratos na planilha e caros na manutenção; o inverso vale para modelos de fronteira em alta complexidade. A comparação honesta é total cost of ownership por unidade de valor entregue.
>
> **Terceira:** governança de dado decide antes de capacidade de modelo. Se os dados não podem sair do perímetro da organização, a discussão "Claude vs. GPT vs. Gemini" é prematura. A pergunta correta é "on-premises ou cloud com conformidade verificada?" — e essa resposta pode eliminar todas as opções de cloud.
>
> Claude é uma ferramenta excelente no seu perfil. Excelente no perfil errado ainda é errado.

---

## 5b.5 — NA PRÁTICA: TRÊS SITUAÇÕES E O QUE FAZER

As situações abaixo são compostas e ilustrativas, na forma *situação → o que fazer → ponto de julgamento*: o passo a passo é replicável, mas o ponto de julgamento é onde o critério vira decisão.

**Situação 1 — A triagem de contratos jurídicos.**
*Situação:* um escritório de advocacia recebe centenas de contratos por mês. Parte exige análise crítica de cláusulas atípicas, síntese de riscos e redação de pareceres. Parte exige apenas conferência de campos padrão (partes, objeto, vigência, valor) para registro. *O que fazer:* aplicar Claude à primeira categoria — raciocínio profundo, saída com nuance, revisão de advogado sênior. Para a segunda, avaliar extração determinística com estrutura fixa; se a variação for alta, considerar modelo menor fine-tuned. *Ponto de julgamento:* se 80% é conferência de campos, usar Claude para tudo é pagar preço de fronteira por extração estruturada. O erro é emocional, não técnico: a equipe não quer "desclassificar" parte do trabalho e aplica o modelo premium indiscriminadamente.

**Situação 2 — O atendimento de suporte de SaaS.**
*Situação:* empresa de SaaS atende 50 mil tickets por mês: 60% são perguntas com resposta em base de conhecimento, 30% exigem diagnóstico técnico e 10% são casos de escalada com contexto acumulado. *O que fazer:* aplicar automação determinística (busca em base de conhecimento + template) na primeira categoria; Claude na segunda e terceira. Implementar classificador em modelo menor para rotear antes de consumir tokens do modelo de fronteira. *Ponto de julgamento:* o classificador precisa de teste rigoroso — falso negativo (caso complexo classificado como simples) gera resposta inadequada e custo de escalonamento que anula a economia do roteamento. Teste com amostra auditada manualmente, não com presunção de que "o modelo vai acertar".

**Situação 3 — A análise de risco regulatório em banco.**
*Situação:* área de compliance analisa semanalmente documentos regulatórios do banco central e reguladores setoriais, cruzando com políticas internas para identificar impactos. Dados incluem informações sensíveis e documentos não públicos. *O que fazer:* avaliar se a política de segurança permite envio a cloud de terceiro — muitos bancos têm política de não saída para dado classificado. Se sim, usar Claude via API com contrato de processamento adequado e revisão humana do output. Se não, avaliar modelo open-weight on-premises com janela de contexto suficiente. *Ponto de julgamento:* a comparação de capacidade entre "Claude via cloud" e "modelo on-premises" é secundária à conformidade regulatória. Escolher a ferramenta mais capaz que a política não admite é erro de sequência de decisão.

> 🔧 **EXERCÍCIO**
>
> Escolha uma iniciativa de IA ativa ou planejada na sua organização — ou na sua rotina, se for uso individual. Aplique os seis critérios da seção 5b.2, respondendo cada um com evidência concreta, não com intuição.
>
> Ao terminar: **a escolha de ferramenta sobrevive a esse escrutínio?** Se não — se algum critério aponta para outra opção —, registre qual critério mudaria a decisão e o que impede de agir. Às vezes o impedimento é técnico; com mais frequência é político ou emocional. Nomear o impedimento é o primeiro passo para resolvê-lo.

---

## 5b.6 — CONEXÕES

- 🔗 **Capítulo-irmão: o roteamento dentro da família Claude** → [Capítulo 5 — Quando Usar Opus, Sonnet, Haiku](L2-C05-quando-usar-modelos.md)
- 🔗 **Framework completo de encaixe com 5 eixos (válido para qualquer provedor)** → [Framework 2 — Diagnóstico de Encaixe](../../Livro-1-Os-Invariantes/03-frameworks/L1-F2-encaixe-5.md)
- 🔗 **Números correntes: preços, benchmarks, versões disponíveis** → [Apêndice Vivo (J)](../04-apendices/L2-APX-J-apendice-vivo.md)
- 🔗 **Invariante 4 — Encaixe (formulação completa)** → Livro 1 — Os Invariantes, Capítulo 4
- 🔗 **Quando delegar e quanto: a escala de autonomia** → Framework 3 — Escala de Propriedade do Agente (Livro 1)
- 🔗 **A responsabilidade que não migra com a ferramenta** → Framework 6 — Governança Indelegável (Livro 1)

---

## 5b.7 — RESUMO EXECUTIVO

| Conceito | Síntese |
|----------|---------|
| **A pergunta deste capítulo** | Devia ser Claude? — a pergunta antes de "qual Claude?" |
| **Invariante regente** | 4 — Encaixe: a escolha correta é entre tarefa e ferramenta, não entre marcas |
| **Critério 1 — Raciocínio** | Tarefas com julgamento, ambiguidade e nuance favorecem fronteira; tarefas com resposta predefinida não |
| **Critério 2 — Ecossistema** | Integração nativa com o ecossistema do fornecedor reduz fricção; migração tem custo real |
| **Critério 3 — Governança do dado** | Residência e conformidade podem eliminar opções de cloud antes de qualquer comparação de capacidade |
| **Critério 4 — Custo e latência** | Volume alto com complexidade baixa favorece modelo menor ou automação determinística |
| **Critério 5 — Reversibilidade** | Erros irreversíveis pedem revisão humana, independentemente do modelo |
| **Critério 6 — Maturidade do caso** | Caso maduro com input bem-estruturado pode ter migrado para automação determinística sem perda |
| **Quando Claude brilha** | Raciocínio profundo, síntese de contexto heterogêneo, geração com nuance, integração com ecossistema Anthropic |
| **Quando honestamente não é a primeira escolha** | Volume alto + complexidade baixa; dado que não pode sair do perímetro; latência crítica em escala; caso maduro e bem-definido |
| **Regra de ouro** | Critério durável no corpo; número corrente no Apêndice Vivo. Encaixe errado é sempre erro de método, nunca de modelo |

---

## 5b.8 — VALIDAÇÃO UAU

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | **Clareza** — Explicar a diferença entre "qual Claude usar" (Cap. 5) e "devia ser Claude" (este capítulo) em 30 segundos | ☐ |
| 2 | **Critérios** — Nomear os 6 critérios de encaixe e dar um exemplo de como cada um pode inverter uma decisão | ☐ |
| 3 | **Tabela** — Para uma tarefa real da sua organização, preencher a linha correspondente da tabela de decisão com justificativa | ☐ |
| 4 | **Honestidade** — Identificar uma iniciativa de IA na sua organização onde Claude (ou qualquer fronteira) pode ser a escolha errada, e nomear a alternativa correta | ☐ |
| 5 | **Governança** — Aplicar o critério de residência de dado a uma tarefa concreta e concluir se ela pode ir a cloud ou deve ficar on-premises | ☐ |

**5 de 5?** Você opera o Invariante 4 com maturidade — a decisão de ferramenta está separada da decisão de marca.
**3 ou 4?** Releia a seção 5b.3 e aplique a tabela a dois casos reais seus antes de avançar.
**Menos de 3?** Retome o Cap. 5 para solidificar o roteamento dentro da família Claude; este capítulo é o passo seguinte, não substituto.

---

🔗 **Próximo capítulo:** [Capítulo 6 — Refresher: Tokens e Contexto](L2-C06-tokens-contexto.md)

---

> *"Usar Claude quando Claude não é a resposta é um erro de método disfarçado de ambição tecnológica. O critério de encaixe não é sobre o que o modelo pode fazer — é sobre o que a tarefa precisa que seja feito."*
