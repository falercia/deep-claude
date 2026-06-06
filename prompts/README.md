# Prompts Setoriais

> Biblioteca de prompts profissionais executáveis para Claude, organizada por setor.
> Calibrados para o contexto regulatório brasileiro.

---

## Por que esta pasta existe

A obra *Deep Claude*, na Parte 4 (Caps 36-40), apresenta casos por setor com prompts de exemplo. Esta pasta carrega versões executáveis desses prompts em qualidade de produção, com constituição completa, golden set de exemplos, instruções de adaptação e referência regulatória.

Prompts aqui são ponto de partida calibrado, não documento final. Adapte ao seu contexto antes de aplicar em produção.

---

## Ponte com `inteligencia-aumentada-recursos`

O repositório-irmão [`inteligencia-aumentada-recursos`](https://github.com/falercia/inteligencia-aumentada-recursos) carrega 30 prompts profissionais em qualidade plena, em XML versionado, com golden set, prefill, self-critique e changelog datado.

**Esta pasta complementa, não duplica.** O que vive aqui:

- Prompts **específicos do ecossistema Claude** (exploram extended thinking, tool use Anthropic-style, system prompts Claude-otimizados)
- Variantes setoriais com **calibração brasileira reforçada**
- Prompts ligados a casos do livro que não estão no L1

Para prompts genéricos multi-modelo, vá ao repositório-irmão. Para Claude-específicos, fique aqui.

---

## Estrutura por prompt

Cada prompt segue a estrutura:

```
prompts/P-XXX-NN/
  README.md         — propósito, quando usar, quando evitar, referência regulatória
  prompt.xml        — XML completo (system + role + constraints + examples)
  golden_set.yaml   — 10-20 casos representativos com output esperado
  changelog.md      — versões e mudanças por data
```

---

## Cobertura inicial — v1.0 (jul/2026)

5 prompts seed, um por área crítica coberta na Parte 4 do livro:

| Setor | Prompt seed | Capítulo |
|---|---|---|
| Jurídico | `P-LEG-CLAUDE-01` — análise de contrato com extended thinking | Cap 36 |
| Saúde | `P-MED-CLAUDE-01` — anamnese estruturada respeitando CFM | Cap 37 |
| Finanças | `P-FIN-CLAUDE-01` — análise de crédito com soberania de dados | Cap 38 |
| SaaS | `P-SAAS-CLAUDE-01` — suporte tier 1 com escalonamento | Cap 39 |
| RH | `P-RH-CLAUDE-01` — triagem de currículo com mitigação de viés | Cap 40 |

---

## Cobertura roadmap

### v1.1 — out/2026
- Cobertura completa dos Caps 36-40 (todos os prompts citados nos capítulos como variantes Claude-otimizadas)

### v1.2 — jan/2027
- Variantes regionais (por estado para casos jurídicos), por porte de empresa, por setor regulado adicional

---

## Como usar

**1. Identifique o prompt do seu domínio.** Leia o README do prompt para entender quando usar e quando evitar.

**2. Adapte a constituição.** A constituição XML é o que diferencia prompt amador de prompt profissional. Adapte tom, regras, exemplos ao seu contexto. Mantenha estrutura.

**3. Construa seu golden set próprio.** O golden set seed traz 10-20 casos representativos. Adicione 20+ casos do seu tráfego real para validação robusta.

**4. Rode evals antes de produção.** Sem eval, prompt vira aposta. Cap 34 do livro detalha o processo. Repositório-irmão tem `eval_runner.py` pronto.

**5. Pin versão em produção.** Use `claude-sonnet-4-XX-YYYYMMDD` (versão datada) em produção, nunca alias. Mudança de modelo precisa eval antes.

---

## Princípios editoriais

**Calibração regulatória.** Prompts setoriais respeitam padrões brasileiros: CFM (saúde), OAB (jurídico), BACEN/CVM (finanças), LGPD (transversal). Cada prompt cita os artigos relevantes.

**Constituição clara.** XML com tags semânticas, sem ambiguidade. Constituição lê como contrato, não como conversa.

**Extended thinking ativado.** Para tarefas analíticas, prompts ativam extended thinking quando apropriado. Trade-off entre custo e qualidade explicitado.

**Golden set realista.** Casos do golden set vêm de padrões reais observados, anonimizados. Não inventados em branco.

**Sem PII no exemplo.** Golden sets nunca contêm dados pessoais reais. Tudo anonimizado, com `[NOME]`, `[CPF]`, etc.

---

## Capítulos relacionados

- **Cap 24 — Engenharia de Prompt Avançada**: 7 técnicas industriais que os prompts aqui aplicam
- **Cap 25 — Prompt Caching**: como os prompts aproveitam cache
- **Cap 23 — Extended Thinking**: quando os prompts ativam thinking
- **Cap 34 — Evaluations**: como validar antes de produção
- **Caps 36-40 — Casos por setor**: contexto setorial completo

---

## Como contribuir

Sua casa tem variante de prompt setorial que funciona melhor que a seed? Contribuição é bem-vinda.

1. Abra issue com label `novo-prompt` e descrição
2. Aguarde alinhamento (especialmente para áreas reguladas)
3. Para áreas reguladas, contribuição passa por revisão de especialista do domínio
4. Abra PR com a estrutura completa

Veja [CONTRATO.md](../CONTRATO.md) para princípios completos.
