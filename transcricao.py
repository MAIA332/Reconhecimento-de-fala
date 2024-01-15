from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import speech_recognition as sr

def ogg2wav(ofn):
    wfn = ofn.replace('.ogg', '.wav')
    try:
        x = AudioSegment.from_file(ofn, format="ogg")  # Specify the format parameter
    except Exception as e:
        print("deu ruim")
    x.export(wfn, format='wav')

def recognize_speech(audio_path):
    if not os.path.exists(audio_path):
        print(f"Error: File not found - {audio_path}")
        return ""

    recognizer = sr.Recognizer()

    # Load the audio with the correct format parameter
    try:
        audio_file = AudioSegment.from_file(audio_path, format="ogg")
    except Exception as e:
        print(f"deu ruim {e}")

    # Split on silence
    chunks = split_on_silence(audio_file, silence_thresh=-40)

    text = ""
    for i, chunk in enumerate(chunks):
        # Export each chunk to WAV
        chunk.export(f"chunk_{i}.wav", format="wav")

        with sr.AudioFile(f"chunk_{i}.wav") as source:
            audio_data = recognizer.record(source)
            try:
                chunk_text = recognizer.recognize_google(audio_data, language="pt-BR")
                text += chunk_text + " "
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    return text.strip()