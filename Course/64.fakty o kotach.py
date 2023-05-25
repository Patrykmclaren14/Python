import requests
import json
import webbrowser
from pprint import pprint

params = {
            "api_key" : '87e55dd682158d784a346926652fdeda5f72e8d5',
            'country' : 'us',
            'year': 2023,
            'month': 'february'
}



r = requests.get('  ', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('niepoprawny format')
else:
    pprint(questions)