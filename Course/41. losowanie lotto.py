import random

def WybierzLosoweNumery(ilosc,wszystkiemozliwosci):

        a = (random.sample(range(wszystkiemozliwosci + 1),ilosc))
        b = (random.sample(range(wszystkiemozliwosci + 1 ),ilosc))
        if(b == a):
            return "wygrales"
        if(b != a):
            return "przegrales"

x = 0
while x < 1000:
    x+=1
    print(WybierzLosoweNumery(6,49))
