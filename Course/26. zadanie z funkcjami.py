import math

print("Wybierz powierzchnie figury ktora chcesz obliczyc")

a = int(input("1 - kwadrat, 2 - prostokat, 3 - trojkat, 4 - trapez, 5 - kolo:"))

if(a==5 or a==1):
    b = float(input("podaj wartosc:"))
elif(a==4):
    h = float(input("podaj wysokosc:"))
    b = float(input("podaj podstawe:"))
    c = float(input("podaj druga podstawe:"))
elif(a==2 or 3):
    b = float(input("podaj wartosc:"))
    c = float(input("podaj druga wartosc:"))
else: 
    print("blad")

def pole_kwadratu(b):
    return(b*b)

def pole_prostokata(b,c):
    return b*c

def pole_trojkata(b,c):
    return b*c*0.5

def pole_trapzeu(b,c,h):
    return (b+c)*h/2

def pole_kola(b):
    return math.pi*b**2

if(a==1):
    print(pole_kwadratu(b))
elif(a==2):
    print(pole_prostokata(a,b))
elif(a==3):
    print(pole_trojkata(a,b))
elif(a==4):
    print(pole_trapzeu(a,b,h))
if(a==5):
    print(pole_kola(b))