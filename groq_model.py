# models/groq_model.py
import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"  # replace with actual Groq endpoint

def chat_groq(prompt, language="English"):
    """
    Send prompt to Groq and return text response.
    Supports multi-language.
    """
    prompt_with_lang = f"[{language}] {prompt}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "groq-text-1",
        "prompt": prompt_with_lang,
        "language": language
    }

    try:
        response = requests.post(BASE_URL, json=payload, headers=headers)
        data = response.json()
        return data.get("text", "⚠️ No response from Groq")
    except Exception as e:
        return f"⚠️ Groq Error: {str(e)}"

