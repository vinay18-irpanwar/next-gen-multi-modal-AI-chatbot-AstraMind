import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_openai(prompt, language="English"):
    # You can use the language argument to modify prompt or API parameters
    # For example, prepend language info to prompt:
    prompt_with_lang = f"[{language}] {prompt}"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_with_lang}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ OpenAI Error: {e}"
