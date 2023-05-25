import json

encodeRetriveMovie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decoded = json.loads(encodeRetriveMovie)

print(decoded)

with open('sample.json',encoding='UTF-8') as file:
    plik = json.load(file)

print(plik)