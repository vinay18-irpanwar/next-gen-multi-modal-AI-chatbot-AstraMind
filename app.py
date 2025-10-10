import streamlit as st
from dotenv import load_dotenv
import os
from openai_model import chat_openai
from pollinations_model import generate_image_pollinations
from image_qa_model import analyze_image
from voice_input import get_voice_input
from groq_model import chat_groq
from PIL import Image

load_dotenv()

st.set_page_config(page_title="AstraMind", page_icon="🤖", layout="wide")

# --- Sidebar ---
st.sidebar.title("Settings")

# Model selection for text
text_model = st.sidebar.selectbox(
    "Choose Text Model:",
    ["OpenAI", "Gemini", "Groq"]
)

# Language selection for input and backend
language = st.sidebar.selectbox(
    "Select Language",
    ["English", "Hindi", "French", "Spanish"]
)

# Input language hint mapping
language_hint = {
    "English": "Enter your prompt:",
    "Hindi": "अपना संदेश दर्ज करें:",
    "French": "Entrez votre message :",
    "Spanish": "Ingrese su mensaje:"
}


# Model selection for image generation
image_model = st.sidebar.selectbox(
    "Choose Image Model:",
    ["Pollinations"]
)
st.title("🤖 AstraMind – Your Multimodal AI Assistant")

mode = st.sidebar.selectbox(
    "Choose a feature:",
    ["💬 Text Chat", "🖼️ Image Generation", "🖼️ Image Q&A", "🎙️ Voice Chat"]
)

# Store chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------------- TEXT CHAT ---------------
if mode == "💬 Text Chat":
    prompt = st.text_area(language_hint[language], key="text_prompt")
    if st.button("Send", key="send_btn"):
        if prompt.strip():
            if prompt.lower() == "exit":
                st.success("Exited chat.")
            else:
                if text_model == "OpenAI":
                    response = chat_openai(prompt) 
                elif text_model == "Gemini":
                    from gemini_model import chat_gemini
                    response = chat_gemini(prompt, language=language)
                elif text_model == "Groq":
                    response = chat_groq(prompt, language=language)

                # Append user and bot messages to chat history (do not display history)
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "bot", "content": response})

                st.write("### 🧠 AstraMind Says:")
                st.write(response)
        else:
            st.warning(language_hint[language])

# --------------- IMAGE GENERATION ---------------
elif mode == "🖼️ Image Generation":
    prompt = st.text_input("Enter an image description:")
    if st.button("Generate Image"):
        if prompt.strip():
            image_url = generate_image_pollinations(prompt)
            st.image(image_url, caption=prompt)
        else:
            st.warning("Please enter a description.")

# --------------- IMAGE Q&A ---------------
elif mode == "🖼️ Image Q&A":
    uploaded_img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    question = st.text_input("Ask a question about the image:")
    if st.button("Analyze Image"):
        if uploaded_img and question.strip():
            with open("temp_image.png", "wb") as f:
                f.write(uploaded_img.read())
            result = analyze_image("temp_image.png", question)
            st.image("temp_image.png", caption="Uploaded Image")
            st.write("### 🧠 Analysis Result:")
            st.write(result)
        else:
            st.warning("Please upload an image and ask a question.")

# --------------- VOICE CHAT ---------------
elif mode == "🎙️ Voice Chat":
    st.info("🎤 " + language_hint[language])
    uploaded_file = st.file_uploader("Upload your voice file", type=["wav", "mp3"])
    voice_text = None

    if uploaded_file is not None:
        import tempfile
        import speech_recognition as sr

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Recognize speech
        recognizer = sr.Recognizer()
        with sr.AudioFile(tmp_path) as source:
            audio = recognizer.record(source)
        try:
            voice_text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            voice_text = "⚠️ Could not understand audio."
        except sr.RequestError:
            voice_text = "⚠️ Google Speech Recognition service error."
        except Exception as e:
            voice_text = f"⚠️ Error: {str(e)}"

    if voice_text:
        st.write(f"🗣️ {language_hint[language]} {voice_text}")
        if "⚠️" not in voice_text:
            if text_model == "OpenAI":
                response = chat_openai(voice_text)
            elif text_model == "Gemini":
                from models.gemini_model import chat_gemini
                response = chat_gemini(voice_text, language=language)
            elif text_model == "Groq":
                response = chat_groq(voice_text, language=language)

            # Append user and bot messages to chat history (do not display history)
            st.session_state.chat_history.append({"role": "user", "content": voice_text})
            st.session_state.chat_history.append({"role": "bot", "content": response})

            st.write("### 🧠 AstraMind Says:")

            st.write(response)

