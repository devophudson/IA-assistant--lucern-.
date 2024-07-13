import requests
from decouple import config
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib


EMAIL = ""
PASSWORD = ""


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


def send_email(receiver_add,subject,message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From']= EMAIL

        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True

    except Exception as e:
        print(e)
        return False


def get_news():
    try:
        # Obter a chave da API de notícias do ambiente
        api_key = config('NEWS_API_KEY')

        # Configurações da News API para buscar notícias no Brasil
        endpoint = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': 'br',  # Alterado para 'br' para buscar notícias do Brasil
            'apiKey': api_key
        }

        # Faz a requisição GET para a API de notícias
        response = requests.get(endpoint, params=params)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Converte a resposta para JSON
            data = response.json()

            # Verifica se a chave 'articles' está presente nos dados
            if 'articles' in data:
                articles = data['articles']
                # Extrai apenas os títulos dos artigos
                headlines = [article['title'] for article in articles]
                return headlines  # Retorna uma lista de títulos de artigos

            else:
                print("Não foram encontrados artigos de notícias.")
                return []  # Retorna uma lista vazia se 'articles' não estiver presente

        else:
            print(f"Erro ao consultar API de notícias: {response.status_code}")
            return []  # Retorna uma lista vazia em caso de erro na requisição

    except Exception as e:
        print(f"Erro ao obter notícias: {str(e)}")
        return []  # Retorna uma lista vazia em caso de erro geral
