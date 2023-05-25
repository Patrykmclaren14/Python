import requests
import json
import webbrowser
from pprint import pprint

params = {

}



r = requests.get('https://api.thecatapi.com/v1/images/search/?breed_ids', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('niepoprawny format')
else:
    for quest in questions:
        webbrowser.open(quest['url'])