import requests
import base64
from . import API_KEY

OPENROUTER_API_KEY = API_KEY.API_KEY

MODEL = "deepseek/deepseek-chat"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # optional but recommended
    "X-Title": "My App"
}

chat_history = []

def send_chat_message(text: str):
    """Send chat message using OpenRouter free model."""

    chat_history.append({
        "role": "user",
        "content": text
    })

    data = {
        "model": MODEL,
        "messages": chat_history,
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1024
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()

    reply = result["choices"][0]["message"]["content"]

    chat_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply

def generate_vision_content(image_path, prompt="What do you see?"):

    with open(image_path, "rb") as img:
        base64_img = base64.b64encode(img.read()).decode()

    data = {
        "model": "llava-hf/llava-1.6-mistral-7b",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_img}"
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    return response.json()["choices"][0]["message"]["content"]