import requests
import wikipedia
import pywhatkit as kit


def find_my_ip():
    ip_adress = requests.get('https://api.ipify.org?format=json').json()
    return ip_adress["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)
