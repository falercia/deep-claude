# Lab — Capítulo 21: Primeira chamada à API Claude

> Lab executável: do zero ao primeiro response do Claude via API em Python.
> Versão 1.0 — 2026-07

---

## Objetivo

Você vai sair deste lab capaz de:

- Configurar ambiente Python para Anthropic SDK
- Autenticar via API key com boas práticas
- Fazer chamada básica à Messages API
- Estruturar prompt com system + user
- Capturar e tratar resposta
- Calcular custo da chamada
- Implementar retry com exponential backoff

## Pré-requisitos

- Python 3.10+
- Conta Anthropic com API key
- USD 1 em crédito (suficiente para todo o lab)

## Tempo estimado

20 minutos.

## Passo a passo

### Passo 1 — Configurar ambiente (3 min)

```bash
mkdir lab-cap-21
cd lab-cap-21
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install anthropic python-dotenv
```

Crie `.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-...
```

**NUNCA** commite `.env`. Adicione ao `.gitignore`:

```bash
echo ".env" >> .gitignore
echo "venv/" >> .gitignore
```

### Passo 2 — Primeira chamada (5 min)

Crie `primeiro_call.py`:

```python
"""Lab Cap 21 — Primeira chamada à API Claude."""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

response = client.messages.create(
    model="claude-haiku-4-5-20251001",  # Verificar versão corrente no Apêndice Vivo
    max_tokens=512,
    system="Você é um assistente conciso, em português brasileiro.",
    messages=[
        {
            "role": "user",
            "content": "Em duas frases, qual é a vantagem competitiva da arquitetura de transformers vs. RNN?"
        }
    ]
)

print("Resposta:")
print(response.content[0].text)
print(f"\nTokens: {response.usage.input_tokens} input, {response.usage.output_tokens} output")
```

Rode:

```bash
python primeiro_call.py
```

### Passo 3 — Estruturar prompt com XML (5 min)

Crie `prompt_estruturado.py`:

```python
"""Demonstra prompt estruturado com XML para análise."""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

prompt = """<contexto>
Empresa fintech brasileira, 50 funcionários, R$ 30M ARR.
Adotando Claude para fluxos de atendimento e análise de crédito.
</contexto>

<pergunta>
Para essa fintech, qual a primeira frente de adoção que tem ROI mais rápido e menor risco?
Considere LGPD, BACEN e capacidade técnica do time.
</pergunta>

<formato_resposta>
Sintetize em 3 parágrafos:
1. Frente recomendada e justificativa
2. Por que essa frente vs outras
3. Riscos e mitigações
</formato_resposta>"""

response = client.messages.create(
    model="claude-sonnet-4-6-20251022",  # Verificar versão corrente
    max_tokens=1500,
    system="Você é um consultor sênior em adoção de IA em fintechs brasileiras.",
    messages=[{"role": "user", "content": prompt}]
)

print(response.content[0].text)
print(f"\n--- Tokens: {response.usage.input_tokens} in, {response.usage.output_tokens} out")
```

### Passo 4 — Calcular custo (3 min)

Crie `calcular_custo.py`:

```python
"""Calcula custo de uma chamada."""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Preços por 1M tokens — ATUALIZAR conforme Apêndice Vivo
PRECOS = {
    "claude-haiku-4-5-20251001":   {"input": 0.80,   "output": 4.00},
    "claude-sonnet-4-6-20251022":  {"input": 3.00,   "output": 15.00},
    "claude-opus-4-7-20260520":    {"input": 15.00,  "output": 75.00},
}

def calcular_custo(model, input_tokens, output_tokens):
    """Custo em USD."""
    p = PRECOS[model]
    return (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000

model = "claude-sonnet-4-6-20251022"
response = client.messages.create(
    model=model,
    max_tokens=300,
    messages=[{"role": "user", "content": "Diga olá em uma frase."}]
)

custo = calcular_custo(
    model,
    response.usage.input_tokens,
    response.usage.output_tokens
)
print(f"Resposta: {response.content[0].text}")
print(f"Custo: USD {custo:.6f}")
print(f"Em BRL ~5x: BRL {custo * 5:.6f}")
```

### Passo 5 — Retry com exponential backoff (4 min)

Crie `retry.py`:

```python
"""Chamada com retry para resiliência em produção."""

import os
import time
from anthropic import Anthropic, RateLimitError, APIError
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def chamar_com_retry(prompt: str, max_retries: int = 3) -> str:
    """Chama Claude com retry exponencial."""
    for tentativa in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6-20251022",
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except RateLimitError as e:
            wait = 2 ** tentativa
            print(f"Rate limit. Aguardando {wait}s antes de tentativa {tentativa + 2}.")
            time.sleep(wait)
        except APIError as e:
            if e.status_code >= 500:
                wait = 2 ** tentativa
                print(f"Erro de servidor. Aguardando {wait}s.")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError(f"Falhou após {max_retries} tentativas")


print(chamar_com_retry("Em uma frase, o que é resiliência em sistemas distribuídos?"))
```

## Validação

Você completou o lab quando:

- ✅ Ambiente Python configurado com SDK Anthropic
- ✅ API key configurada via .env (NÃO no código)
- ✅ Primeira chamada bem-sucedida
- ✅ Prompt estruturado com XML testado
- ✅ Custo calculado e entendido
- ✅ Retry implementado

## Próximos passos

- Lab Cap 22 — Tool Use prático (próxima versão)
- Cap 21 do livro para detalhes avançados

## Conexão com o livro

- Cap 21 — API + SDKs (fundamentação)
- Cap 24 — Engenharia de Prompt (XML)
- Cap 25 — Prompt Caching (otimização de custo)
- Cap 4-5 — Modelos e tiers

## Pegadinhas comuns

**API key no código**. NUNCA commite. Use `.env` e `.gitignore`.

**Versão de modelo não pinada**. Em produção, use versão datada (`claude-sonnet-4-6-20251022`), não alias (`claude-sonnet-4`). Mudança de modelo silenciosa pode quebrar comportamento.

**Sem retry em produção**. Tier 1 da API tem rate limits modestos. Volume rápido derruba se não retry.

**Sem timeout**. `client.messages.create()` não tem timeout default. Em produção, configure `timeout` para evitar travamento.

## Versão

1.0 — 2026-07
