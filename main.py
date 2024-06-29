import keyboard
import pyttsx3
import os
import subprocess as sp
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from conv import random_text  # Importar se necessário
import keyword

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
            if "how are you" in query:
                speak("Estou absolutamente bem, senhor. E você, como vai?") #TODO: Cumprimento basico

            elif "open command prompt " in query:
                speak("Abrindo o prompt de comando") #TODO: Abrir promp de comando
                os.system('start cmd')

            elif "open camera" in query:
                speak("Abrindo a camera senhor ")
                sp.run('start microsoft.windows.camera:', shell=True) #TODO: Abrir camera

            elif "open google" in query:
                speak("Abrindo o google para você senhor")
                google_path = ("C:\Program Files\Google\Chrome\Application\chrome.exe") #TODO: Abrir navegador google
                os.startfile(google_path)
