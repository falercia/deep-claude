# Lab — Capítulo 30: Construir Skill do Zero

> Lab executável: criar um Claude Skill customizado para sua casa.
> Versão 1.0 — 2026-07

---

## Objetivo

Você vai sair deste lab capaz de:

- Entender estrutura de um skill (SKILL.md + recursos)
- Escrever descrição de skill que ativa com precisão
- Definir triggers e anti-triggers
- Versionar skill com semver
- Instalar localmente em Claude Code ou Cowork
- Testar e iterar

## Pré-requisitos

- Claude Code instalado (ou Cowork)
- Editor de texto
- Conhecimento básico de Markdown
- Lab Cap 9 (tour do Claude Code) recomendado

## Tempo estimado

30 minutos.

## Cenário do lab

Você é CTO da empresa **Acme Energia** e quer criar skill para padronizar como o time analisa contratos de fornecimento elétrico (área crítica para a casa).

## Passo a passo

### Passo 1 — Estrutura básica (5 min)

```bash
mkdir -p ~/meus-skills/contrato-energia-acme
cd ~/meus-skills/contrato-energia-acme
mkdir examples resources
```

Crie `SKILL.md`:

```markdown
---
name: contrato-energia-acme
description: Skill para análise de contratos de fornecimento elétrico da Acme Energia. Acionar quando usuário pedir para "analisar contrato de energia", "revisar acordo elétrico", "due diligence fornecedor energia" ou similar em contexto da Acme. Foca em cláusulas regulatórias ANEEL e específicas do setor elétrico brasileiro.
version: 1.0
---

# Contrato Energia — Acme

## Quando ativar

Acione quando o usuário pedir análise de contrato com fornecedor de energia elétrica.

## Quando NÃO ativar

- Contratos não-elétricos (use analise-juridica-br)
- Análise tarifária pura (use skill específico de tarifa)
```

### Passo 2 — Calibrar trigger (8 min)

Triggers vagos ativam errado. Vamos refinar com 3 ciclos.

**Ciclo 1**: descrição inicial (acima).

Teste no Claude Code:

> "Analise este contrato de SaaS para nossa diretoria"

Se o skill ativou (não deveria), o trigger está amplo demais.

**Ciclo 2**: adicionar especificidade.

Edite SKILL.md:

```markdown
description: Skill ESPECÍFICO para análise de contratos de fornecimento de energia elétrica para a Acme Energia. Acionar APENAS quando: (1) o contrato é de fornecimento elétrico (cláusulas ANEEL, MW, kW, MWh, contratos de comercialização ACL/ACR); (2) é para a Acme Energia (contexto interno). Não ativar para contratos genéricos.
```

Teste de novo. Skill agora só ativa para casos específicos.

**Ciclo 3**: testar caso real:

> "Vou analisar este contrato de fornecimento elétrico com a [fornecedor]"

Skill deve ativar.

### Passo 3 — Adicionar instruções estruturadas (8 min)

Expanda SKILL.md:

```markdown
## Estrutura de análise

Produza análise em 6 seções:

1. **Síntese para diretoria** (3 frases)
2. **Cláusulas ANEEL críticas** (transcrição + análise)
3. **Riscos comerciais** (preço, indexação, garantias)
4. **Riscos regulatórios** (ACL vs ACR, migrações de mercado)
5. **Pontos de negociação** (com proposta alternativa)
6. **Próximos passos**

## Regras absolutas

- NUNCA decidir sobre contrato (output é insumo)
- SEMPRE citar artigo ANEEL aplicável
- SEMPRE sinalizar se contrato envolve geração distribuída

## Glossário ANEEL para uso

- ACL: Ambiente de Contratação Livre
- ACR: Ambiente de Contratação Regulada
- CCEAR: Contrato de Comercialização de Energia em Ambiente Regulado
- CCEE: Câmara de Comercialização de Energia Elétrica

## Modelo recomendado

Claude Opus com extended thinking ativo.

## Disclaimer obrigatório

"Análise gerada com auxílio de IA. Insumo qualificado, sem valor de parecer jurídico. Decisão final cabe à diretoria assessorada por jurídico especializado em setor elétrico."
```

### Passo 4 — Adicionar exemplos (3 min)

Em `examples/`, crie `caso-tipico.md`:

```markdown
# Exemplo de uso

## Input
"Analise este contrato CCEAR com [fornecedor] de 100 MW para 5 anos"

## Output esperado (parcial)

### Síntese para diretoria
Contrato CCEAR de 100 MW por 5 anos com cláusulas predominantemente padronizadas pela ANEEL. Identifiquei 3 cláusulas críticas com risco médio: indexação ao IPCA com piso de 5%, garantia inadequada para volumes acima de 80 MW, e cláusula de força maior restritiva. Recomendo renegociar indexação e garantias antes da assinatura.

### Cláusulas ANEEL críticas
[...]
```

### Passo 5 — Instalar e testar (3 min)

```bash
ln -s ~/meus-skills/contrato-energia-acme ~/.claude/skills/contrato-energia-acme
```

Reinicie Claude Code.

Teste:

> "Acabei de receber um CCEAR de 50 MW para nossa subsidiária de geração. Pode analisar?"

Skill deve ativar e produzir análise estruturada.

### Passo 6 — Versionar (3 min)

Ao iterar, suba versão em SKILL.md:

```markdown
version: 1.1
```

Documente mudanças em `CHANGELOG.md`:

```markdown
# Changelog

## [1.1] — 2026-07-XX
- Adicionado glossário ANEEL no SKILL.md
- Refinado trigger para evitar ativação em contratos genéricos

## [1.0] — 2026-07-XX
- Versão inicial
```

## Validação

Você completou o lab quando:

- ✅ Skill criado com estrutura adequada
- ✅ Trigger calibrado (não ativa errado, ativa certo)
- ✅ Instruções estruturadas no SKILL.md
- ✅ Exemplo de uso documentado
- ✅ Instalado no Claude Code e testado
- ✅ Versionamento iniciado

## Princípios aprendidos

**Trigger é o coração do skill**. Skill que ativa errado polui a operação. Especificidade alta + anti-triggers explícitos.

**SKILL.md como contrato**. Ali está o que o skill faz e não faz. Quem instala lê esse documento.

**Iteração rápida**. Primeira versão nunca está perfeita. 3-5 ciclos de teste com casos reais calibram bem.

**Versionamento desde o início**. Mesmo skill simples merece semver e changelog. Em time, vira ativo compartilhado.

## Próximos passos

- Compartilhe seu skill no repositório interno da sua casa (forkar deep-claude e adicionar lá)
- Para skills genéricos (não-Acme), contribua ao deep-claude com PR
- Cap 30 do livro para padrões avançados

## Conexão com o livro

- Cap 30 — Claude Skills (fundamentação)
- Cap 24 — Engenharia de Prompt
- Cap 9 — Claude Code (ambiente de uso)

## Versão

1.0 — 2026-07
