import json
import requests
import pprint
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days=7)
searchDate = datetime.today() - timeBefore

params = {
    'site':'stackoverflow',
    'sort':'votes',
    'order':'desc',
    'fromdate':int(searchDate.timestamp()),
    'tagged':'python',
    'min':15
}

r = requests.get('https://api.stackexchange.com/2.2/questions/', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('niepoprawny format')
else:
    for question in questions['items']:
        print(question['link'])
        webbrowser.open_new_tab(question['link'])
      