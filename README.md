# 🎙️ CareCloud Voice Transcriber

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://voice-transcriber-whisper01.streamlit.app/)

🔗 **Live App**: [Click to try it](https://voice-transcriber-whisper01.streamlit.app/)

A simple and powerful web app that records your voice from the browser and transcribes it into text using the Groq Whisper API.

---

## 🚀 Features

* 🎤 Record audio directly from your browser (no extra mic setup)
* 📄 Transcribe audio to text using Whisper-large-v3
* ⬇️ Download recorded audio as MP3
* 🌐 Fully deployable on Streamlit Cloud

---

## 📁 Project Structure

```
voice-transcriber/
├── Frontend/
│   ├── Main.py                  # Streamlit UI app
│   ├── Transcriber.py           # Transcribes audio using Groq Whisper
├── requirements.txt
├── .env                         # Environment variables (not pushed to GitHub)
├── README.md
```

---

## 📦 Requirements

**Python Libraries** (from `requirements.txt`):

```txt
streamlit
groq
python-dotenv
pydub
audio-recorder-streamlit
```

**System Dependencies** (only for Streamlit Cloud):

```bash
apt-get update && apt-get install -y ffmpeg
```

---

## 🔐 .env File Setup

Create a `.env` file with your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

For Streamlit Cloud, set this via **Secrets tab**.

---

## ▶️ Run Locally

```bash
git clone https://github.com/YourUsername/voice-transcriber.git
cd voice-transcriber
python -m venv venv
source venv/bin/activate       # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run Frontend/Main.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Deploy your app
4. In **Advanced settings > System Dependencies**, paste:

   ```bash
   apt-get update && apt-get install -y ffmpeg
   ```
5. In **Secrets**, add:

   ```
   GROQ_API_KEY=your_groq_api_key
   ```

---

## 🧠 Transcription Model

Using Groq's implementation of:

* 🔊 `whisper-large-v3`
* Language: English (`language="en"`)
* Creativity: Controlled via `temperature=0.6`

---

## 🛠 Troubleshooting

* **PyAudio error?** Use browser recorder (this app already does!)
* **FFmpeg not found?** Make sure `apt-get install ffmpeg` is set in Streamlit Cloud
* **API errors?** Check `.env` or Secrets tab for your API key

---

## 📜 License

MIT License

---

## 🙌 Credits

Built with ❤️ using:

* [Streamlit](https://streamlit.io/)
* [Groq Whisper](https://console.groq.com/)
* [audio-recorder-streamlit](https://github.com/stefanrmmr/audio-recorder-streamlit)
