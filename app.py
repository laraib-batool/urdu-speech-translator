import streamlit as st
import speech_recognition as sr
from googletrans import Translator

# Streamlit page setup
st.set_page_config(page_title="Urdu to English Speech Translator", page_icon="🎤", layout="centered")

st.title("🎤 Urdu → English Speech Translator")
st.write("Speak in **Urdu**, and I will translate it into **English** for you!")

# Translator object
translator = Translator()

# Function to capture and translate speech
def recognize_and_translate():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎙 Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        st.success("✅ Speech captured! Processing...")
        with st.spinner("Processing audio..."):
    # do recognition + translation
        urdu_text = recognizer.recognize_google(audio, language="ur-PK")
        st.write(f"**You said (Urdu):** {urdu_text}")

        translation = translator.translate(urdu_text, src="ur", dest="en")
        st.write(f"**English Translation:** {translation.text}")

    except sr.UnknownValueError:
        st.error("Sorry, I could not understand the audio.")
    except sr.RequestError:
        st.error("Network error. Please check your connection.")

# Button to trigger recognition
if st.button("🎤 Start Recording"):
    recognize_and_translate()

st.markdown("---")
st.caption("Built with Python, Streamlit, and Google Translate API")





