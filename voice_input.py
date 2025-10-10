import speech_recognition as sr
import tempfile
import streamlit as st

def get_voice_input():
    """
    Get voice input from the user using a file upload.
    Works without PyAudio.
    """
    uploaded_file = st.file_uploader("Upload your voice file", type=["wav", "mp3"])
    if uploaded_file is not None:
        try:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            # Use speech_recognition to convert to text
            recognizer = sr.Recognizer()
            with sr.AudioFile(tmp_path) as source:
                audio = recognizer.record(source)

            text = recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            return "⚠️ Could not understand audio."
        except sr.RequestError:
            return "⚠️ Google Speech Recognition service error."
        except Exception as e:
            return f"⚠️ Error: {str(e)}"

    return None
