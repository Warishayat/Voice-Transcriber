from groq import Groq
from dotenv import load_dotenv
import os
import warnings
# from Frontend.Speech_Recognizer import record_audio

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
    

# pipeline
#1: first i will record the voice through microphone
#2: as my voice input will complete the audio will save on path file.
#3: pass that voice to the transcribe_text function for transcribe the path audio file.
#4: from transcrib_text we will receive the text that will transcribe from the audio
#5: Print the response on the screen
if __name__ == "__main__":
    path = "Speech_recognizer.mp3"
    record_audio(file_path=path)
    response = transcribe_text(path)
    print("response is")
    print(response)