# CAPÍTULO 17
## CLAUDE WEB SEARCH

---

> *"Web Search é o complemento que tira Claude do isolamento do treino e o coloca em contato com o mundo atual. Bem usado, fecha a lacuna mais óbvia entre conhecimento congelado e realidade viva."*

---

> 🧭 **Por que este capítulo é a aplicação do Invariante 1 — Plausibilidade**
>
> Web Search é o antídoto parcial à Plausibilidade: quando o modelo não sabe, pergunta a uma fonte fora dele. Não elimina alucinação; restringe a superfície em que ela atua.

---

## 17.1 — O CONCEITO INTUITIVO

Existe uma limitação estrutural de modelos de linguagem que vimos no Capítulo 2. Todo modelo foi treinado com dados até uma data de corte; depois disso, não sabe nada do que aconteceu, a menos que receba a informação no contexto da conversa. Para Claude em maio de 2026, o conhecimento direto se estende até alguns meses atrás — lacuna que cresce conforme o tempo passa.

Web Search resolve essa lacuna. Quando ativado, Claude pode, durante o raciocínio, fazer consultas à web em tempo real, ler páginas relevantes, extrair informação e usar isso para compor a resposta. Diferente de Research — processo profundo com subagentes paralelos — Web Search é mais leve, mais rápido e pontual. O modelo consulta algumas páginas em uma única busca, em segundos (latências e volumes atuais no [Apêndice Vivo (J)](../04-apendices/L2-APX-J-apendice-vivo.md)). A resposta integra os achados com citações inline.

Em uso profissional, Web Search separa "Claude limitado ao corte de treino" de "Claude conectado ao presente". Quando você precisa de cotação atual, evento recente, especificação de produto lançado essa semana ou status de regulação que mudou ontem, Web Search resolve. O modelo para de inventar plausibilidade onde pode fornecer fato verificado.

---

## 17.2 — ANALOGIA: O ASSISTENTE QUE TEM ACESSO AO JORNAL

Pense em dois assistentes executivos. O primeiro é extremamente competente — vasto conhecimento sobre praticamente tudo que importa para o trabalho — mas trancado em um escritório sem internet. Para temas do dia, responde "pelo que eu sei até dois meses atrás, era assim". Útil para temas estáveis, problemático para tudo que evolui.

O segundo tem a mesma competência, mas pode consultar jornais, sites e fontes oficiais quando precisa. Para tema estável, responde do próprio conhecimento. Para tema atual, consulta as fontes, volta com a informação atualizada e cita a origem.

Claude com Web Search é o segundo assistente. O modelo escolhe automaticamente quando consultar a web e quando responder do treino — ou você força o comportamento quando faz diferença.

---

## 17.3 — EXPLICAÇÃO TÉCNICA

### 17.3.1 — Como funciona a busca por dentro

Quando Web Search está ativo e Claude identifica que a pergunta exige informação atual, alguns passos acontecem.

> 📊 **Diagrama 17.1 — Mecânica do Claude Web Search**
>
> ![Fluxo Web Search](imagens/cap-17-img-01-fluxo-web-search.svg)
>
> *Busca pontual com citações inline, em segundos.*

Primeiro, Claude formula a query de busca otimizada para o motor de pesquisa, frequentemente diferente da pergunta original do usuário. Se você pergunta "qual o impacto da nova regulação do Banco Central sobre Open Finance?", Claude pode buscar com query mais específica como "regulação Open Finance Banco Central Brasil 2026 mudança recente".

Em seguida, o sistema executa a busca em tempo real, recebe resultados e seleciona as fontes mais promissoras — tipicamente três a dez páginas. A seleção prioriza fontes autoritativas e descarta spam, mas sem garantia perfeita.

Depois, o sistema lê essas páginas, extrai trechos relevantes e descarta ruído. Esse conteúdo entra no contexto como material recuperado, pronto para Claude usar na resposta.

Finalmente, Claude compõe a resposta integrando conhecimento próprio com informação recuperada, com citações inline para cada afirmação derivada da web. O comportamento exato das citações varia por interface.

### 17.3.2 — Como ativar e calibrar

A forma de ativar Web Search depende da interface e do plano — consulte o [Apêndice Vivo (J)](../04-apendices/L2-APX-J-apendice-vivo.md) para o estado atual. Pode ser ativado pontualmente ou permanecer sempre ativo. Em modo automático, Claude decide quando buscar; em modo manual, você controla.

Para uso profissional, vale conhecer quatro técnicas que melhoram a qualidade da busca:

Primeiro, **seja específico sobre temporalidade quando importa**. Em vez de "regulação do BCB sobre fintechs", peça "regulação do BCB sobre fintechs em 2026 ou mais recente".

Segundo, **especifique o tipo de fonte quando relevante**. "Privilegie fontes oficiais como Bacen e CVM" guia a triagem. "Inclua perspectivas brasileiras" evita resultado dominado por conteúdo americano.

Terceiro, **peça verificação cruzada em fatos críticos**. "Verifique este dado em pelo menos duas fontes independentes" força Claude a buscar confirmação.

Quarto, **explicite quando alguma fonte específica deve ser consultada**. "Consulte o site oficial da empresa para o número mais recente" direciona para a fonte de verdade quando você a conhece.

### 17.3.3 — Quando Web Search rende mais

Web Search faz diferença visível em cinco classes de pergunta:

**Dados em tempo real**: cotações, preços, indicadores econômicos, status de mercado. Sem Web Search, Claude inventa ou se recusa; com ele, retorna número atual com fonte.

**Eventos recentes** das últimas semanas ou meses: lançamentos de produto, mudanças regulatórias, notícias de mercado. O conhecimento de treino fica defasado; Web Search atualiza.

**Especificações de produto** para itens lançados ou atualizados recentemente: versões de software, configurações de planos, novos recursos.

**Verificações de fato**: confirmar afirmação específica com fonte ao vivo em vez de afirmar do treino.

**Pesquisas de fontes pontuais**: encontrar página específica que mencione algo, mais eficaz que busca tradicional.

### 17.3.4 — Quando não usar

Há classes de pergunta em que Web Search é desperdício ou pode até atrapalhar:

**Conceitos conhecidos do treino**: para temas estáveis (machine learning, contabilidade, gramática), o treino é suficiente; busca adiciona ruído sem ganho.

**Pesquisas profundas**: se precisa de análise multi-fonte com síntese estruturada, use Research em vez de Web Search. Web Search é pontual, Research é arquitetural.

**Análises sobre conteúdo já no contexto**: se você anexou documento e quer análise dele, busca externa pode confundir o modelo. Mantenha foco no material fornecido.

**Brainstorm criativo**: para gerar ideias e explorar possibilidades, você quer o conhecimento integrado do modelo, não fatos pontuais.

---

## 17.4 — VALIDAÇÃO DE FONTES, A DISCIPLINA QUE NINGUÉM ENSINA

Web Search retorna o que está disponível na web — e a web tem qualidade radicalmente variável. A triagem fina das fontes continua sendo responsabilidade humana.

> 📊 **Diagrama 17.2 — Hierarquia de Confiabilidade de Fontes**
>
> ![Hierarquia de fontes](imagens/cap-17-img-02-validacao-fontes.svg)
>
> *Web Search faz triagem básica. A curadoria fina continua sendo sua.*

**Tier 1** (confiabilidade altíssima): bancos centrais, órgãos reguladores oficiais, IBGE, Diário Oficial. Cite diretamente em material profissional.

**Tier 2** (confiabilidade alta): consultorias top-tier como McKinsey, BCG, Gartner; mídia consolidada como Financial Times, Valor Econômico, The Economist; papers peer-reviewed. Use com confiança, citando autor e veículo.

**Tier 3** (confiabilidade moderada): blogs corporativos oficiais, releases de empresas, mídia regional, sites técnicos especializados. Use, mas verifique antes de citar em material crítico — releases têm viés institucional, blogs têm precisão variável.

**Tier 4** (confiabilidade baixa): blogs pessoais sem expertise, fóruns como Reddit, redes sociais, conteúdo agregado sem autoria. Use apenas como indicador inicial. Nunca cite como fonte primária.

**Tier 5** (desconfiança ativa): sites com agenda política não declarada, conteúdo gerado por IA sem autoria, SEO spam. Descarte ou valide duramente contra fontes melhores antes de aceitar qualquer afirmação.

Quando Web Search retorna mistura de fontes, olhe os domínios antes de aceitar afirmação importante. Citação de bacen.gov.br é terreno sólido. De blog desconhecido, verifique antes.

---

## 17.5 — EXEMPLO MEMORÁVEL: O FATO QUE NÃO ERA FATO

Em fevereiro de 2026, um diretor de empresa brasileira de saúde preparava apresentação sobre tendências de IA no setor, com prazo de três dias. Pediu a Claude com Web Search ativo "qual o tamanho do mercado de IA aplicado à saúde no Brasil em 2025". A resposta veio com número específico e impressionante, citando uma "consultoria especializada".

Antes de incluir na apresentação para o board, resolveu validar a fonte. Clicou no link. O destino era um blog de empresa pequena, conteúdo otimizado para SEO, sem autoria identificada, número sem origem documentada. A "consultoria especializada" não existia como entidade formal — o número havia sido inventado por um redator e replicado por agregadores até virar "fato consensual".

A validação levou quinze minutos. Refez a pergunta pedindo explicitamente "use apenas fontes Tier 1, como IBGE, Anvisa, ABDI, ou consultorias top-tier reconhecidas, com nome próprio do autor da estimativa". A nova resposta veio com números bem mais conservadores, vindos de relatório da Gartner e estudo da ABDI, com referências verificáveis. Os números eram cerca de 40% menores que o "fato" anterior — mas eram verdade.

A apresentação foi feita com os dados validados. Na discussão, um executivo do board questionou exatamente esse número. Com a fonte sólida, a resposta foi tranquila e o argumento sustentou. Com o número anterior, teria sido pego em informação fabricada — com consequência direta para a credibilidade junto à diretoria.

**Web Search reduz risco de alucinação porque traz fontes, mas não elimina risco quando as fontes são ruins. A curadoria das fontes citadas continua sendo indispensável, especialmente em material que vai sair da organização ou subir em hierarquia decisória.** Quinze minutos validando podem salvar credibilidade construída em anos.

> 🎯 **PARA EXECUTIVOS**
> Em qualquer apresentação, relatório ou comunicação executiva onde números específicos são citados, **valide as fontes retornadas pelo Web Search antes de usar**. Especialmente para estatísticas de mercado, percentuais e projeções, que são as informações mais frequentemente fabricadas em conteúdo SEO. O custo de validar é minutos, o custo de não validar pode ser reputação.

### 17.5.1 — O padrão de falsa confiança específico do Web Search

Web Search tem um risco diferente do Research, mas igualmente silencioso. No Research, o perigo é o relatório denso com muitas fontes que parece completo. No Web Search, o perigo é mais simples e mais frequente: **a resposta com citação inline que parece verificada, mas cuja fonte você nunca abriu**.

Claude retorna afirmação com número preciso e um link. Você lê a afirmação. O link está lá. Você assume que o link suporta a afirmação. Você não clica.

A citação funciona como sinal visual de rigor, independentemente do que está na fonte. Em uso profissional, um número citado sem abertura da fonte é tão não-verificado quanto um número sem citação — a diferença é que parece verificado, o que é pior.

**A disciplina mínima para uso profissional:**

- Afirmação que vai sair da sua organização (deck, email, relatório, publicação) → **abra a fonte, leia o trecho, confirme**.
- Afirmação numérica específica (percentual, valor, data) → **verifique contra a fonte primária, não a secundária que Claude citou**.
- Afirmação que contradiz o que você sabia antes → **investigue a contradição, não aceite a versão nova só porque tem link**.
- Afirmação que confirma perfeitamente a sua tese → **trate com ceticismo redobrado**. Viés de confirmação tem link agora.

O Invariante 1 aplicado ao Web Search não é "não use Web Search". É: **o link não é a verificação. Abrir o link é a verificação.**


---

## 17.6 — NA PRÁTICA: TRÊS APLICAÇÕES REPLICÁVEIS

O exemplo anterior mostra o risco; esta seção entrega o roteiro para evitá-lo. Três aplicações que você pode rodar esta semana.

**Aplicação 1 — Verificação de número antes de apresentar.**
*Situação:* você está finalizando deck ou relatório com estatística de mercado de fonte secundária; a apresentação é para liderança ou cliente. *O que fazer:* ative Web Search com instrução explícita — "verifique este número em fonte primária como IBGE, Bacen, consultoria top-tier com nome do autor, ou paper peer-reviewed". Receba a resposta com citações inline. Abra cada link, leia o trecho, confirme que o que Claude diz que a fonte diz é o que a fonte realmente diz. *O ponto de julgamento:* a verificação que vale não é Claude retornar uma citação — é você abrir a fonte. Citação sem leitura é ilusão de verificação. O número que vai no slide tem sua assinatura, não a do modelo (Invariante 1 — Plausibilidade).

**Aplicação 2 — Atualização de contexto antes de reunião urgente.**
*Situação:* você tem reunião em duas horas com interlocutor que veio a público ontem com declaração relevante, ou cuja empresa anunciou mudança estratégica recente; você não teve tempo de acompanhar. *O que fazer:* ative Web Search com escopo temporal explícito — "notícias sobre [empresa/pessoa] dos últimos sete dias, com foco em [tema], priorizando fontes Tier 1 e Tier 2". Receba o sumário. Abra as duas ou três citações principais para confirmar os fatos que você vai usar na reunião. *O ponto de julgamento:* distinga âncora factual (verificado) de contexto de fundo (não cite como dado). "Li que a empresa anunciou X" é diferente de "a empresa anunciou X" — e essa diferença aparece quando o interlocutor pede a fonte (Invariante 1 — Plausibilidade).

**Aplicação 3 — Monitoramento pontual de mudança regulatória.**
*Situação:* você precisa saber se houve mudança em regulação relevante — normativa do BCB, resolução da CVM, instrução da Anvisa — sem fazer Research completo. *O que fazer:* ative Web Search com instrução de fonte Tier 1 exclusiva — "busque em sites oficiais como bacen.gov.br, cvm.gov.br ou anvisa.gov.br publicações sobre [tema] dos últimos 90 dias". Se Claude retornar resultado sem fonte Tier 1, peça refinamento. Se não houver resultado confiável, sinalize isso em vez de aceitar resposta vaga. *O ponto de julgamento:* em matéria regulatória, a única fonte que importa é o texto oficial no site do órgão. Resumo em blog pode estar desatualizado ou incorreto. Se a citação não apontar para o Diário Oficial ou site do regulador, a verificação não terminou — termine você (Invariante 1 — Plausibilidade; Invariante 8 — Responsabilidade Indelegável).

> 🔧 **EXERCÍCIO**
> Pegue um material profissional seu — deck, relatório, e-mail para cliente — que contenha pelo menos um número de mercado ou estatística. Identifique a fonte original desse número. Agora peça a Claude com Web Search que **verifique esse número em fonte Tier 1 ou Tier 2**, com link para a fonte. Abra o link e leia o trecho. O número é o mesmo? A fonte diz o que Claude disse que dizia? Documente o resultado. Esse exercício, feito uma vez com atenção, muda como você usa Web Search para sempre.

---

## 17.7 — CONEXÕES COM OUTROS CAPÍTULOS

- 🔗 **RAG e recuperação de informação** → [Capítulo 6](../../Livro-1-Os-Invariantes/02-capitulos/L1-C06-rag.md)
- 🔗 **Alucinação e validação** → [Capítulo 2](../../Livro-1-Os-Invariantes/02-capitulos/L1-C02-como-modelos-funcionam.md)
- 🔗 **Claude Research, busca profunda** → [Capítulo 16](L2-C16-research.md)
- 🔗 **Claude Code com web search integrado** → [Capítulo 9](L2-C09-claude-code.md)
- 🔗 **Segurança em uso de IA** → [Capítulo 37](../../Livro-1-Os-Invariantes/02-capitulos/L1-C19-seguranca.md)

---

## 17.8 — RESUMO EXECUTIVO

| Conceito | Síntese |
|----------|---------|
| **Web Search** | Busca pontual integrada ao chat, com citações inline |
| **Mecânica** | Query otimizada → resultados → leitura → síntese com citações |
| **Quando usar** | Dados em tempo real, eventos recentes, verificação de fato |
| **Quando evitar** | Conceitos do treino, pesquisa profunda, brainstorm criativo |
| **Hierarquia de fontes** | Tier 1 oficial, Tier 2 consultoria/mídia profissional, até Tier 5 spam |
| **Validação** | Triagem básica automática, mas curadoria fina continua humana |

---

## 17.9 — CHECKLIST DO CAPÍTULO

- [ ] Distinguir Web Search de Research e de chat normal
- [ ] Ativar Web Search seletivamente conforme tarefa
- [ ] Validar fontes antes de citar em material profissional
- [ ] Aplicar a hierarquia de cinco tiers de confiabilidade
- [ ] Especificar tipo de fonte e temporalidade na pergunta
- [ ] Reconhecer quando Web Search vira ruído em vez de ajuda

---

## 17.10 — PERGUNTAS DE REVISÃO

1. Por que Web Search é diferente de Research e quando cada um faz sentido?
2. Como você instrui Claude a priorizar fontes específicas?
3. Quais são os cinco tiers de confiabilidade e exemplos de cada?
4. Por que validar fontes manualmente continua sendo necessário?
5. Em que situação Web Search atrapalha em vez de ajudar?

---

## 17.11 — EXERCÍCIOS PRÁTICOS

### Exercício 1 — Comparação de modos
Faça a mesma pergunta sobre tendência recente em três modos diferentes (chat normal, Web Search, Research). Compare qualidade, profundidade e tempo.

### Exercício 2 — Validação rigorosa
Para uma resposta de Claude com Web Search, valide cada fonte citada manualmente. Documente quais eram Tier 1-2 e quais eram Tier 3-5.

### Exercício 3 — Calibração de fontes
Refaça uma busca pedindo explicitamente apenas Tier 1 e Tier 2. Compare o resultado com a busca aberta original.

### Exercício 4 — Auditoria de uso
Revise suas últimas cinco respostas de Claude com Web Search. Quantas você citou em material profissional sem validar fontes? Documente os riscos identificados.

---

## 17.12 — PROJETO DO CAPÍTULO

**Estabeleça política pessoal de validação de fontes.**

Para uso profissional de Web Search, escreva sua política de validação. Em quais tipos de pergunta você sempre valida? Em quais aceita sem verificar? Que tiers você considera aceitáveis para citação direta? Que tiers exigem validação adicional? Esse documento, mesmo pessoal, vira hábito que protege sua credibilidade em uso intensivo.

---

## 17.13 — REFERÊNCIAS PRINCIPAIS

📚 **Documentação**

- [Anthropic — Web search](https://www.anthropic.com/news/web-search)
- [Claude Docs](https://docs.claude.com/)

---

## 17.14 — VALIDAÇÃO UAU

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | **Clareza** — Explicar Web Search e quando usá-lo em 60 segundos | ☐ |
| 2 | **Profundidade** — Defender a hierarquia de cinco tiers de confiabilidade | ☐ |
| 3 | **Aplicação** — Aplicar validação de fontes em três usos reais nesta semana | ☐ |
| 4 | **Conexão** — Articular como Web Search conecta com RAG (Cap 6), Research (Cap 15), segurança (Cap 37) | ☐ |
| 5 | **Curiosidade UAU** — Está com vontade de entrar em Claude Code, o produto que vem mudando como software é construído | ☐ |

**5 de 5?** Avance. Você acabou de adicionar disciplina de validação ao seu uso de IA.
**3 ou 4?** Releia 16.5 (caso do diretor). É onde a disciplina vira salva-vidas reputacional.
**Menos de 3?** O capítulo merece releitura, especialmente se você usa Web Search em material profissional.

---

🔗 **Próximo capítulo:** [Capítulo 18 — Claude Voice](L2-C18-voice.md)

---

> *"Web Search tira Claude do isolamento do treino. Validar as fontes que ele retorna é o que tira você do risco de citar fato inventado."*
