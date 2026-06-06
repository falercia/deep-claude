# Changelog do Apêndice Vivo

> Histórico mensal de atualizações, mudanças observadas e errata pública.
> Cadência: dias 1-7 de cada mês. Mudanças relevantes fora da janela geram alerta extraordinário aqui.

---

## 2026-07 (planejado — lançamento oficial)

### Adicionado
- Snapshot completo de modelos vigentes em julho/2026
- Preços oficiais com cotação USD/BRL do mês
- Benchmarks atualizados conforme leaderboards oficiais
- Janelas de contexto e SLAs por plano

### Marco
- Versão 1.0 do Apêndice Vivo casando com o lançamento do livro

---

## 2026-06-06 (seed inicial)

### Adicionado
- Estrutura do Apêndice Vivo: 5 arquivos temáticos + changelog
- Princípios de leitura para cada arquivo
- Lista de fontes primárias estruturada
- Padrões de versionamento explícito (modelo + data)
- Padrão de transparência temporal (`Atualizado em` em cada item)

### Princípios estabelecidos
- Fonte primária obrigatória em cada item
- Errata pública via este changelog
- Cadência mensal declarada (dias 1-7)
- Sem cherry-picking de benchmark
- Cotação cambial via Banco Central

---

## Errata pública

*Quando informação anterior estava errada, errata explícita aqui com data, descrição e correção. Não removida silenciosamente do histórico do snapshot.*

Formato típico de errata:

```
### Errata YYYY-MM-DD
- **Arquivo**: PRECOS.md
- **Item**: Preço de Sonnet 4.6 input
- **Anterior**: $X / 1M tokens
- **Correto**: $Y / 1M tokens
- **Fonte**: link para doc oficial vigente na correção
- **Impacto para o leitor**: orçamentos calculados com valor anterior precisam ser revisitados.
```

Nenhuma errata até o momento.

---

## Alertas extraordinários

*Mudanças relevantes fora da janela mensal (lançamento de modelo, mudança de preço, incidente grave) geram alerta aqui sem esperar a janela.*

Nenhum alerta até o momento.

---

## Cadência

| Janela | Atividade |
|---|---|
| Dia 1-3 do mês | Coleta de mudanças nas fontes primárias |
| Dia 4-6 do mês | Atualização dos arquivos do Apêndice |
| Dia 7 do mês | Publicação do snapshot do mês |
| Mid-month | Alertas extraordinários se aplicável |

**Compromisso declarado**: a cadência mensal é compromisso editorial. Não cumprir compromisso vira perda de credibilidade da obra.

---

## Como contribuir

Observou mudança em fonte primária que não está refletida no Apêndice Vivo?

1. Abra issue no repositório com label `errata` ou `nova-fonte`
2. Inclua link para fonte primária
3. Descreva a mudança e o impacto
4. Mantenedor processa na próxima janela mensal (ou em alerta extraordinário se crítico)

Veja [CONTRATO.md](../CONTRATO.md) para o fluxo completo.
