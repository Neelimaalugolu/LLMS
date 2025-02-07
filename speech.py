import streamlit as st
import speech_recognition as sr
import tempfile
def run():
    st.title("🗣️Speech Recognition")

    recognizer = sr.Recognizer()

    audio_file = st.file_uploader("Upload an Audio File", type=["wav", "mp3"])

    if audio_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
            temp_audio_file.write(audio_file.getbuffer())
            temp_audio_file.close()

            
            with sr.AudioFile(temp_audio_file.name) as source:
                audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data)
                st.write("Text: ", text)

                
                text_file = "converted_text.txt"
                with open(text_file, "w") as f:
                    f.write(text)

                
                with open(text_file, "rb") as f:
                    st.download_button("Download Text File", f, file_name=text_file)

            except sr.UnknownValueError:
                st.write("Sorry, could not understand the audio.")
            except sr.RequestError:
                st.write("Could not request results from Google Speech Recognition.")

