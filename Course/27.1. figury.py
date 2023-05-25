import figury
from enum import IntEnum

Menu_Figury = IntEnum("Menu_Figury",'Kwadrat Prostokat Trapez Kolo trojkat')

wybor = int(input("""Wybierz figure ktora ccesz obliczyc:
1. kwadrat
2. prostokat
3. trojkat
4. trapez
5. kolo
"""))

if(wybor == Menu_Figury.Kwadrat):
    a = float(input("Podaj bok kwadratu: "))
    print(figury.pole_kwadratu(a))

elif(wybor == Menu_Figury.Prostokat):
    a = float(input("Podaj bok prostokata: "))
    b = float(input("Podaj drugi bok prostokata: "))
    print(figury.pole_prostokata(a,b))

elif(wybor == Menu_Figury.trojkat):
    a = float(input("Podaj podstawe trojkata: "))
    h = float(input("Podaj wysokosc trojkata: "))
    print(figury.pole_trojkata(a,h))

elif(wybor == Menu_Figury.Trapez):
    a = float(input("Podaj podstawe trapezu: "))
    b = float(input("Podaj druga podstawe trapezu: "))
    h = float(input("Podaj wysokosc trapezu: "))
    print(figury.pole_trapezu(a,b,h))

elif(wybor == Menu_Figury.Kolo):
    r = float(input("Podaj promien kola: "))
    print(figury.pole_kola(r))

