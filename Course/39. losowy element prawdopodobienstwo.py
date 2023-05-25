"""
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości

"""

from itertools import count
import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia", "losowa rzecz"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

print(random.choice(movieList))
print(random.choices(nagrodaZeSkrzynki, k = 10)) # zwraca liste

from collections import Counter

print(Counter(random.choices(nagrodaZeSkrzynki, weights=[80,15,4,1], k = 100 )))
