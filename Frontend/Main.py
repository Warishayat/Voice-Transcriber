import streamlit as st
from audio_recorder_streamlit import audio_recorder
from Transcriber import transcribe_text
import os
import uuid

st.set_page_config(page_title="🎙️ Voice to Text", layout="centered")
st.title("🎙️ CareCloud – Voice Recorder")

audio_bytes = audio_recorder()

if audio_bytes:
    # Save audio to a file
    os.makedirs("temp_audio", exist_ok=True)
    filename = f"temp_audio/{uuid.uuid4()}.wav"

    with open(filename, "wb") as f:
        f.write(audio_bytes)

    st.audio(audio_bytes, format="audio/wav")
    st.success("✅ Voice recorded!")

    with st.spinner("🧠 Transcribing..."):
        try:
            result = transcribe_text(filename)
            st.subheader("📝 Transcribed Text:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
