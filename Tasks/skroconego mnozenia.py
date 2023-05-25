import math

def funkcja_kwadratowa(a,b,c):
    x = 0
    a*x**2+b*x+c
    delta = 0
    delta = b**2-4*a*c
    print(delta)
    if(delta>=0):
        
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a
        print(math.sqrt(delta))
        print(x1)
    else: 
        return "brak miejsc zerowych"

print(funkcja_kwadratowa(2,6,1))