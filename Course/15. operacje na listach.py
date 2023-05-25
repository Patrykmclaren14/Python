lista1 = ["Arek", "Kuba", "Karol", "Adrian"]
lista2 = [1,54,-2,20]

print(len(lista1)) #sprawdza dlugosc listy //4 

lista2.append(4) #dodaje i zmienia zawartosc, dodal 4 do listy
print(lista2)


#lista2.append([4,2,3,1]) #dodaje nam wartosci ale tworzy nowa liste czyli liste w liscie
#print(lista2)

lista2.extend([2,12,24,2]) #dodaje nam wartosci do listy nie tworzac nowej listy
print(lista2)

lista1.insert(0, "Kuba") #mozemy dodac cos do listy w miejsce w ktore chcemy
print(lista1)

print(lista2.index(54)) #pokazuje nam na ktorej pozycji jest dana wartosc

lista2.sort(reverse = True) #od najwiekszej do najmniejszej
print(lista2)

lista2.sort(reverse = False) #od najmniejszego do najwiekszego
print(lista2)

print(max(lista2)) #najwiekszy argument
print(min(lista2)) #najmniejszy argument

print(lista2.count(54)) #ile razy argument pojawil sie w liscie //1

lista2.pop() #usuwa ostatni element z listy
print(lista2)

lista1.remove("Arek") #usunie element z listy
print(lista1)

#lista1.clear() #czysci cala liste
#print(lista1)

lista1.reverse() #zmienia kolejnosc listy
print(lista1)
