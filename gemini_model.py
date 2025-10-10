import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def chat_gemini(prompt, language="English"):
    prompt_with_lang = f"[{language}] {prompt}"
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        response = model.generate_content(prompt_with_lang)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {e}"
