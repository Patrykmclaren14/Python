

tab = [1, 1]

suma = 0
for x in range(0, 8):
    suma = tab[x] + tab[x+1]
    tab.append(suma)

print(tab)
