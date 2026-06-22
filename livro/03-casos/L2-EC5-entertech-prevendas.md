# EC5 — ENTERTECH BR
## Pré-vendas com Claude Research

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em vendors brasileiros de software enterprise durante adoção de IA em pré-vendas entre 2024 e 2026; números são realistas mas não identificam empresa específica.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | Vendor BR de software enterprise |
| **Tamanho** | ~120 colaboradores |
| **Ciclo de venda médio** | 9 meses |
| **Ticket** | R$ 800 mil a R$ 4 milhões |
| **Tempo de prep por prospect** | 18-24h (sênior) |
| **Invariantes** | 4, 9 |
| **Frameworks** | F1 DECID-IA, F2 ENCAIXE-5 |

## 2. PROBLEMA

Pré-vendas técnica gasta 18-24h por proposta em pesquisa de prospect. Qualidade desigual entre profissionais. SDR não filtra bem. Perdas tardias no ciclo (chegava à reunião com prospect e descobria desalinhamento técnico que poderia ter sido visto na pesquisa).

## 3. TESE — Profundidade de pesquisa em horas, não dias

Usar Claude Research para profile profundo do prospect, mapa de stakeholders, sinais de compra, comparação com cases similares. SDR + executivo de conta leem o sumário antes de qualquer reunião agendada.

## 4. ARQUITETURA — Claude Research + Skills + Projects

- **Claude Research** como ferramenta central de pesquisa profunda multi-fonte
- **Skills** para padrões reutilizáveis: "perfil de conta", "mapa de stakeholders", "fit técnico", "objeções esperadas"
- **Projects** para histórico por conta
- **Integração com CRM** (Salesforce) por MCP

## 5. WORKFLOW

```
Trigger: lead qualificado entra no CRM
   ↓
Research bundle disparado (5-9 perguntas estruturadas)
   ↓
Output estruturado: brief de 4 páginas
   ↓
Revisão humana (pré-vendas sênior)
   ↓
Ingestão em CRM (campo estruturado por categoria)
   ↓
SDR + executivo de conta leem antes da 1ª reunião
```

## 6. SKILLS PROPRIETÁRIAS DA ENTERTECH

| Skill | Conteúdo |
|-------|----------|
| Perfil de empresa B2B BR | Estrutura societária, faturamento, headcount, tech stack visível, recentes movimentos |
| Mapa de stakeholders | LinkedIn público, mídia, atribuições, decisores prováveis |
| Sinais de compra | Vagas abertas, RFPs, anúncios, mudanças de liderança |
| Fit com nosso produto | Rubrica de adequação por eixo (escala, integração, regulação) |

## 7. MCP

| Conexão | Permissão |
|---------|-----------|
| CRM (Salesforce) | Read-only para pesquisa; write controlado para sumário em campo dedicado |
| Base interna de cases por setor | Read |
| Linkedin Sales Navigator | Via web search controlado |

Aplicação F5: Quadrante B (padrão maduro disponível; dados sensíveis do CRM) — MCP self-hosted ou variante privada.

## 8. GOVERNANÇA F6

- Política explícita sobre uso de dados públicos vs sensíveis
- AUP sobre extração e armazenamento
- LGPD aplicada a dados pessoais de stakeholders (base legal: legítimo interesse com avaliação documentada)
- Revisão humana antes de envio externo
- Comitê comercial + jurídico mensal

## 9. EVALS

**Golden set** de **50 prospect briefs** com gabarito de pré-vendas sêniores. Eval de **honestidade** (não inventar fonte) e **cobertura** (capturou os sinais relevantes?).

## 10. LLMOPS

- Tracing
- Versionamento das Skills
- Auditoria de fontes citadas em cada brief
- Quota por SDR

## 11. MÉTRICAS

| Métrica | Pré-projeto | Resultado |
|---------|-------------|-----------|
| Tempo de prep por prospect | 22h | 4h humano (revisão + ajuste) |
| Conversão SQL → Opp | baseline | +14 pp |
| Win rate | baseline | +6 pp |
| Ticket médio | baseline | +9% (melhor matching de fit) |
| Propostas qualificadas geradas | baseline | 2,1× |

## 12. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Informação imprecisa em conversa de venda | Toda afirmação no brief cita fonte verificável; eval de honestidade mensal |
| Uso indevido de dados pessoais (LGPD) | Política rígida; treinamento; auditoria |
| Dependência da qualidade da pesquisa | SDR treinado para ler com ceticismo |

## 13. LIÇÃO ESTRUTURAL

*O ganho em pré-vendas vem de chegar à reunião sabendo mais que o concorrente. Research bem operado é desigualdade competitiva; mal operado é embaraço público. F2 ENCAIXE-5 explica por que Claude Research é o encaixe certo aqui: contexto longo + multi-fonte + síntese estruturada.*

## 14. CONEXÕES

- 🔗 [Manifesto](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Inv. 4, 9)
- 🔗 Frameworks: [F1](../../Livro-1-Os-Invariantes/03-frameworks/L1-F1-decid-ia.md), [F2](../../Livro-1-Os-Invariantes/03-frameworks/L1-F2-encaixe-5.md)
- 🔗 Caps: [15 Comparação](../../Livro-1-Os-Invariantes/02-capitulos/L1-C15-comparacao-modelos.md), [34 Executivos](../../Livro-1-Os-Invariantes/02-capitulos/L1-C44-roadmap-pessoal.md)
- 🔗 Claude: [Cap 22 Research](../02-capitulos/L2-C23-research.md), [Cap 31 Skills](../02-capitulos/L2-C32-skills.md), [Cap 20 Projects](../02-capitulos/L2-C21-projects.md)

---

> *"Em pré-vendas, IA não substitui o vendedor; ela compõe a desigualdade competitiva que o vendedor leva à reunião."*
