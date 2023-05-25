def pole_prostokata(a, b):
    return a*b
poleprostokataA = pole_prostokata(a=int(input("Podaj pierwszy bok:")), b=int(input("Podaj drugi bok:")))
print(5 *poleprostokataA)

def dzielenie(a,b):
    if(b == 0):
        return "Nie dziel przez 0"
    return a/b

print(dzielenie(a=int(input("Pierwsza liczba:")), b=int(input("Druga liczba:"))))