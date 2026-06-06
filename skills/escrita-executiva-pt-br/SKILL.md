---
name: escrita-executiva-pt-br
description: Skill para escrita executiva em português brasileiro com tom de C-level. Acionar quando usuário pedir para "escrever para executivo", "tom executivo brasileiro", "comunicação para C-level", "redigir nota para conselho", "preparar comunicado executivo" ou similar. Usa frases longas com vírgulas, raciocínio direto, sem cadência de IA, sem clichês corporativos.
version: 1.0
---

# Escrita Executiva PT-BR

## Quando ativar

Acione quando o usuário pedir comunicação para audiência executiva brasileira:

- "escrever uma nota para conselho"
- "redigir comunicado executivo"
- "preparar texto para C-level"
- "comunicação institucional formal"
- "post executivo de autoridade"
- "tom executivo brasileiro"

**Não ative** para:

- Escrita técnica de código ou documentação
- Comunicação informal ou casual
- Conteúdo de marketing (CTAs, hooks)
- Tradução literal de inglês para português

## Voz autoral

O skill produz texto com 6 características:

1. **Frases longas com vírgulas, conjunções e subordinadas**, evitando o estilo curto-curto-curto típico de IA.
2. **Travessão raro**, usado para enfatizar quando realmente cabe, não como muletas.
3. **Sem cadência de IA**: nada de "Em primeiro lugar... Em segundo lugar... Por fim...".
4. **Conjunções ricas**: "porque", "embora", "ainda que", "uma vez que", "na medida em que".
5. **Sem clichês corporativos**: nada de "fundamental", "no final do dia", "olhar holístico", "sinergias", "alavancar".
6. **Densidade alta**: cada parágrafo carrega ideia substantiva, sem enchimento.

## Anti-padrões a evitar

- Listas onde prosa contínua serviria melhor
- Repetição de palavras-chave em frases consecutivas
- "Importante notar que", "Vale destacar que", "É importante mencionar"
- "Solução", "estratégia", "abordagem" usados como muletas
- Vai-e-vem entre formal e casual no mesmo texto
- Emojis no corpo do texto

## Tom de referência

Tom de C-level brasileiro maduro: confiante sem ser arrogante, direto sem ser ríspido, denso sem ser hermético, claro sem ser simplista. Pensa antes de escrever, escreve para quem lê com pouco tempo, não tenta agradar todo mundo.

## Configurações

```xml
<contexto>
  <audiencia>{{conselho | C_level | diretoria | comunicado_publico | post_linkedin}}</audiencia>
  <tom>{{neutro | provocativo | de_autoridade | de_reflexao}}</tom>
  <extensao>{{breve_300_palavras | medio_600_palavras | longo_1200_palavras}}</extensao>
</contexto>
```

## Modelo recomendado

- Claude Opus para textos críticos
- Claude Sonnet para volume

Temperature 0.5 (alguma variação para tom natural, mas não solto).

## Como validar

Antes de entregar, releia checando:

1. Há clichê corporativo? Reescreva.
2. Há frase curta seguida de frase curta seguida de frase curta? Junte com vírgula e conjunção.
3. O texto soa como IA bem-comportada? Adicione personalidade controlada.
4. Há lista quando prosa caberia? Converta.
5. O texto tem densidade ou tem enchimento? Corte.

## Conexões

- Cap 24 — Engenharia de Prompt Avançada
- Cap 10 — Claude Web
- Manifesto de Voz Autoral do livro (paratexto)
