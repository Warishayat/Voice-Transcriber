# from dotenv import load_dotenv
# import logging
# import os
# import warnings
# import speech_recognition as sr
# from pydub import AudioSegment
# from io import BytesIO
# warnings.filterwarnings("ignore")

# load_dotenv()
# # to check ffmpg path exit or not.
# ffmpeg_path = os.getenv("FFMPEG_PATH")

# AudioSegment.converter = "ffmpeg"



# #saves logs
# logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')


# #Recognize and save audio
# def record_audio(file_path,timeout=20, phrase_time_limit=None):
#     """
#     Record audio from the microphone and save it as an MP3 file.

#     Args:
#         file_path (str): Path to save the recorded audio file.
#         timeout (int): Max time to wait for speech to start (in seconds).
#         phrase_time_limit (int or None): Max length of the speech (in seconds).
#     """
#     voice_recognizer = sr.Recognizer()

#     try:
#         with sr.Microphone() as source:
#             logging.info("Adjust for ambient noise......")
#             voice_recognizer.adjust_for_ambient_noise(source, duration=1)
#             logging.info("Start speaking now.......")
#             audio_data = voice_recognizer.listen(source=source,timeout=timeout,phrase_time_limit=phrase_time_limit)
#             logging.info("Recording is complete....")

#             # convert the data intp mp3 formate
#             wav_data = audio_data.get_wav_data()
#             audio_Segment = AudioSegment.from_wav(BytesIO(wav_data))
#             audio_Segment.export(file_path, format="mp3", bitrate="128k")
#             print(f'your output is saved at {file_path}')

#     except Exception as e:
#         logging.error(f"An error occurred: {e}")


# if __name__ == "__main__":
#     file_path = "speech_recognize.mp3"
#     record_audio(file_path=file_path)
