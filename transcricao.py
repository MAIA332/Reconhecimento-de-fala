from pydub import AudioSegment
from pydub.silence import split_on_silence

sr = __import__("speech_recognition")

def recognize_speech(audio_path):
    # Inicializa o reconhecimento
    recognizer = sr.Recognizer()

    # carrega o audio
    audio_file = AudioSegment.from_wav(audio_path)

    # Divide pelo silencio
    chunks = split_on_silence(audio_file, silence_thresh=-40) 

    # Reconhece para cada "chunck"
    text = ""
    for chunk in chunks:
        with sr.AudioFile(chunk.export(format="wav")) as source:
            audio_data = recognizer.record(source)
            try:
                chunk_text = recognizer.recognize_google(audio_data, language="pt-BR")
                text += chunk_text + " "
            except Exception as e:
                print(f"Não foi possível identificar: {e}")

    return text.strip()

""" audio_path = "Gravando.wav"
recognize_speech(audio_path) """
