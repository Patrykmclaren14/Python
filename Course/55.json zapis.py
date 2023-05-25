"""

json.dumps(data) - zapisuje dane do postaci Stringowej json
json.dump(data, nameOfFileHandler, ensure_ascii=False) -
                               zapisuje dane do pliku w postacji json

dump z ang. zsypać/zwalić/zrzucać
"""

import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}
print(film)
encodedFilm = json.dumps(film, ensure_ascii=False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)
"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""

