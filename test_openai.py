import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Diga olá"}]
    )
    print(response.choices[0].message["content"])
except Exception as e:
    print("Erro:", e)

