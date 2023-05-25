wartosc = int(input("Sprawdze czy liczba jest z zakresu od 1 do 10: "))

if (wartosc > 1 and wartosc < 10): #and laczy nam warunki
    print("wartość jest w zakresie od 1 do 10")
else:
    print("wartość nie jest w zakresie od 1 do 10")

wartosc = int(input("Sprawdze czy liczba jest 3 lub 5: "))

if (wartosc == 5 or wartosc == 3): #or jesli jedno wyrazenie jest prawdziwe zwraca nam true
    print("wartość jest 3 lub 5")
else:
    print("wartość nie jest 3 lub 5")

wartosc = int(input("Sprawdze czy liczba jest 3 lub 5: "))

if (not(wartosc == 5 or wartosc == 3)): #or jesli jedno wyrazenie jest prawdziwe zwraca nam true
    print("wartość nie jest 3 lub 5")
else:
    print("wartość jest 3 lub 5")

    if(-5):
        print("sndaa")