# O Que Mudou Nesta Edição

Este é o livro vivo da série: o corpo ensina o que dura, e o Apêndice Vivo (J) carrega o número da semana, com fonte e data. Esta página resume, em linguagem direta, o que mudou desde a versão anterior da edição digital — leia em dois minutos e decida se precisa reler algo.

## Edição de outubro de 2026 (revisão de 1º de outubro)

**O que mudou no corpo.** Uma correção de interpretação, na seção 45.3.6 do Capítulo 45: o texto atribuía a marca d'água mundial a um cálculo de custo da Anthropic. A razão que a empresa declara é outra, uma limitação técnica de escopo regional, com sinal de que pode regionalizar depois. O padrão continua valendo, agora mais honesto: obrigação europeia que vira comportamento global por atrito de arquitetura, não por estratégia.

**O que mudou no Apêndice Vivo (agora na versão 0.5).**

1. **Nova geração da família Claude.** Fable 5.1 (1º de setembro), Opus 5.5 (22 de setembro, US$ 4/20) e Sonnet 5.5 (28 de setembro, US$ 2/10). O Fable 5.1 manteve US$ 10/50, mas a leitura de cache caiu para US$ 0,25. Se você compara só entrada e saída, está olhando o número errado.
2. **Contrato de API mudou.** Tool use forçado retorna erro, o raciocínio do Opus 5.5 não pode ser desligado e o histórico da conversa precisa ser append-only. Rode sua suíte de avaliação antes de trocar de modelo, mesmo com o preço igual ou menor.
3. **Cobrança deixou de ser só por token.** Agentes gerenciados cobrem horas de sessão (US$ 0,08 por hora em execução), residência de dados nos EUA custa 1,1x e ferramentas têm tarifa própria.
4. **Correção de erro nosso.** A tabela de usage credits da versão 0.4 estava errada: em Max e seats premium o Fable fica incluído até 50% dos limites semanais, sem data de término; em Pro e seats standard o corte foi em 19 de julho, não 7 de julho.
5. **Salvaguardas viraram produto.** Programa de verificação para ciências da vida (17 de setembro) e Enterprise Frontier Safeguards (1º de setembro) mudam o que seu contrato precisa dizer sobre retenção e monitoramento.
6. **Regulação.** O PL 2338 segue aguardando parecer do relator na Câmara; a API de detecção de marcas d'água está em private preview desde 1º de setembro.

**Por que isso importa.** Em dois meses, o preço de topo convergiu entre os dois grandes fornecedores e a disputa migrou para o custo de cache, a unidade de cobrança passou a incluir o tempo de vida do agente, e um erro do próprio apêndice foi corrigido com fonte. Nenhum capítulo precisou de reescrita de padrão, a não ser a correção de interpretação acima.

---

## Edição de agosto de 2026 (revisão de 12 de agosto)

**O que entrou nos capítulos.**

1. **Capítulo 45 (Segurança, Compliance e LGPD)** ganhou a seção 45.3.6 sobre marcação de conteúdo gerado: desde agosto de 2026, o que o Claude gera carrega marca d'água invisível no texto e metadados assinados em arquivos, em qualquer produto e em qualquer país. A seção explica o que isso significa para a sua operação — inclusive o fato de que os documentos que sua empresa emite com apoio do Claude saem marcados — e o princípio que evita o erro caro: **a marca prova processamento, não autoria**.
2. **Capítulo 5 (Quando Usar Cada Modelo)** ganhou o Padrão 6: roteamento também é continuidade. Classificadores de segurança podem redirecionar sua requisição para outro modelo sem a sua aplicação escolher, e a fronteira do que redireciona muda quando o fornecedor recalibra salvaguardas — não só quando lança modelo. Sua política de roteamento precisa declarar qual degradação aceita, por escrito, antes do incidente.
3. **Capítulo 4 (Todos os Modelos Claude)** ganhou dois avisos de comparação: compare custo por tarefa e nunca por token (tokenizers mudam entre gerações), e o tier premium pode oferecer modo de velocidade premium (fast mode) com sobrepreço.

**O que mudou no Apêndice Vivo (agora na versão 0.4).**

1. **Marcas d'água:** seção nova com os dois mecanismos (watermark no texto, C2PA em arquivos), o que cobrem, o que não provam e onde acompanhar as ferramentas de detecção prometidas.
2. **Sonnet 5:** o aumento de preço programado para 1º de setembro **foi cancelado** — US$ 2/10 por milhão de tokens virou o preço padrão. Se você orçou com US$ 3/15, revise para baixo.
3. **Fable 5:** salvaguardas de biologia recalibradas em 7 de agosto — perguntas cotidianas de saúde deixaram de cair no fallback; só usos sensíveis (virologia, toxicologia, design molecular) seguem redirecionados ao Opus 5.
4. **Fonte única de números:** os espaços reservados para preços de concorrentes (GPT, Gemini, Grok) agora apontam para a Trilha do Número do Livro 1, que é a camada multi-vendor da série. Um número, um lugar, uma manutenção.

**Por que isso importa.** Em nove dias de agosto, um preço anunciado morreu antes de entrar em vigor, uma salvaguarda mudou de fronteira sem release de modelo e todo texto gerado passou a carregar assinatura invisível. Nenhuma dessas mudanças exigiu reescrever um capítulo — os três já ensinavam o padrão; o apêndice absorveu o número. É o desenho do livro funcionando.

---

*O histórico completo, com fonte primária por item, está no controle de versão do Apêndice Vivo e no repositório. Ative watch no GitHub para ser notificado das próximas revisões.*
