import requests
import json

# Чтение API-ключа из файла config.json
with open('config.json') as config_file:
    config = json.load(config_file)
    API_KEY = config['api_key']

# Функция, работающая с Google Translate API
def google_translate(text, source_language="ru", target_language="en"):
    URL = "https://google-translator9.p.rapidapi.com/v2"
    payload = {
	    "q": text,
	    "source": source_language,
	    "target": target_language,
	    "format": "text"
    }
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "google-translator9.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(URL, json=payload, headers=headers)
    return response.json()["data"]["translations"][0]["translatedText"]

# Функция, работающая с Albit Translator API
def albit_translator(text, from_language="ru", to_language="en"):
    URL = "https://aibit-translator.p.rapidapi.com/api/v1/translator/text"
    payload = {
        "from": from_language,
        "to": to_language,
        "text": text
    }
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "aibit-translator.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(URL, json=payload, headers=headers)
    return response.json()["trans"]



