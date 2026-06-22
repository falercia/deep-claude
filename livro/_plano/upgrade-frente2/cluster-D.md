# CHANGELOG — CLUSTER D: ECOSSISTEMA 3 / ENG
**Upgrade Editorial Frente 2 · Livro 2 "Deep Claude" · 2026-06-17**

---

## C19 — Claude Team (5/10 → alvo 7/10)

**P1 — Camada Viva:**
- Preço exato removido do corpo (seções 19.1, 19.3 e tabela 19.5) → substituído por ponteiro `[Apêndice Vivo (J)]` com instrução de consulta à página oficial.

**P2 — Decisão + Invariante:**
- Seção 19.3 reescrita com critério bidirecional: quando migrar (mantido) + **quando Team é prematuro** (equipes de 2-3 sem compartilhamento real) + **quando Team é insuficiente** (pulo direto para Enterprise em setores regulados).
- Invariante 8 operacionalizado: a responsabilidade dilui-se sem Team; com Team, cada Project e Skill tem dono identificável.

**P2 — Profundidade técnica:**
- Seção 19.2 expandida com modelo de papéis (Admin / Member / Guest) e suas permissões reais.
- Diferença SSO SAML Team vs SCIM Enterprise tornado explícito — limitação do Team descrita (offboarding manual obrigatório).

**P3 — Exercícios:**
- Substituídos 5 critérios declarativos por 3 exercícios acionáveis: mapear workspace, aplicar tabela de fronteira 19.5, calcular custo da fragmentação atual.

**P4 — Sobreposição Team/Enterprise:**
- Adicionada **Tabela de Fronteira Team vs Enterprise** (seção 19.5) com 16 capacidades comparadas. C19b parte desta tabela e não a repete.

---

## C19b — Claude Enterprise (6/10 → alvo 7.5/10)

**P1 — Camada Viva:**
- Certificações (SOC 2, ISO 27001) sinalizadas com `⚡` e ponteiro para Apêndice Vivo + página de trust da Anthropic.
- Referência a regulações (LGPD, GDPR, HIPAA) também com ponteiro — status regulatório evolui com decisões das autoridades.

**P2 — Decisão + Invariante:**
- Seção 19b.3 expandida com **quando Enterprise é excesso** — crítica a contratar Enterprise "por precaução" sem requisitos formais que justifiquem.
- Adicionada subseção sobre o processo de negociação Enterprise: NDA, reunião técnica, MSA+DPA, integração de SCIM, cronograma de 4-12 semanas.

**P2 — Profundidade técnica (Pilar 3):**
- Diferença SAML Team vs SCIM Enterprise tornado explícito com implicações práticas de offboarding.
- O que SCIM automatiza (criação/remoção via diretório de RH) descrito com casos concretos.
- O que DPA cobre além do ToS padrão explicado.

**P3 — Exercícios:**
- Substituídos 5 critérios declarativos por 3 exercícios acionáveis: mapear requisitos formais, simular as seis instâncias do banco, estimar cronograma de negociação.

**P4 — Sobreposição:**
- Adicionado aviso explícito no início: "Este capítulo parte da tabela de fronteira do Cap 19. Não repete o que Team cobre."
- Não há mais re-explicação de SSO do zero — o Pilar 3 aprofunda o que Team não tem (SCIM, offboarding automático, granularidade adicional), assumindo que leitor veio de C19.

---

## C20 — Connectors, Dispatch e Routines (6/10 → alvo 7.5/10)

**P1 — Camada Viva:**
- Lista hardcoded de Connectors removida do corpo (seção 20.2.1) → substituída por descrição de categorias + ponteiro `[Apêndice Vivo (J)]` + instrução de consultar documentação oficial.

**P2 — Decisão + Invariante:**
- Adicionada seção **20.2.4 — Quando NÃO ativar um Connector**: escopo OAuth, dados sensíveis, auditoria.
- Adicionada seção **20.3.3 — Quando NÃO usar Dispatch**: ações irreversíveis sem supervisão, custo acumulado sem monitoramento, falha silenciosa de webhook.
- Adicionada seção **20.4.4 — Quando Routines não valem o overhead**: fluxos únicos, instáveis ou pouco frequentes.
- Box 🧭 expandido: critério central explícito antes de ativar qualquer mecanismo ("você consegue ver o que está rodando, quanto está custando, e reverter se der errado?").

**P2 — Profundidade técnica:**
- Routines: adicionado exemplo mínimo de estrutura de pasta e conteúdo de routine.md com parâmetros e passos.
- Tabela 20.5 expandida com coluna "Critério de evitar".

**P3 — Exercícios:**
- Substituídos 5 critérios declarativos por 3 exercícios acionáveis: auditoria de Connectors ativos, mapeamento de trigger Dispatch com checklist de segurança, criação de primeira Routine mínima.

---

## C28 — Claude + MCP: Arquiteturas Corporativas (7/10 → alvo 8/10)

**P2 — Decisão + Invariante:**
- Adicionada seção **28.3 — Quando construir MCP corporativo — e quando não construir**: critérios bidirecional explícitos. Regra prática: "se o Connector resolve, use o Connector".
- Seção original 28.3 renomeada para 28.3b.

**P2 — Governança como método:**
- Seção 28.2 (camada de governança) expandida: cada elemento de governança (catálogo, permissões, logs, processo de revisão) descrito com critério de decisão operacional, não apenas listado.
- Logging de chamadas MCP detalhado: o que logar, por quê, como isso responde a auditoria de compliance.

**P3 — Exercícios:**
- Validação UAU declarativa substituída por 3 exercícios acionáveis: aplicar critério de construção a 5 sistemas internos, estimar ROI do sistema de maior valor, definir processo de governança mínimo antes do primeiro deploy.

---

## C30 — Claude Skills (8/10 → alvo 9/10)

**P2 — Decisão + ponto cego:**
- Adicionada seção **30.4 — Governança de Skills**, ancorada em Responsabilidade Indelegável (Inv. 8). Cobre: os três problemas silenciosos de Skills sem governança (acúmulo não curado, distribuição sem validação, descontinuação fantasma); ciclo mínimo de governança (5 passos: aprovação, dono identificado, revisão periódica, critério de descontinuação, teste antes de re-publicar); frontmatter mínimo de governança com campos owner, version, last-reviewed, status, approved-by.

**P3 — Exercícios:**
- Validação UAU declarativa substituída por 3 exercícios acionáveis: identificar candidatos, construir SKILL.md mínima, definir governança antes de compartilhar.

**Estrutura e blueprints:** integralmente preservados (seções 30.1–30.3 + 6 exemplos completos). Apenas nova seção 30.4 inserida antes do exemplo da consultoria (agora 30.5).

**P4 — Sinal para o leitor:**
- Adicionado parágrafo "Adapte, não copie" (seção 30.3.7) antes dos padrões comuns.

---

## C31 — Subagents e Workflows (6/10 → alvo 7.5/10)

**P2 — Governança prometida entregue:**
- Adicionada seção **31.6 — Governança de Subagents**: quatro pontos de falha típicos (custo invisível, falha silenciosa, erro destrutivo sem rollback, debug impossível sem tracing) com método de mitigação para cada um. Pré-flight check como tabela operacional de 5 critérios antes de qualquer deploy em produção.

**P2 — Padrões expandidos:**
- Padrão "hierarquia": adicionado limite prático (máx. 2 níveis antes de teste exaustivo).
- Padrão "debate": adicionado risco de loop de refinamento sem convergência + critério de resolução.

**P3 — Exercícios:**
- Validação UAU parcialmente declarativa substituída por 3 exercícios acionáveis: mapear fluxo candidato, identificar fluxos que NÃO se beneficiam (critério reverso), aplicar pré-flight check.

---

## RESOLUÇÃO DA SOBREPOSIÇÃO C19 ↔ C19b

**Solução implementada:**
1. C19 (Team) criou **Tabela de Fronteira** (seção 19.5) com 16 capacidades comparadas — única fonte de verdade para a divisão.
2. C19b (Enterprise) adicionou aviso explícito de entrada: "Este capítulo parte da tabela 19.5. Não repete o que Team cobre."
3. C19b removeu re-explicação de SSO do zero — o Pilar 3 agora aprofunda apenas o que Enterprise adiciona (SCIM, offboarding automático, granularidade de SAML), assumindo que leitor veio de C19.
4. C19b adicionou subseção de processo de negociação — informação high-value que C19 não tem e que impede o leitor corporativo de fechar a decisão sem dados práticos.

---

## O QUE AINDA PEDE REESCRITA PROFUNDA (P5)

### C19 — Team
- **Exemplo de configuração real** de SSO SAML no Team: ao menos um fluxo de configuração com campos reais (ACS URL, Entity ID, atributos esperados). O capítulo ganhou profundidade conceitual mas ainda não tem profundidade técnica de implementação.
- **Diagrama de permissões**: fluxo visual de como Admin/Member/Guest se relacionam com Projects compartilhados.

### C20 — Connectors, Dispatch e Routines
- **Exemplo memorável brasileiro** para pelo menos Connectors ou Dispatch. O capítulo continua sem âncora local — nenhum caso nomeado.
- **Configuração real de webhook Dispatch**: ao menos um exemplo de payload de entrada e saída para o caso de CRM + análise de retenção.

### C28 — Claude + MCP
- **Seção de primeiros passos**: como construir o primeiro servidor MCP interno — linguagem, framework, quanto tempo para um POC funcional. Hoje o leitor sabe por que construir mas não sabe por onde começar.
- **Stack de observabilidade**: qual ferramenta monitorar chamadas MCP em produção (OpenTelemetry, Datadog, CloudWatch, outro).

### C31 — Subagents
- **Exemplo de código real**: ao menos uma invocação de subagente em Claude Code com sintaxe real. O capítulo é o mais técnico do livro mas não tem uma linha de código.
- **Custo real do exemplo da proposta**: quanto custou computacionalmente as "duas semanas de refinamento"? Sem esse dado o ROI parece mágico.

---

*Changelog gerado em 2026-06-17. Autor das edições: Editor Executivo L2.*
