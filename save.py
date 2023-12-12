from transcricao import recognize_speech, sr
import pyttsx3

reproducao = pyttsx3.init()


def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():
    print("Oi, qual é seu nome completo?")
    sai_som("Oi, qual é seu nome completo?")

    rec = sr.Recognizer()

    try:

        with sr.Microphone() as s:
            print("Fale agora...")
            audio_data = rec.record(s,duration=5)

            # Save the recorded audio as a WAV file
            audio_file = "Gravando2" + ".wav"
            
            with open(audio_file, "wb") as f:
                f.write(audio_data.get_wav_data())

            print(f"Salvo: {audio_file}")
            return audio_file

    except Exception as e:
        sai_som("error")
        print(f"{e}")
         


if __name__ == '__main__':
    sai_som("Iniciando")
    assistente()



