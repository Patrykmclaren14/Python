wynik = 0

i = 0

while i<3:
    x = int(input("Podaj liczbe parzysta: "))
   
    if(x%2 == 0):
        wynik += x      
    else:
        print("Liczba nie jest parzysta, sproboj jeszcze raz:")
        continue
    print("Wynik dodawania =",wynik)
    i+=1
    