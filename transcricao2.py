import speech_recognition as sr
import subprocess

def convert_ogg_to_wav(ogg_file_path, wav_file_path):
    # Use ffmpeg to convert OGG to WAV
    subprocess.run(["ffmpeg", "-i", ogg_file_path, wav_file_path])

def transcribe_audio(audio_file_path):

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)

    try:
        # Use Google Web Speech API for transcription
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    # Specify the path to your audio file
    audio_file_path = "494Cath.wav"

    # Perform transcription
    transcription_result = transcribe_audio(audio_file_path)

    # Display the transcription result
    print("Transcription result:")
    print(transcription_result)
