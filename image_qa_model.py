import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_image(image_path, question):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        img = Image.open(image_path)

        response = model.generate_content(
            [question, img]
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error analyzing image: {str(e)}"
