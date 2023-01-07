import speech_recognition as sr 
import pyttsx3
from random import choice
from config import *

reproducao = pyttsx3.init()


def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():
    print("Oi, qual é seu nome completo?")
    sai_som("Oi, qual é seu nome completo?")
    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:

                try:
                    
                    audio = rec.listen(s)

                    user_name = rec.recognize_google(audio, language="pt")
                    user_name = verifica_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verifica_nome_existe(user_name))
                    print(apresentacao)
                    sai_som(apresentacao)

                    brute_user_name = user_name
                    user_name = user_name.split("")
                    user_name = user_name[0]
                    break

                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)

            break           

    print("="* len(apresentacao))
    print("Ouvindo...")

    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:

                try:
                    
                    audio = rec.listen(s)

                    entrada = rec.recognize_google(audio, language="pt")
                    print("{}: {}".format(user_name, entrada))

                    resposta = conversas[entrada]

                    print("Assistente: {}".format(resposta))
                    sai_som("{}".format(resposta))

                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)





if __name__ == '__main__':
    intro()
    sai_som("Iniciando")
    assistente()



