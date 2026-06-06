"""Lab Cap 21 — Primeira chamada à API Claude.

Pré-requisitos:
    pip install anthropic python-dotenv

.env:
    ANTHROPIC_API_KEY=sk-ant-...

Executar:
    python primeiro_call.py
"""

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
