# next-gen-multi-modal-AI-chatbot-AstraMind
visit Steamlit for more details:-- https://next-gen-multi-modal-ai-chatbot-astramind-s46fdq8b7br4w5kbttvc.streamlit.app/
🤖 AstraMind – Your Multimodal AI Assistant

AstraMind is a next-generation, multimodal AI assistant built with Streamlit that integrates multiple advanced AI models like OpenAI, Gemini, Groq, and Pollinations.
It enables users to chat, generate images, analyze images, and even interact through voice, all in one seamless interface.

🌟 Features
Mode	Description
💬 Text Chat	Talk to AstraMind using text — supports OpenAI, Gemini, and Groq models.
🖼️ Image Generation	Generate stunning images using the Pollinations API.
🖼️ Image Q&A	Upload an image and ask AstraMind questions about it using Gemini Vision.
🎙️ Voice Chat	Speak to AstraMind! Upload voice files for real-time transcription and AI responses.
🌐 Multi-language Support	Communicate in English, Hindi, French, or Spanish.
🧠 Tech Stack
Component	Technology
Frontend	Streamlit

AI APIs	OpenAI, Gemini, Groq, Pollinations
Voice Recognition	SpeechRecognition (Google Speech API)
Environment Management	python-dotenv
Image Handling	Pillow (PIL)
Language Handling	Multi-language prompt formatting
🗂️ Project Structure
AstraMind/
│
├── app.py                           # Main Streamlit app
│
├── models/
│   ├── openai_model.py              # Handles OpenAI text chat
│   ├── gemini_model.py              # Handles Gemini text chat
│   ├── pollination_model.py         # Handles image generation
│   ├── groq_model.py                # Handles Groq AI responses
│   ├── image_qa_model.py            # Handles image-based Q&A with Gemini
│   ├── voice_model.py               # Handles voice input (speech recognition)
│
├── .env                             # API keys and environment variables
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation

⚙️ Setup & Installation

Follow these steps to run AstraMind locally 👇

1️⃣ Clone the Repository
git clone https://github.com/your-username/AstraMind.git
cd AstraMind

2️⃣ Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the root directory and add your API keys:

OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key

🚀 Run the App

Start the Streamlit app with:

streamlit run app.py

🧩 How to Use

Launch AstraMind — the Streamlit interface will open in your browser.

Select a Mode from the sidebar:

💬 Text Chat – interact with OpenAI, Gemini, or Groq.

🖼️ Image Generation – describe an image to generate.

🖼️ Image Q&A – upload an image and ask about it.

🎙️ Voice Chat – upload a voice file and get AI replies.

Choose Language — supports English, Hindi, French, and Spanish.

Enjoy Your AI Assistant!

🧰 Requirements

Python ≥ 3.10

Streamlit ≥ 1.32

Requests, Pillow, SpeechRecognition

google-generativeai, python-dotenv

💡 Future Enhancements

🔊 Real-time microphone input

🧩 Model benchmarking and analytics

☁️ Persistent chat memory and export
