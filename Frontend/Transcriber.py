from groq import Groq
from dotenv import load_dotenv
import os
import warnings
from Speech_Recognizer import record_audio

warnings.filterwarnings('ignore')


load_dotenv()
Groq_api_key = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=Groq_api_key)
def transcribe_text(file_path):
    """
    it take audio file as input and transcrie it into the text.

     Args:
        file_path (str): it take the file path as input where speech recognizer save the audio into mp3.
        Tranascribe (Text) : convert that audio into the text
    """
    with open(file_path, "rb") as recognizer_voice:
        transcribtion = client.audio.transcriptions.create(
            file=recognizer_voice,
            model = "whisper-large-v3",
            language = "en",
            temperature = 0.6, #as i will increase this temprature the model will be more creative
        )
        return transcribtion.text
    


if __name__ == "__main__":
    path = "Speech_recognizer.mp3"
    record_audio(file_path=path)
    response = transcribe_text(path)
    print("response is")
    print(response)