# EC7 — INSTITUTO NORTE
## Programa de letramento em IA para executivos com avaliação

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em escolas de negócios brasileiras durante adoção de IA em formação executiva entre 2025 e 2026; números são realistas mas não identificam instituição específica.

---

## 1. CONTEXTO

| Dimensão | Detalhe |
|----------|---------|
| **Setor** | Educação executiva (pós-MBA) |
| **Tamanho** | Turma de 80 alunos C-Level e diretores |
| **Programa** | "AI for Executives" — 8 semanas |
| **Investimento por aluno** | R$ 24-32 mil |
| **Invariantes** | 7, 9 |
| **Frameworks** | F1 DECID-IA, F8 EVAL-PIRÂMIDE |

## 2. PROBLEMA

Demanda explosiva por "AI for Executives". Oferta atual no mercado é rasa, motivacional, sem método de avaliação. Alunos terminam o curso sabendo siglas, não sabendo decidir. NPS dos programas existentes no mercado: 6-7 em 10.

## 3. TESE — Aplicação ao próprio caso + Validação UAU como gate

Programa baseado na obra *Inteligência Aumentada* + frameworks proprietários (F1-F9) + Validação UAU por capítulo + projeto final aplicado ao próprio negócio do aluno, com defesa oral.

## 4. ARQUITETURA PEDAGÓGICA

```
Semana N:
1. Pré-leitura por trilha (capítulos do livro)
   ↓
2. Aula síncrona com partner do Instituto
   ↓
3. Workshop com o framework (F1, F2, F3...)
   ↓
4. Aplicação ao próprio caso (slot dedicado)
   ↓
5. Revisão por pares (3 alunos em grupo)
   ↓
6. Revisão por partner (assíncrono, com rubrica)
   ↓
Validação UAU semanal — 5 critérios
```

## 5. AVALIAÇÃO

- **Validação UAU** por capítulo (autoavaliação reportada)
- **Rubrica do partner** por projeto semanal
- **Defesa final oral** (20 minutos) com banca de 3 partners

## 6. SKILLS AUXILIARES PARA ALUNOS

| Skill | Função |
|-------|--------|
| Auditor de governança | Aplica F6 GOV-INDELEGÁVEL no próprio negócio do aluno |
| Analisador de trade-off de modelo | Aplica F2 ENCAIXE-5 em casos do aluno |
| Avaliador de pirâmide de evals | Aplica F8 EVAL-PIRÂMIDE em features do aluno |

## 7. MÉTRICAS

| Métrica | Meta |
|---------|------|
| Taxa de conclusão | 92% |
| NPS do programa | 78+ |
| Aplicação real declarada em 60 dias pós-programa | ≥70% dos alunos |
| Cases gerados pelos próprios alunos | 1 por aluno (case do próprio negócio) |

## 8. ROI PARA O ALUNO

Casos reais (cenário ilustrativo) já mostraram payback do programa em **1 decisão de adoção bem feita** — exemplo típico: aluno evita migração desnecessária de stack de IA na empresa após aplicar F2 e perceber que a decisão era reativa, não fundamentada. Economia estimada: 3-12 meses de salário do CTO em retrabalho evitado.

## 9. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|-------|-----------|
| Aluno usa IA para "fingir" o projeto | Defesa oral; rubrica que premia decisão informada, não output bonito |
| Programa vira teatro motivacional | Método rígido + Validação UAU + projeto aplicado |
| Método não escala sem partners qualificados | Treinamento intensivo de partners; certificação interna |
| Aluno entra esperando "10 prompts mágicos" | Comunicação prévia clara: "este programa ensina método, não receita" |

## 10. LIÇÃO ESTRUTURAL

*Educação executiva em IA só funciona com aplicação ao próprio caso e avaliação pelo partner. Sem isso, vira curso de slides sobre o futuro. O Invariante 9 (Operador) sustenta: o programa ensina a operar, não a usar. A diferença vira diferencial de carreira do aluno.*

## 11. CONEXÕES

- 🔗 [Manifesto](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md) (Inv. 7, 9)
- 🔗 Frameworks: [F1](../../Livro-1-Os-Invariantes/03-frameworks/L1-F1-decid-ia.md), [F2](../../Livro-1-Os-Invariantes/03-frameworks/L1-F2-encaixe-5.md), [F6](../../Livro-1-Os-Invariantes/03-frameworks/L1-F6-gov-indelegavel.md), [F8](../../Livro-1-Os-Invariantes/03-frameworks/L1-F8-eval-piramide.md)
- 🔗 Caps: [44 Roadmap pessoal](../../Livro-1-Os-Invariantes/02-capitulos/L1-C44-roadmap-pessoal.md), [00M Manifesto](../../Livro-1-Os-Invariantes/01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 Claude: [Cap 34 Executivos](../02-capitulos/L2-C35-executivos.md), [Cap 31 Skills](../02-capitulos/L2-C32-skills.md)

---

> *"Educação executiva em IA precisa de projeto, defesa e rubrica. Sem isso, vira curso de slides sobre o futuro."*
