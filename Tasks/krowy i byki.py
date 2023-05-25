import random



LiczbaDoZgadniecia = str(random.randrange(1000, 9999)) #liczbaKtoraUzytkownikMusiZgadnac
print(LiczbaDoZgadniecia)

ZlotaLiczba = list(LiczbaDoZgadniecia)

print(ZlotaLiczba)
NaszaLiczba = list(input("Podaj liczbe: "))

while ZlotaLiczba == NaszaLiczba:
    NaszaLiczba = list(input("Podaj liczbe: "))




    