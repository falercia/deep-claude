# AUDITORIA — CLUSTER D: ECOSSISTEMA 3 / ENG
**Banca Editorial Adversarial · Livro 2 "Deep Claude" · 2026-06-17**

---

## C19 — Claude Team

Nota: 5/10 · Veredito: Funcional mas raso · "Manual de botão"? MÉDIO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅ — Inv. 8 (Responsabilidade Indelegável) declarado explicitamente no box 🧭. Justificativa coerente: Team cria dono identificável por Project e Skill. Funciona.

2. **Conceito intuitivo + analogia (Teste da Joana)** ✅ — Seção 19.1 usa o cenário do "caos de Pro descentralizado" (15 pessoas, reembolsos, nenhuma visibilidade). Joana entende. Mas a analogia termina aí; não há imagem mental concreta para *workspace compartilhado* nem para o salto qualitativo de "ferramenta individual → plataforma organizacional" prometido no epígrafe.

3. **Quando usar / quando EVITAR** ⚠️ — Seção 19.3 dá a regra dos "5 usuários regulares" e lista sinais de migração. Bom. Problema: *nenhum cenário de quando NÃO migrar ou quando Pro ainda é suficiente*. Falta critério de evitar. Ex: equipe de 2 freelancers que nunca compartilham Projects? Empresa com dados ultra-sensíveis sem avaliação de Enterprise primeiro? Ausência é falha nº1.

4. **Profundidade técnica real** ❌ — Mais fraco para capítulo de ecossistema. "Projects compartilhados são a alavanca de produtividade coletiva mais importante" (seção 19.2) é afirmação, não demonstração. A anatomia lista recursos mas não explica como funciona o compartilhamento de permissões, nem diferença entre Admin, Member e Guest no workspace. SSO via SAML mencionado sem qualquer detalhe sobre configuração ou limitações no plano Team. Não há diagrama de fluxo de acesso.

5. **Exemplo memorável brasileiro, rotulado** ✅ — Agência de marketing digital, 45 funcionários, 30 clientes. Três métricas concretas (onboarding 3 semanas → 4 dias; qualidade mais consistente; custo −15%). Memorável e específico.

6. **Camada Viva — perecível no corpo vs Apêndice Vivo** ❌ — Falha nº2 direta e grave. Seção 19.2 cita **preço exato "~US$ 30/usuário/mês em 2026"** e mínimo de 5 usuários no corpo do texto e na tabela resumo (19.5). Informação perecível enterrada no corpo sem nenhum sinalizador de volatilidade. Preços Anthropic mudam a cada ciclo; o livro vai parecer desatualizado em meses. Deve ir para Apêndice Vivo.

7. **Exercícios + autoavaliação + conexões** ⚠️ — Validação UAU (19.6) existe mas é genérica demais: critérios 1–5 são todos declarativos ("consegue explicar?"), nenhum é prático ("faça X e avalie o resultado"). Conexões em 19.5 são links crus; faltam frases de ponte explicando *por que* conectar com aquele capítulo.

### 5 testes

- **Joana**: Passa parcialmente — entende "o que é" mas não "como funciona por dentro".
- **Durabilidade**: Reprovado — preços e limites numéricos no corpo tornam o capítulo perecível.
- **Diferenciação**: Fraco — não distingue com clareza o que Team oferece que Pro não oferece via workaround.
- **Memorização**: Passa — o exemplo da agência é retido facilmente.
- **Transformação**: Fraco — leitor termina sabendo que deve migrar mas não sabe como ou o que mudar na prática da equipe.

### Top lacunas (priorizadas, com seção)

1. **Seção 19.2 / 19.5** — Preços e limites numéricos no corpo → mover para Apêndice Vivo.
2. **Seção 19.3** — Ausente: critério de quando NÃO migrar / quando Team é prematuro.
3. **Seção 19.2** — Anatomia sem profundidade: falta modelo de permissões (Admin/Member/Guest), onboarding via SSO SAML no Team (vs Enterprise), limitações do compartilhamento de Projects.
4. **Seção 19.1** — Analogia não fecha: "plataforma organizacional" precisa de imagem concreta além da lista de recursos.
5. **Seção 19.6** — Exercícios declarativos; incluir pelo menos 1 exercício prático (ex: "desenhe o workspace para 10 pessoas em 3 departamentos").

### Maior força a preservar

O exemplo da agência com as três métricas concretas (19.4) é o melhor trecho do capítulo. Real, específico, brasileiro, aponta transformação qualitativa. Preservar integralmente.

---

## C19b — Claude Enterprise

Nota: 6/10 · Veredito: Sólido em governança, raso em profundidade técnica · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅ — Inv. 8 + Inv. 6 declarados com justificativa clara. Box 🧭 explica bem por que Enterprise operacionaliza indelegabilidade em escala. Dois invariantes, ambos pertinentes.

2. **Conceito intuitivo + analogia (Teste da Joana)** ✅ — Seção 19b.1 lista setores regulados (bancos, saúde, governo) com requisitos nomeados (LGPD, GDPR, HIPAA). Joana do setor regulado entende imediatamente por que Enterprise é pré-requisito, não upgrade.

3. **Quando usar / quando EVITAR** ✅ — Seção 19b.3 é o melhor critério de decisão entre os 6 capítulos auditados. Regra clara (200–500 usuários podem ficar no Team; acima ou com requisitos regulatórios, Enterprise), indicadores concretos (DPA, SAML, VPC, certificações). Ainda falta critério de quando Enterprise é excesso (pequena empresa que acha que precisa por status).

4. **Profundidade técnica real** ⚠️ — Cinco Pilares (19b.2) são descritos em nível razoável. Mas faltam: diferença entre SSO no Team vs SCIM automático no Enterprise; o que VPC isolado via Bedrock implica para o cliente (custo, setup, isolamento real); como funciona "data residency" na prática; o que DPA cobre contratualmente que ToS padrão não cobre. Para decisão de TI corporativa, a profundidade está aquém.

5. **Exemplo memorável brasileiro, rotulado** ✅ — Banco brasileiro, 12 mil funcionários, 8 meses de ciclo de aprovação. Narrativa cronológica das 6 instâncias (SI, Compliance, Auditoria, Jurídico, Identidade, Risco) é o melhor exemplo factual do cluster por mostrar o *processo real*, não só o resultado.

6. **Camada Viva** ⚠️ — "Preço sob consulta, contratos anuais customizados" na tabela está OK (sem número específico). Mas a referência a certificações específicas (SOC 2 Type II, ISO 27001) no corpo merece sinalizador de volatilidade ou link para página de trust da Anthropic no Apêndice Vivo.

7. **Exercícios + autoavaliação + conexões** ⚠️ — Mesmo problema do C19: Validação UAU declarativa, sem exercício prático. Critério 2 ("defender quais requisitos exigem Enterprise") é o melhor mas ainda é verbal, não experiencial.

### 5 testes

- **Joana**: Passa bem — setor regulado entende imediatamente.
- **Durabilidade**: Passa parcialmente — sem preços numéricos; certificações devem ir para Apêndice Vivo.
- **Diferenciação**: Forte — os 5 pilares são genuinamente distintos de Team.
- **Memorização**: Forte — o banco com 8 meses de aprovação fica gravado.
- **Transformação**: Médio — leitor sabe que precisa de Enterprise mas não sabe como iniciar o processo de contratação.

### Top lacunas (priorizadas, com seção)

1. **Seção 19b.2** — Adicionar profundidade técnica: diferença SAML Team vs SCIM Enterprise; o que VPC/Bedrock implica operacionalmente; o que DPA cobre além do ToS.
2. **Seção 19b.2 (certificações)** → sinalizador de volatilidade ou link para Apêndice Vivo.
3. **Seção 19b.3** — Adicionar: quando Enterprise é excesso e Team basta mesmo com 500+ usuários.
4. **Seção 19b.6** — Incluir exercício prático: "mapeie os requisitos da sua organização contra os 5 pilares".
5. **Ausente** — Falta seção sobre *como iniciar a negociação com Anthropic* (sales motion, NDA antes de conversa técnica, timeline típico) — informação high-value para o leitor corporativo.

### Maior força a preservar

A narrativa das 6 instâncias do banco (19b.4) com nomes explícitos de cada área e o que cada uma exigiu. É o coração do capítulo e a sua razão de ser distinto de Team.

---

## NOTA ESPECIAL: Sobreposição C19 ↔ C19b (Team vs Enterprise)

**Sobreposição existe mas é gerenciável. Não é redundância fatal.**

Ambos os capítulos: (a) declaram Inv. 8 como invariante, (b) descrevem SSO/SAML, (c) mencionam dados não usados para treinamento, (d) citam compliance como razão de escolha, (e) têm tabela resumo com estrutura idêntica.

O problema real não é sobreposição de conteúdo mas **ausência de handoff limpo**. C19 deveria dizer explicitamente: "SSO SAML aqui é básico — se precisar de SCIM, VPC, data residency ou DPA, é Enterprise". C19b deveria assumir que leitor veio de C19 e não reiterar o que Team oferece, apenas o que Enterprise *adiciona*. Hoje C19b reexplica SSO do zero como se C19 não existisse.

Recomendação: C19 termina com tabela de fronteira clara Team vs Enterprise; C19b começa assumindo essa tabela como lida. Curador deve revisar os dois capítulos em paralelo, não em sessões separadas.

**Risco de publicação se não corrigido:** leitor que lê C19 pode achar que já entendeu Enterprise suficientemente e não ir a C19b. Ou leitor que só leu C19b vai se perguntar por que existe C19 separado.

---

## C20 — Connectors, Dispatch e Routines

Nota: 6/10 · Veredito: Bom catálogo, critério de evitar ausente, Camada Viva comprometida · "Manual de botão"? MÉDIO-ALTO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅ — Inv. 6 e 5 declarados. Justificativa relevante: automação por trigger exige observabilidade proporcional (Inv. 6) e custo composto dispara sem controle (Inv. 5). Box 🧭 curto mas pertinente.

2. **Conceito intuitivo + analogia (Teste da Joana)** ✅ — Seção 20.1 usa o framework "fricção que cada mecanismo remove" (setup → Connectors; início → Dispatch; repetição → Routines). Tabela 20.5 cristaliza bem. Joana executiva entende Connectors e Dispatch. Routines é mais técnico — Joana não-desenvolvedora pode se perder.

3. **Quando usar / quando EVITAR** ❌ — Falha crítica e sistemática. Para Connectors: cuidados mencionados (20.2.4) mas não há critério de quando *não* ativar (dados sensíveis, auditoria, escopo de acesso excessivo). Para Dispatch: nenhuma menção de quando cria risco (webhook dispara sem supervisão humana, erros silenciosos, custo acumulado). Para Routines: sem critério de quando Routine não vale o overhead de manutenção. O capítulo trata os três mecanismos como ferramentas quase sempre benéficas. "Manual de botão" no sentido mais direto: ensina como ligar sem ensinar quando *não ligar*.

4. **Profundidade técnica real** ⚠️ — Connectors: OK para executivo mas vago para técnico (o que exatamente OAuth autoriza? qual escopo mínimo de permissão?). Dispatch: a seção 20.3 descreve formas sem mostrar uma configuração sequer — como se configura um webhook para Dispatch? Qual o formato de payload? Routines: seção 20.4.3 descreve estrutura de pasta mas não mostra um SKILL.md real nem exemplo de invocação com parâmetros.

5. **Exemplo memorável brasileiro, rotulado** ❌ — Ausente. Nenhum dos três mecanismos tem exemplo brasileiro nomeado. Os casos de uso são genéricos ("empresa que usa Slack intensivamente", "CRM detecta cliente em risco"). Para capítulo sobre ferramentas práticas, a ausência de exemplo concreto localizado é lacuna séria.

6. **Camada Viva** ❌ — Falha nº2 grave. Seção 20.2.1 lista Connectors disponíveis "em 2026" com nomes específicos hardcoded no corpo (Google Workspace, Microsoft 365, Slack, Notion, GitHub, Salesforce, Stripe, etc.) sem sinalização de volatilidade. Connectors adicionados/removidos pela Anthropic não têm ciclo previsível. Esta lista deve ir para Apêndice Vivo com URL canônica da documentação oficial.

7. **Exercícios + autoavaliação + conexões** ⚠️ — Validação UAU (20.8) existe. Critério 3 ("liste 3 Routines que sua equipe deveria ter") é o mais prático dos 6 capítulos. Conexões completas. Falta exercício para Connectors e Dispatch.

### 5 testes

- **Joana**: Passa para Connectors; falha parcialmente em Dispatch (configuração); falha em Routines (só para desenvolvedor).
- **Durabilidade**: Reprovado — lista de Connectors por nome no corpo.
- **Diferenciação**: Médio — diferença Connector vs MCP explicada mas critério de escolha é quase sempre "use Connector"; nuances de quando MCP é melhor são subdesenvolvidas.
- **Memorização**: Fraco — sem exemplo brasileiro nomeado, nada ancora o conteúdo.
- **Transformação**: Médio — leitor sabe que existe Dispatch mas não sabe como configurar o primeiro webhook.

### Top lacunas (priorizadas, com seção)

1. **Seção 20.2.1** — Lista de Connectors → Apêndice Vivo com link para documentação oficial.
2. **Seções 20.2 / 20.3 / 20.4** — Ausente: critério de quando NÃO usar cada mecanismo (risco Dispatch, escopo excessivo Connector, overhead de manutenção Routines).
3. **Todo o capítulo** — Ausente: exemplo memorável brasileiro para pelo menos um dos três mecanismos.
4. **Seção 20.3** — Dispatch precisa de ao menos um exemplo concreto de configuração (formato de webhook, payload esperado, canal de retorno).
5. **Seção 20.4** — Routines: mostrar SKILL.md real mínimo com parâmetros e exemplo de invocação.

### Maior força a preservar

A tabela de fricção removida (seção 20.5) e o conceito de "patamar qualitativamente diferente" para quem combina os cinco mecanismos. É a síntese certa para o capítulo.

---

## C28 — Claude + MCP: Arquiteturas Corporativas

Nota: 7/10 · Veredito: O mais sólido tecnicamente do cluster, mas governança fica como lista, não método · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅ — Inv. 6 (Autonomia Proporcional) e Inv. 4 (Encaixe) declarados. A metáfora do porto com dono, autoridade e auditoria é a melhor ancoragem metafórica do cluster. Funciona genuinamente.

2. **Conceito intuitivo + analogia (Teste da Joana)** ✅ — Seção 28.1 usa a divisão em três classes de sistemas (SaaS externo, MCP interno, filesystem local) como mapa mental. Claro para executivo técnico. Joana CTO entende. Joana CFO pode travar em "SaaS externos com servidores MCP oficiais" sem ajuda adicional.

3. **Quando usar / quando EVITAR** ⚠️ — Seção 28.2 descreve bem as três camadas mas não tem critério de quando *não* construir MCP interno (quando Connector já basta, quando sistema legado é simples demais para justificar servidor dedicado, quando ROI não fecha). Seção 28.3 apresenta três casos reais sem mencionar casos em que a arquitetura corporativa falhou ou custou mais que o planejado. Assimetria de sucesso.

4. **Profundidade técnica real** ✅ — Melhor capítulo em profundidade proporcional à sua categoria. A descrição da camada de governança (catálogo aprovado, permissões granulares, logs, processo de revisão) é genuína, não decorativa. O exemplo do varejo com 14 sistemas legados tem número de investimento (R$ 1,2 milhão), prazo (8 meses), e resultado em duas métricas claras. Para arquiteto corporativo, é acionável. Faltam ainda: como se faz log de auditoria de chamadas MCP na prática, qual stack de observabilidade é recomendada.

5. **Exemplo memorável brasileiro, rotulado** ✅ — Rede de varejo, 200 lojas, R$ 4 bilhões de faturamento, 14 sistemas legados, 25 anos de operação. Métricas antes/depois (2–4 dias → 5–15 minutos para pergunta executiva). Memorável, específico, brasileiro.

6. **Camada Viva** ✅ — Sem números de preço ou listas de produtos voláteis no corpo. A referência a "AWS Bedrock para VPC isolado" é tecnicamente estável. Único risco menor: nomes de servidores MCP oficiais de terceiros não são listados em detalhe (ponto positivo por omissão).

7. **Exercícios + autoavaliação + conexões** ✅ — Validação UAU inclui critério 3 prático ("identifique três sistemas da sua empresa para construir MCP") que força aplicação real. Conexões com AI Engineering e Segurança relevantes. Falta: exercício de estimativa de ROI, dado que o argumento central do capítulo é ROI durável.

### 5 testes

- **Joana**: Passa bem para CTO/arquiteto; parcialmente para CFO.
- **Durabilidade**: Passa — sem dependência de preços ou listas voláteis no corpo.
- **Diferenciação**: Forte — "camada MCP como ativo que rende para qualquer ferramenta de IA futura" é genuinamente diferenciado.
- **Memorização**: Forte — o varejo com 14 sistemas e R$ 1,2 milhão ficam.
- **Transformação**: Médio — leitor entende o padrão mas não sabe por onde começar o primeiro servidor MCP interno.

### Top lacunas (priorizadas, com seção)

1. **Seção 28.3** — Adicionar: quando NÃO construir MCP corporativo (quando Connector já basta, ROI negativo para sistemas simples).
2. **Seção 28.2 (governança)** — Aprofundar: como fazer log de auditoria de chamadas MCP, stack de observabilidade recomendada, processo de revisão de segurança antes de produção.
3. **Ausente** — Falta seção de "primeiros passos": como construir o primeiro servidor MCP interno, qual ferramenta usar, quanto tempo leva para POC.
4. **Seção 28.4** — Adicionar estimativa de custo de oportunidade de não fazer (complementa o ROI positivo e cria assimetria honesta).
5. **Seção 28.2** — Camada de filesystem local mencionada mas não desenvolvida: riscos de acesso local em contexto corporativo?

### Maior força a preservar

O framing "camada MCP como ativo durável que rende para qualquer ferramenta de IA futura" (seção 28.4, parágrafo final). É o argumento de maior valor estratégico do capítulo e deve ser amplificado, não reduzido.

---

## C30 — Claude Skills

Nota: 8/10 · Veredito: O capítulo mais maduro do cluster, estrutura exemplar, governança de Skills ausente · "Manual de botão"? BAIXO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅ — Inv. 3 (Camada Dupla) + Inv. 9 (Operador) declarados. A frase "padrão durável capturado em forma reaplicável e versionada" é a instanciação mais precisa de Camada Dupla em todo o cluster. Funciona.

2. **Conceito intuitivo + analogia (Teste da Joana)** ✅ — Seção 30.1 usa a analogia "sênior mais experiente do grupo ensinando a melhor forma de fazer, sempre disponível". Joana entende imediatamente. A frase "quem só prompta refaz tudo a cada turno" cria contraste memorável.

3. **Quando usar / quando EVITAR** ⚠️ — Seção 30.1 dá critério de uso razoável ("fluxo mais de uma vez por mês, com estrutura razoavelmente estável"). Mas falta explicitamente: quando Skills são excesso (fluxo único, contexto muda demais, manutenção custa mais que ganho), quando Skill mal-construída é pior que prompt solto (promessas de qualidade não entregues criam falsa segurança), e como detectar uma Skill que envelheceu e precisa ser descontinuada.

4. **Profundidade técnica real** ✅ — Seção 30.2 (anatomia) + 30.3 (seis exemplos completos com estrutura de pasta, SKILL.md essencial, e caso de uso real) é o conteúdo mais acionável do livro inteiro. O leitor pode construir sua primeira Skill baseado apenas neste capítulo. Profundidade proporcional à relevância do tópico.

5. **Exemplo memorável brasileiro, rotulado** ✅ — Consultoria de M&A, 20 consultores, 12 Skills em 4 meses, 200 horas de investimento. Métricas: due diligence preliminar 18h → 6h; onboarding 8 semanas → 3 semanas; 5 novos deals sem contratação. Forte. Único risco: o capítulo já tem seis exemplos extensos nas subseções + o exemplo da consultoria. Pode haver fadiga de exemplo.

6. **Camada Viva** ✅ — Sem preços, sem listas de integrações voláteis. O formato de SKILL.md é estável (Anthropic define a convenção). Único cuidado menor: "carregamento sob demanda, quando Claude reconhece relevância" na tabela 30.5 pode ficar desatualizado se o mecanismo de descoberta mudar.

7. **Exercícios + autoavaliação + conexões** ✅ — Validação UAU critério 3 ("identifique três Skills que sua organização deveria construir") é excelente gatilho de aplicação. Conexões adequadas. Falta: exercício de *criação* real de uma SKILL.md mínima, não só identificação.

### 5 testes

- **Joana**: Passa bem — analogia do sênior + seis exemplos por área garantem que Joana de qualquer função veja aplicação para si.
- **Durabilidade**: Passa — sem dependências voláteis no corpo.
- **Diferenciação**: Forte — Skills vs "prompts soltos" é distinção clara que o leitor retém.
- **Memorização**: Forte — a consultoria de M&A e a frase "industrializar expertise" ficam.
- **Transformação**: Forte — este é o capítulo com maior potencial transformador do cluster. Leitor sai com blueprint acionável.

### Top lacunas (priorizadas, com seção)

1. **Ausente** — Governança de Skills completamente ausente: quem aprova uma Skill antes de ir para workspace compartilhado? Como se descontinua uma Skill obsoleta? Como se testa antes de distribuir? Para livro que aplica Inv. 8 (Responsabilidade Indelegável), Skills sem governança é ponto cego sério.
2. **Seção 30.1 / ausente** — Falta critério de quando Skills são excesso e quando Skill mal-feita é pior que prompt solto.
3. **Seção 30.6** — Exercícios: incluir criação real de SKILL.md mínima (não só identificação de candidatos).
4. **Seção 30.4** — Exemplo da consultoria forte, mas poderia incluir o custo de manutenção das 12 Skills (quem são os curadores, quanto tempo gastam) para equilibrar o argumento de ROI.
5. **Seção 30.3** — Seis exemplos completos é generoso; risco de o leitor usar como receita sem adaptar. Incluir parágrafo "adapte, não copie" em 30.3.7.

### Maior força a preservar

As seis estruturas completas de SKILL.md (30.3.1 a 30.3.6). São o núcleo prático do capítulo e diferencial de valor real para o leitor.

---

## C31 — Subagents e Workflows

Nota: 6/10 · Veredito: Arquitetura bem explicada, governança prometida e não entregue, exemplo forte · "Manual de botão"? MÉDIO

### Os 7 elementos

1. **Abertura ancorada num Invariante** ✅ — Inv. 6 (Autonomia Proporcional) declarado com a frase-chave: "sem tracing e sem rollback, sub-rotina vira loop opaco com custo composto crescente". Essa frase é a melhor articulação de governança em todo o cluster. Porém, o capítulo não honra essa promessa no corpo — a governança fica exclusivamente no box de abertura.

2. **Conceito intuitivo + analogia (Teste da Joana)** ✅ — Seção 31.1 usa a analogia do "gerente de projeto coordenando especialistas em vez de tentar fazer tudo sozinho". Joana entende. A distinção "contexto inflado prejudica atenção" como motivação técnica para dividir é genuinamente instrutiva.

3. **Quando usar / quando EVITAR** ✅ — Seção 31.3 é a mais balanceada entre todos os 6 capítulos neste critério. Rende/Atrapalha explícito, com casos concretos para cada polo. "Atrapalha quando a coordenação custa mais que a especialização rende" é critério real. Ponto positivo claro.

4. **Profundidade técnica real** ⚠️ — A arquitetura está bem descrita (31.2) e os padrões de orquestração (31.5) cobrem pipeline, paralelismo, debate, hierarquia. Mas faltam completamente: como se configura um subagente no Claude Code (qual a sintaxe real de invocação?), como se monitora custo de uma cadeia multi-agente antes que estoure o budget, como se faz tracing para debug quando subagente retorna resultado inesperado, qual é o limite de profundidade de hierarquia recomendado. Para o capítulo mais avançado do livro, a ausência de uma linha de código ou configuração real é limitação séria.

5. **Exemplo memorável brasileiro, rotulado** ✅ — Agência de consultoria estratégica, 30 consultores, proposta de 8 páginas em 25 minutos. Arquitetura dos 4 subagentes descrita com nomes (Pesquisador, Analista, Redator, Revisor), modelos usados (Opus, Sonnet), e resultado (16h → 2h humanas, vazão quintuplicou). Forte e memorável.

6. **Camada Viva** ✅ — Sem preços ou listas de APIs no corpo. "Opus para profundidade, Sonnet para o comum, Haiku para o simples" pode ficar desatualizado com modelos novos, mas é princípio de categorização, não dado de produto, então tem durabilidade razoável.

7. **Exercícios + autoavaliação + conexões** ⚠️ — Validação UAU critério 2 ("defender quando dividir em subagentes vale o overhead") é bom. Mas critério 3 ("identifique três fluxos que se beneficiariam") deveria vir acompanhado de critério reverso ("identifique três fluxos que *não* se beneficiariam"). Conexões adequadas.

### 5 testes

- **Joana**: Passa para Joana diretora que quer entender o padrão; falha para Joana engenheira que quer implementar.
- **Durabilidade**: Passa — sem dependências de produto voláteis.
- **Diferenciação**: Médio — o "quando não usar" da seção 31.3 diferencia do tratamento usual de Subagents, mas poderia ir mais longe.
- **Memorização**: Forte — os 4 subagentes da proposta com nomes e tempos ficam.
- **Transformação**: Fraco — leitor entende o padrão mas não consegue implementar sem documentação adicional.

### Top lacunas (priorizadas, com seção)

1. **Todo o capítulo** — A promessa da abertura ("sem tracing e sem rollback, loop opaco") não é cumprida no corpo. Falta seção de governança real: como monitorar custo, como fazer tracing, como definir timeout e fallback, como reverter se subagente comete erro com ferramenta destrutiva.
2. **Seção 31.2 / 31.5** — Ausente: qualquer exemplo de código ou configuração. Ao menos uma invocação de subagente em Claude Code deve aparecer para honrar "profundidade técnica".
3. **Seção 31.4** — O exemplo é forte mas incompleto: quanto custou computacionalmente? Qual foi o custo de falhas durante as "duas semanas de refinamento"? Sem esses dados, o ROI parece mágico.
4. **Seção 31.3** — "Atrapalha em tarefas simples" é vago. Incluir critério mais preciso (ex: tarefas abaixo de N passos sequenciais ou com contexto total abaixo de X tokens não justificam subagentes).
5. **Seção 31.5 (padrões)** — Padrão "Debate" (adversarial) mencionado em uma frase. Merece parágrafo: quando usar, como orquestrar, riscos de loops.

### Maior força a preservar

A seção 31.3 (quando usar / quando evitar) e a arquitetura detalhada do exemplo da proposta (31.4) com nomes dos subagentes e modelos usados. São os dois melhores trechos.

---

## LINHAS-TRACKER

```
CODIGO|NOTA|MANUAL_BOTAO|LACUNA_PRINCIPAL
C19|5|MÉDIO|Preços no corpo (Camada Viva falha); sem critério de quando não migrar para Team
C19b|6|BAIXO|Profundidade técnica insuficiente (SCIM vs SAML, VPC); certificações → Apêndice Vivo
C20|6|MÉDIO-ALTO|Lista de Connectors hardcoded no corpo (Camada Viva falha); sem critério de evitar para nenhum dos três mecanismos; sem exemplo brasileiro
C28|7|BAIXO|Sem critério de quando não construir MCP corporativo; governança como lista não como método; sem seção de primeiros passos
C30|8|BAIXO|Governança de Skills ausente (aprovação, descontinuação, teste antes de distribuição ao workspace)
C31|6|MÉDIO|Promessa de governança na abertura (tracing, rollback) não cumprida no corpo; sem código ou configuração real de subagente
```

**SOBREPOSIÇÃO C19 ↔ C19b:** Real em SSO/SAML/compliance. Solução: C19 deve criar tabela de fronteira clara (o que Team não faz que Enterprise faz); C19b deve assumir essa tabela como lida e não re-explicar Team. Curador deve revisar os dois capítulos em paralelo, não em sessões separadas.
