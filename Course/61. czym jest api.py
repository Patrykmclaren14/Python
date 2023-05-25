import json
import requests
import pprint

params = {
    'site':'stackoverflow',
    'sort':'votes',
    'order':'desc',
    'fromdate':'2022-12-24',
    'tagged':'python',
    'min':'15'
}

r = requests.get('https://api.stackexchange.com/2.2/questions/', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('niepoprawny format')
else:
    pprint.pprint(questions)