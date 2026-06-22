# Checklist de Lançamento — Deep Claude

*Status: em preparação · Data alvo de lançamento: [DATA A DEFINIR — AUTOR]*

Este checklist cobre o caminho completo da obra desde o manuscrito fechado até o livro disponível ao leitor. Itens marcados com **[AUTOR]** dependem de input ou aprovação do Fabio Garcia e não avançam sem ele.

---

## FRENTE 1 — REVISÃO FINAL DO MANUSCRITO

> *Não iniciar diagramação antes de todos os gates desta frente estarem verdes.*

- [ ] Voz autoral ("DA CADEIRA DO CTO"): boxes em todos os capítulos-chave (8, 9, 15, 42, 43, 44, 45)
- [ ] Capítulo 5b "Quando Claude, quando não" — revisado e ancorando ao Apêndice para números
- [ ] Apêndice K "Os 9 Modos de Falha" — completo, um modo por Invariante
- [ ] Boxes POSTMORTEM: caps 8, 9, 13/6, 25, 29/30, 36, 43, 28 — todos redigidos
- [ ] Casos setoriais (37-41): cada um com "o que quase deu errado" + Invariante violado
- [ ] Callbacks conceituais ao Livro 1 nos 6 pontos definidos na Banca Adversarial
- [ ] Frases-assinatura por capítulo — todos os 47 caps + 5b + K
- [ ] Galé seletiva: corte de 10-15% nos capítulos que incharam no sweep
- [ ] Apêndice Vivo J: 100% preenchido, com fonte e data por linha (sem campos TBD)
- [ ] Três diagramas faltantes: mapa unificado do ecossistema, matriz risco×autonomia, pipeline de uso seguro corporativo
- [ ] Build final: verificação de links internos, numeração, referências cruzadas L1/L2

**Gate de saída desta frente:** manuscrito aprovado pelo autor **[AUTOR]** + build sem erro.

---

## FRENTE 2 — PRODUÇÃO EDITORIAL

### 2.1 ISBN e Ficha CIP

- [ ] **[AUTOR]** Solicitação de ISBN à Câmara Brasileira do Livro (CBL) ou Biblioteca Nacional
- [ ] Recebimento do ISBN
- [ ] Geração da Ficha CIP (Catalogação na Publicação)
- [ ] Inserção do ISBN e Ficha CIP na página de copyright do manuscrito

> *Sem ISBN não há PDF final com número na capa. Bloqueia: diagramação final, capa definitiva, distribuição.*

### 2.2 Diagramação e PDF

- [ ] Definição do diagramador/ferramenta **[AUTOR]**
- [ ] Briefing de diagramação: tipografia, margens, espaçamento, tratamento dos boxes (POSTMORTEM, DA CADEIRA DO CTO, INVARIANTE-MÃE, TEATRO DE IA)
- [ ] Tratamento do sistema de diagramas SVG (107 diagramas → verificar resolução para impressão/tela)
- [ ] Primeira prova de diagramação
- [ ] **[AUTOR]** Revisão e aprovação da prova
- [ ] Correções pós-revisão
- [ ] **[AUTOR]** Aprovação final da diagramação
- [ ] Geração do PDF final (versão digital) com ISBN
- [ ] Geração do EPUB (se aplicável)
- [ ] Geração do arquivo para impressão POD (se aplicável) — 300 dpi, sangria, CMYK

### 2.3 Capa

- [ ] Briefing de capa: conceito A (companheiro visual ao L1), tipografia, laranja Anthropic (#E97451), creme (#fefce8), selo "Volume Vivo · 2026", ano em destaque **[AUTOR]**
- [ ] Entrega da capa pelo designer
- [ ] **[AUTOR]** Aprovação da capa
- [ ] Versões da capa: frente isolada (PNG alta resolução), capa aberta (frente+lombada+quarta), versão digital (EPUB cover, tamanhos para plataformas)
- [ ] Integração da capa ao PDF de diagramação

### 2.4 Quarta Capa

- [ ] Texto da quarta capa (rascunho em `livro/00-paratexto/L2-00-capa-e-titulos.md` — Rota A)
- [ ] **[AUTOR]** Aprovação ou ajuste do texto
- [ ] Integração na capa pelo designer

---

## FRENTE 3 — PLATAFORMAS E DISTRIBUIÇÃO

- [ ] **[AUTOR]** Decisão de canal de venda: Amazon KDP, Hotmart, loja própria, livrarias físicas?
- [ ] Criação/ajuste de conta na(s) plataforma(s) escolhida(s)
- [ ] Upload do PDF/EPUB final
- [ ] Preenchimento de metadados: título, subtítulo, série, autor, ISBN, categoria, palavras-chave, descrição (usar texto da quarta capa)
- [ ] Definição de preço **[AUTOR]**
- [ ] Definição de data de lançamento **[AUTOR]**
- [ ] Configuração de pré-venda (se aplicável)
- [ ] Revisão de página de produto antes de publicar **[AUTOR]**
- [ ] Publicação (apertar o botão) **[AUTOR]**

---

## FRENTE 4 — LANDING PAGE

- [ ] **[AUTOR]** Decisão: página própria (domínio) ou página no repositório GitHub?
- [ ] Conteúdo da landing: título, subtítulo, promessa central, sumário visual, sobre o autor, link de compra, link do repositório
- [ ] Texto da landing baseado em `livro/_plano/POSICIONAMENTO-L2.md`
- [ ] **[AUTOR]** Aprovação do texto
- [ ] Implementação (HTML simples, GitHub Pages, ou plataforma a definir)
- [ ] Imagem da capa na landing
- [ ] Link de compra funcional
- [ ] **[AUTOR]** Revisão e publicação

---

## FRENTE 5 — KIT DE DIVULGAÇÃO

- [ ] Ler e completar `lancamento/KIT-DIVULGACAO.md`
- [ ] **[AUTOR]** Revisão e personalização dos textos (voz do autor)
- [ ] Imagens de divulgação: banners para LinkedIn (1200×627), cards de citação (1080×1080)
- [ ] **[AUTOR]** Foto do autor em alta resolução (para bio e imprensa)
- [ ] Release para imprensa (criar em `lancamento/prensa/`)
- [ ] FAQ do livro (criar em `lancamento/faq/`)

---

## FRENTE 6 — DIVULGAÇÃO (EXECUTAR NO DIA E SEMANA DO LANÇAMENTO)

*Não executar antes de o livro estar disponível para compra.*

- [ ] **[AUTOR]** Post de anúncio no LinkedIn (usar Gancho 1 ou 2 de `POSICIONAMENTO-L2.md`)
- [ ] Publicação de thread aprofundada (usar estrutura de `KIT-DIVULGACAO.md`)
- [ ] E-mail para lista (se houver) **[AUTOR]**
- [ ] Atualização do perfil do repositório GitHub: README principal com link de compra
- [ ] Atualização do `CONTRATO.md` e `README.md` do repo com link de compra
- [ ] Comunicação para comunidades relevantes (fóruns, grupos, comunidades de tecnologia BR) **[AUTOR]**
- [ ] Convite para primeiros leitores deixarem avaliação na plataforma de venda

---

## DATAS-CHAVE (PREENCHER — AUTOR)

| Marco | Data planejada | Responsável |
|---|---|---|
| Manuscrito fechado (gate) | [A DEFINIR] | Autor |
| ISBN solicitado | [A DEFINIR] | Autor |
| ISBN recebido | [A DEFINIR] | Câmara/BN |
| Diagramação entregue | [A DEFINIR] | Diagramador |
| Capa aprovada | [A DEFINIR] | Autor |
| PDF final gerado | [A DEFINIR] | Diagramador |
| Landing page no ar | [A DEFINIR] | A definir |
| Abertura de pré-venda | [A DEFINIR] | Autor |
| **Data de lançamento** | **[A DEFINIR]** | **Autor** |
| Primeiro post de divulgação | [A DEFINIR] | Autor |

---

## DEPENDÊNCIAS CRÍTICAS (ordem importa)

```
Manuscrito fechado
  → Apêndice Vivo J 100% preenchido
    → ISBN solicitado
      → ISBN recebido
        → Diagramação final
          → Capa final
            → PDF final
              → Upload na plataforma
                → Landing page
                  → Data de lançamento confirmada
                    → Divulgação pública
```

Nenhuma etapa de divulgação externa deve acontecer antes de o livro estar disponível para compra. Expectativa sem entrega é a única coisa pior do que silêncio.

---

*Última atualização: 2026-06-22 · Responsável pelo checklist: [A DEFINIR — AUTOR]*
