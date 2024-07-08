import keyboard
from online import find_my_ip, search_on_google,search_on_wikipedia,youtube
import pyttsx3
import os
import subprocess as sp
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from conv import random_text  # Importar se necessário


# Inicialização do pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)

# Verificar vozes disponíveis
voices = engine.getProperty('voices')
for voice in voices:
    print("Voz:", voice.id, " - Idioma:", voice.languages)

# Configurar voz em português, se disponível
voice_id = None
for voice in voices:
    if "portuguese" in voice.languages:
        voice_id = voice.id
        break

if voice_id:
    engine.setProperty('voice', voice_id)
    print("Voz configurada para:", voice_id)

# Captação das variáveis do ambiente
USER = config('USER')
HOSTNAME = config('BOT')

# Função para falar texto
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para cumprimentar de acordo com o horário
def greet_me():
    hour = datetime.now().hour
    if 0 <= hour < 6:
        speak(f"Boa Madrugada, {USER}")
    elif 6 <= hour < 12:
        speak(f"Bom Dia, {USER}")
    elif 12 <= hour < 18:
        speak(f"Boa Tarde, {USER}")
    else:
        speak(f"Boa Noite, {USER}")
    speak(f"Eu sou {HOSTNAME}. Como posso te ajudar hoje?")

listening = False

#função para começar a ouvir
def start_listening():
    global listening
    listening = True
    print("começou a escutar ")

#função para parar de ouvir !
def pause_listening():
    global listening
    listening = False
    print("parou de ouvir")

#TODO: Teclas para inicialização da ia (começar a ouvir / parar de ouvir) !
keyboard.add_hotkey('ctrl+shift+k', start_listening)
keyboard.add_hotkey('ctrl+shift+p', pause_listening)


# Função para reconhecer comandos de voz
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR',)  # Reconhecimento em português do Brasil
        print("Você disse:", query)
        if "parar" in query or "sair" in query:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Boa noite, cuide-se!")
            else:
                speak("Tenha um bom dia, senhor!")
            exit()
        else:
            speak(choice(random_text))  # Responde com uma mensagem aleatória

    except Exception as e:
        print("Erro:", str(e))
        speak("Desculpe, não consegui entender o que você disse. Pode repetir?")
        query = 'None'

    return query.lower()

# Execução principal do programa
if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "como está você ?" in query:
                speak("Estou absolutamente bem, senhor. E você, como vai?") #TODO: Cumprimento basico

            elif "abrir prompt de comando" in query:
                speak("Abrindo o prompt de comando") #TODO: Abrir promp de comando
                os.system('start cmd')

            elif "abrir câmera" in query:
                speak("Abrindo a sua câmera frontal ")
                sp.run('start microsoft.windows.camera:', shell=True) #TODO: Abrir camera

            elif "abrir google" in query:
                speak("Abrindo o google para você senhor")
                google_path = (r"PUT YOUR DESTINY EXE APLICATION") #TODO: Abrir navegador google
                os.startfile(google_path)

            elif "abrir notepad" in query:
                speak("Abrindo o bloco de anotações !")
                notepad_path = r"PUT YOUR DESTINY EXE APLICATION"
                os.startfile(notepad_path)

            elif "abrir discord" in query:
                speak("Abrindo o discord senhor ")
                discord_path = r"PUT YOUR DESTINY EXE APLICATION"
                os.startfile(discord_path)

            elif "localizar meu endereço ip" in query:
                ip_adress = find_my_ip()
                speak(f" seu endereço ip é {ip_adress}")
                print(f" Your ip adress : {ip_adress}")

            elif "abrir youtube" in query:
                speak("Oque Você deseja ver no youtube ? ")
                video = take_command().lower()
                youtube(video)

            elif "pesquisar no google" in query:
                speak("Oque você deseja pesquisar senhor ? ")
                query = take_command().lower()
                search_on_google(query)

            elif "pesquisar no wikipédia" in query:
                speak("Oque você deseja pesquisar no wikipédia ? ")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"Esses são os resultados de acordo com a wikipédia {results}")
                speak("Estou printando agora os resultados no terminal, se você preferir olhar por lá !")
                print(results)

