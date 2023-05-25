imiona = ["Arek", "Kuba", "Karol", "Adrian"]
liczby = [1,54,-2,20]

print("Arek" in imiona)
print("Marcel" in imiona) #false

if("Arek" in imiona):
    print("czesc Arek")

if(2 not in liczby):
    print("Nie ma liczby 2")

print(3* liczby) # kazda liczba wyswietli sie 3 razy

print([4,2] + liczby) # dodajemy 2 listy do siebie

print(liczby)

liczby = [4,20,30] + liczby #dodaje liste do pierwotnej listy dodajac nowe wartosci
print(liczby)