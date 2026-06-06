# Skill — analise-juridica-br

> Skill de apoio à análise contratual sob Direito brasileiro.
> Versão 1.0 — 2026-07

---

## Para quem é

Para advogados internos, consultores jurídicos, analistas contratuais e CTOs que precisam de triagem rápida de contratos antes de revisão jurídica formal.

## Como instalar

### Em Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s /caminho/para/deep-claude/skills/analise-juridica-br ~/.claude/skills/analise-juridica-br
```

Após instalar, o skill é descoberto automaticamente quando você pede análise de contrato.

### Em Cowork

Em Cowork, vá em Settings > Capabilities > Skills > Install from folder, aponte para esta pasta.

## Como usar

Após instalar, basta pedir naturalmente:

> "Analise este contrato de prestação de serviços que vou anexar"
> "Faça due diligence das cláusulas críticas deste contrato"
> "Identifique pontos de negociação neste acordo de SaaS"

O skill ativa automaticamente e estrutura a análise nas 5 seções padrão.

## Exemplo de uso

**Input do usuário**:
> "Analise este contrato de cloud para nossa fintech. Anexo no chat."

**Output esperado**:
- Síntese executiva
- 3-7 cláusulas críticas com classificação
- 2-5 pontos de negociação
- Análise LGPD + BACEN (setor fintech)
- 3-5 próximos passos
- Disclaimer obrigatório

## Limitações

- **Calibrado para Brasil**. Outras jurisdições demandam adaptação significativa.
- **Não é parecer**. É insumo qualificado para advogado.
- **Não detecta tudo**. Cláusulas tecnicamente complexas (compromisso arbitral elaborado, garantias estruturadas) podem exigir advogado especializado.

## Conexão com o livro

- Cap 36 — Casos Jurídicos (contexto completo)
- Cap 23 — Extended Thinking (técnica subjacente)
- Cap 30 — Claude Skills (fundamentação)

## Versão

1.0 — 2026-07
