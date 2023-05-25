import random
from itertools import count
from collections import Counter



def Wybieranie_komnaty(WyborKomnaty):
    skrzynki = ["zielona", "pomaranczowa", "fioletowa", "zlota"]
    DobraKomnata = random.randint(1,100)
    x = 0
    wynik = 0
    b = 0
    for x in range(0,5):
        k = (random.choices(skrzynki,  weights = [75,20,4,1],)) 
        print(k)
        if k == ['zielona']:
            b = 1000
            print("Właśnie zdobyłeś skrzynie zieloną ktora zawiera 1000 zlota")
        elif k == ['pomaranczowa']:
            b = 4000
            print("Właśnie zdobyłeś skrzynie pomaranczowa ktora zawiera 4000 zlota")
        elif k == ['fioletowa']:
            b = 9000
            print("Właśnie zdobyłeś skrzynie fioletowa ktora zawiera 9000 zlota")
        elif k == ['zlota']:
            b = 160000
            print("Właśnie zdobyłeś skrzynie złotą ktora zawiera 16000 zlota")
        else: None
        
        wynik +=b
    else: print("Niestety trafiłeś na komnate w której nie ma żadnej skrzyni") 
    print("Twoja łączny wynik złota wynosi", wynik)
        
           
        


Wybieranie_komnaty(60)



               