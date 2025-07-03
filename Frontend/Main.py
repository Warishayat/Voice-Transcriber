import streamlit as st
from Speech_Recognizer import record_audio
from Transcriber import transcribe_text
import os

# Streamlit page config
st.set_page_config(page_title="🎙️ Voice to Text", layout="centered")
st.title("🧠 CareCloud - AI Voice Transcriber")
st.markdown("Record your voice and get it transcribed using AI.")

# Path to save audio file
save_path = "Speech_recognizer.mp3"

# Recording duration selector (5–60 seconds)
phrase_time_limit = st.slider(
    "🎛️ Select how long you want to speak (seconds)",
    min_value=5,
    max_value=60,
    value=15
)

# Button to start recording and transcribing
if st.button("🎤 Record & Transcribe"):
    # Step 1: Record the user's voice
    with st.spinner("🎙️ Recording... please speak now!"):
        record_audio(file_path=save_path, timeout=30, phrase_time_limit=phrase_time_limit)
        st.success("✅ Recording complete!")

    # Step 2: Transcribe the audio using Groq Whisper
    with st.spinner("🧠 Transcribing your voice..."):
        try:
            result = transcribe_text(save_path)
            st.subheader("📝 Transcribed Text:")
            st.write(result)

            # Step 3: Show download button for MP3
            if os.path.exists(save_path):
                with open(save_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download MP3",
                        data=f,
                        file_name="transcription.mp3",
                        mime="audio/mp3"
                    )
        except Exception as e:
            st.error(f"❌ An error occurred during transcription:\n{str(e)}")
