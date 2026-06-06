# P-LEG-CLAUDE-01 — Análise estruturada de contrato

> Prompt profissional para análise de contrato com Claude Opus + extended thinking.
> Calibrado para o contexto regulatório brasileiro (OAB, LGPD).
> Versão 1.0 — 2026-07

---

## Quando usar

Use este prompt quando precisar de uma análise estruturada de contrato com identificação de cláusulas críticas, riscos contratuais e pontos de negociação. Tipicamente para:

- Due diligence em M&A (revisão de portfólio contratual do alvo)
- Revisão de contrato de prestação de serviços antes de assinatura
- Análise de contrato de fornecedor crítico (tecnologia, infraestrutura, dados)
- Auditoria de contratos vigentes para mapeamento de riscos

O prompt aciona **extended thinking** para análise profunda (consome ~3-5x mais tokens que prompt padrão, mas entrega cobertura analítica significativamente superior).

## Quando NÃO usar

Não use este prompt para:

- **Substituir advogado.** Output é insumo qualificado para discussão com jurídico interno, nunca documento final. OAB Provimento 205/2021 sobre IA jurídica é referência.
- **Decisão final em contrato regulatório.** Áreas com regulação setorial (BACEN, ANS, CVM) exigem revisão humana especializada antes de qualquer ação.
- **Contratos em jurisdições não-brasileiras.** Prompt é calibrado para Direito brasileiro; outras jurisdições demandam adaptação significativa.
- **Documentos não-contratuais.** Atos societários, sentenças, pareceres têm estruturas diferentes; este prompt não cobre.

## Fundamentação regulatória

| Norma | Aplicação |
|---|---|
| **OAB Provimento 205/2021** | IA jurídica deve ser supervisionada por advogado; outputs são insumos |
| **LGPD Art. 5, 7, 46** | Tratamento de dados pessoais em contratos; cláusulas de proteção |
| **Código Civil Arts. 421, 422** | Função social do contrato; boa-fé objetiva |
| **CDC** (Lei 8.078/90) | Quando aplicável (relações de consumo) |
| **MP/Lei das Estatais** (13.303/16) | Quando uma das partes for estatal |

## Estrutura do prompt

O prompt produz output em **5 seções estruturadas**:

1. **Síntese executiva** (3-5 frases) — para CTO/CEO/CFO em 60 segundos
2. **Cláusulas críticas identificadas** — com transcrição literal + análise + risco classificado (alto/médio/baixo)
3. **Pontos de negociação prioritários** — com proposta de redação alternativa
4. **Riscos LGPD e regulatórios** — específicos quando aplicável
5. **Próximos passos recomendados** — ação executiva

## Como adaptar ao seu contexto

A constituição XML do prompt traz parâmetros configuráveis no bloco `<contexto>`. Adapte os 4 elementos:

```xml
<contexto>
  <setor>{{seu_setor}}</setor>
  <jurisdicao>{{jurisdicao_principal}}</jurisdicao>
  <relacao>{{B2B | B2C | Estatal}}</relacao>
  <criticidade>{{alto | medio | baixo}}</criticidade>
</contexto>
```

**Setor**: jurídico (universal), saúde, fintech, SaaS, indústria, etc.
**Jurisdição**: Brasil é o padrão; se multi-jurisdição, declarar.
**Relação**: B2B (entre empresas), B2C (com consumidor — aplica CDC), Estatal (aplica Lei das Estatais).
**Criticidade**: alto/médio/baixo conforme valor e impacto.

## Modelo e configuração recomendados

| Parâmetro | Valor recomendado |
|---|---|
| Modelo | Claude Opus (versão corrente) |
| Extended thinking | Ativo (budget 8000-16000 tokens) |
| Temperature | 0.0 (determinístico para análise) |
| Max output tokens | 4000 |
| System prompt | Ver `prompt.xml` |

Em ambiente com volume alto, considere Claude Sonnet para casos não-críticos (menor custo) e Opus para casos de alto valor.

## Custo estimado

| Cenário | Tokens input | Tokens output | Tokens thinking | Custo aprox. |
|---|---|---|---|---|
| Contrato 10 páginas | ~8.000 | ~2.500 | ~10.000 | Ver Apêndice Vivo |
| Contrato 50 páginas | ~40.000 | ~3.500 | ~12.000 | Ver Apêndice Vivo |

Valores atualizados estão em `/apendice-vivo/PRECOS.md`. Para análise em volume, considere prompt caching (Cap 25 do livro).

## Validação antes de produção

**Obrigatório:**

1. Construir golden set com 20+ casos representativos do seu tráfego
2. Rodar evals comparando output vs revisão humana de referência
3. Pinar versão de modelo (`claude-opus-X.X-YYYYMMDD`) em produção
4. Implementar mecanismo de "advogado-no-loop" para casos de alto risco
5. Audit log de cada análise para defesa em caso de questionamento

## Conexão com o livro

- **Cap 23 — Extended Thinking**: fundamentação de quando ativar
- **Cap 24 — Engenharia de Prompt Avançada**: técnicas XML aplicadas aqui
- **Cap 25 — Prompt Caching**: otimização para volume
- **Cap 36 — Casos Jurídicos**: contexto completo do prompt
- **Cap 44 — Segurança, Compliance e LGPD**: tratamento de dados em contratos

## Changelog

Ver [`changelog.md`](./changelog.md).
