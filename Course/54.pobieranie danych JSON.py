import requests
import json


r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print('niepoprawny format')
else:
    print('wszysko okej')
    print(tasks[:10])

