liczby = [1,2,3,4,5,6]

potegaDwojki = []

for element in liczby:
    potegaDwojki.append(element**2)

print(potegaDwojki)

liczbyparzyste = []

for element in liczby:
    if(element % 2 == 0):
        liczbyparzyste.append(element)

print(liczbyparzyste)