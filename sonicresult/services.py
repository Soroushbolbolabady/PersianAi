import requests
from deep_translator import GoogleTranslator, MyMemoryTranslator

def translator_to_en(text):
    phrase = text
    en_translated = GoogleTranslator(source='auto', target='en').translate(text=phrase)
    return en_translated


def result(input_payload):
    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
    payload = {
        'enable_google_results': True,
        'enable_memory': False,
        'input_text': f'{input_payload}'
    }
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'X-API-KEY': '229b44c4-0529-4c42-b109-069012218932'
    }
    response = requests.post(url, json=payload, headers=headers)

    rt = response.json()
    res = rt['message']
    return res


def translator_to_fa(text):
    phrase = text
    fa_translated = GoogleTranslator(source='auto', target='persian').translate(text=phrase)
    return fa_translated


def main():
    translator_to_fa(result(translator_to_en("چشم سوم")))
