# Contrato de Uso e Contribuição

Este documento define os princípios de uso, contribuição e operação do repositório `deep-claude`.

---

## Para o leitor

### O que você pode fazer

Você pode clonar este repositório, forkar para uso interno da sua casa, customizar prompts, skills e templates ao seu contexto, integrar ao seu stack interno de IA. O licenciamento dual (MIT para código, CC-BY 4.0 para conteúdo) garante máxima liberdade.

### O que você deve fazer

Você deve atribuir a obra original quando reutilizar conteúdo textual em material público (artigos, posts, decks, vídeos). A atribuição é o que sustenta o modelo aberto deste repositório. Sem atribuição, o ecossistema editorial brasileiro de IA fica empobrecido.

### O que você não deve fazer

Você não deve aplicar artefatos deste repositório em produção sem entender os capítulos correspondentes do livro. Prompts setoriais respeitam contexto regulatório brasileiro (CFM, OAB, BACEN, LGPD); aplicar fora desse contexto ou sem entender o método gera resultado raso ou risco operacional. O livro é o mapa; o repositório é o atalho. Sem mapa, atalho vira armadilha.

---

## Para o contribuidor

### Princípios

**Sem autopromoção.** Contribuição é técnica, não marketing. Não aceitamos PRs que insiram autopromoção, link de venda ou material promocional em qualquer pasta.

**Fonte primária obrigatória.** Toda informação factual (preço, benchmark, janela de contexto, SLA, recurso de produto) precisa fonte primária linkada (doc oficial, blog launch, paper). Sem fonte primária, contribuição não é incorporada.

**Idioma.** Contribuições em português brasileiro. Nomes técnicos em inglês onde for padrão da indústria.

**Calibração por painel.** Para áreas reguladas (jurídico, saúde, finanças), contribuições passam por revisão de especialista do domínio antes de incorporação. Isso protege o leitor que vai aplicar em produção.

### Tipos de contribuição

| Tipo | Como contribuir |
|---|---|
| Erro factual | Abra issue com label `erro` e fonte primária correta |
| Errata em Apêndice Vivo | Issue com label `errata` (modelo, preço, benchmark) |
| Novo prompt setorial | PR com prompt completo + golden set + fonte regulatória |
| Novo skill | PR com skill em SKILL.md + exemplo de uso |
| Novo lab | PR com lab executável + dataset + script de validação |
| Tradução ou clareza textual | PR direto |
| Sugestão estrutural | Issue com label `discussão` |

### Fluxo

1. Abra issue antes de PR substancial (alinhamento prévio evita retrabalho)
2. Aguarde resposta do mantenedor (até 7 dias)
3. Abra PR contra branch `main`, com descrição clara da mudança
4. PR passa por revisão; ajustes pedidos via comentários
5. Após merge, contribuição entra no changelog datado com atribuição

### Atribuição

Contribuidores aprovados são listados no CONTRIBUTORS.md (a criar conforme repositório evolui), com nome, GitHub handle e tipo de contribuição. Atribuição é opcional; quem prefere anonimato pode pedir.

---

## Para o operador em produção

### O que você deve revisar antes de aplicar

**Para prompts setoriais.** Antes de aplicar em produção, revise a constituição do prompt (regras XML) e adapte ao seu contexto regulatório específico. Prompts são calibrados para padrões brasileiros gerais; sua casa tem nuances que só você conhece.

**Para skills.** Antes de instalar skill, leia o `SKILL.md` para entender quando o trigger ativa. Skills mal calibrados ativam em momentos errados e poluem a operação.

**Para MCPs.** Antes de conectar MCP a stack de produção, valide credenciais, escopos e autorização. MCPs com acesso amplo viram superfície de ataque.

**Para templates de governança.** Antes de adotar template como política da casa, passe por jurídico interno. Templates são ponto de partida, não documento final assinado.

### Limites de responsabilidade

Este repositório é fornecido "como está", sem garantias. Você é responsável pela aplicação no seu contexto. Em setores regulados (saúde, jurídico, financeiro), aplicação inadequada pode gerar multa, exposição reputacional ou risco operacional. Leia os capítulos correspondentes do livro, valide com especialista do seu domínio, e teste em sandbox antes de produção.

---

## Princípio raiz

Este repositório existe para acelerar a transformação do leitor em profissional Claude capaz e responsável. Tudo o mais é instrumento desse fim.

---

*Última revisão: 2026-06-06*
