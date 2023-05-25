pokoje = {49: 'Patryk Wierzbowski', 69: 'Jakub Czaja'}
pokoje[49] = 'Jan Kowalski'
pokoje[50] = 'Jan Bednarek'

print(pokoje)

a={'imie' : 'Arkadiusz', 'nazwisko': 'Tańcula'}
print(a)

pokoje.update({400:'Jan Kowalski'}) #dodaje pokoj
print(pokoje)

del(pokoje[400]) #usuwa dany pokoj
print(pokoje)

pokoje.pop(69)
print(pokoje)

print(len(pokoje))