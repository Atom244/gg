import requests
import json
# перед запуском: pip install requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"

MODEL = "deepseek/deepseek-chat"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Console Chat"
}

messages = [
    {
        "role": "system",
        "content": (
            "Ты дружелюбный чат-бот. "
            "Отвечай по-русски, без рассуждений и служебного текста."
        )
    }
]

print("Console Chat (exit / quit for exit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ("exit", "quit"):
        print("bye")
        break

    if not user_input:
        print("empty enter\n")
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "model": MODEL,
            "messages": messages
        }
    )

    if response.status_code != 200:
        print("error:", response.text)
        continue

    data = response.json()
    answer = data["choices"][0]["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": answer
    })

    print("\nAI:", answer, "\n")
