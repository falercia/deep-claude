# Claude Skills

> Skills prontos para Claude Code e Cowork, organizados por domínio profissional.

---

## Por que esta pasta existe

A obra *Deep Claude*, no Capítulo 30, apresenta Claude Skills como mecanismo de extensão progressiva e descoberta on-demand. Esta pasta carrega skills prontos para instalação em Claude Code e Cowork, organizados por domínio profissional brasileiro.

Skills aqui são reusáveis, versionados, com SKILL.md autodocumentado, e testados em ambiente real.

---

## O que é Skill

Skill é descrição estruturada em Markdown (SKILL.md) que Claude usa para acionar comportamento específico quando trigger ativa. Diferente de prompt, skill é registrado uma vez no ambiente e descoberto on-demand pelo Claude.

Vantagem: skill mantém prompt limpo (não polui contexto principal), permite versionamento (skill é arquivo), permite compartilhamento (basta copiar pasta).

Para a fundamentação completa, ver Capítulo 30 do livro.

---

## Estrutura por skill

Cada skill segue a estrutura padrão Anthropic:

```
skills/<nome-do-skill>/
  SKILL.md          — descrição estruturada, triggers, instructions
  README.md         — propósito, casos de uso, exemplos
  examples/         — exemplos de uso real
  resources/        — arquivos de apoio (templates, configs)
```

---

## Cobertura inicial — v1.0 (jul/2026)

3 skills core como ponto de partida:

| Skill | Domínio | Trigger principal |
|---|---|---|
| `analise-juridica-br` | Jurídico brasileiro | "analisar contrato", "revisar cláusulas" |
| `escrita-executiva-pt-br` | Comunicação corporativa | "escrever para executivo", "tom executivo brasileiro" |
| `dashboard-azure-devops` | Engenharia | "dashboard Azure DevOps", "métricas do sprint" |

---

## Cobertura roadmap

### v1.1 — out/2026

| Skill | Domínio |
|---|---|
| `anamnese-medica-cfm` | Saúde (respeitando CFM) |
| `analise-credito-bacen` | Finanças |
| `suporte-tier1-saas` | SaaS |
| `triagem-rh-br` | RH com mitigação de viés |

### v1.2 — jan/2027

| Skill | Domínio |
|---|---|
| `governance-ia-comite` | Governança executiva |
| `lgpd-checker` | Compliance LGPD |
| `marketing-content-br` | Marketing PT-BR |
| Cobertura adicional Cowork específica |

---

## Como instalar

### Em Claude Code

```bash
# Clone o repositório (uma vez)
git clone https://github.com/falercia/deep-claude.git ~/repos/deep-claude

# Symlink para diretório de skills do Claude Code
mkdir -p ~/.claude/skills
ln -s ~/repos/deep-claude/skills/<nome-do-skill> ~/.claude/skills/<nome-do-skill>
```

### Em Cowork

Cowork tem mecanismo próprio de instalação de skills via Settings > Capabilities. Cada skill desta pasta inclui instruções específicas de instalação no Cowork.

---

## Princípios

**Trigger preciso.** Skill que ativa em momentos errados polui a operação. Descrição em SKILL.md deve descrever com clareza quando ativa, dando contexto, palavras-chave e exemplos.

**Auto-contido.** Skill não depende de configuração externa. Todos os recursos necessários estão na pasta do skill.

**Versionado.** Cada skill carrega versão semântica em SKILL.md. Mudança breaking gera bump major.

**Testado em real.** Skills aqui foram exercitados em ambiente real do autor antes de publicação. Sem teste, skill é receita teórica.

---

## Como contribuir

Sua casa criou skill que funciona bem em domínio brasileiro? Contribuição é bem-vinda.

1. Abra issue com label `novo-skill`
2. Descreva trigger, casos de uso e exemplos
3. Abra PR com a estrutura completa (SKILL.md + README + examples)
4. Skill passa por revisão funcional e editorial

Veja [CONTRATO.md](../CONTRATO.md) para princípios completos.

---

## Capítulos relacionados

- **Cap 30 — Claude Skills**: fundamentação completa
- **Cap 9 — Claude Code**: contexto de uso primário dos skills
- **Cap 8 — Cowork**: contexto de uso alternativo
- **Cap 36-40 — Casos por setor**: domínios cobertos pelos skills

---

## Referências oficiais

- **Anthropic Skills repository**: https://github.com/anthropics/claude-skills
- **Docs oficiais**: https://docs.anthropic.com/ (seção Skills)
- **Skill Creator**: skill oficial da Anthropic para criar skills
