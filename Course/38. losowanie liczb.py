#random()
'''''''''
import random

x=0
while x < 5:
    x=x+1
    print(random.uniform(0, 100))

def SzansaNaStrzal(IleMamyProcentNaStrzal):
    SzansaStrzalu = random.uniform(0,100)
    if(SzansaStrzalu<IleMamyProcentNaStrzal): #musi byc wiecej od 50 zeby stzelila
        return "hit"
    else:
        return "not hit"

print(SzansaNaStrzal(50))

x = 0

ListaStrzalow = []

while x < 100:
    x=x+1
    ListaStrzalow.append(SzansaNaStrzal(50))

print(ListaStrzalow)
print(ListaStrzalow.count("hit"))
print(ListaStrzalow.count("not hit"))

from collections import Counter

SlownikStrzalow = Counter(ListaStrzalow)

print(SlownikStrzalow)

x = 0
while x < 5:
    x=x+1
    print(random.randrange(2,100,2))

x = 0
while x < 5:
    x=x+1
    print(random.randint(10,50))
'''''''''
import random


def SzansaNaStrzal(IleMamyProcentNaStrzal):
    SzansaStrzalu = random.uniform(0,100)
    if(SzansaStrzalu<IleMamyProcentNaStrzal): #musi byc wiecej od 50 zeby stzelila
        return "hit"
    else:
        return "not hit"

x = 0

ListaStrzalow = []

while x < 100:
    x=x+1
    ListaStrzalow.append(SzansaNaStrzal(50))

print(ListaStrzalow)
print(ListaStrzalow.count("hit"))
print(ListaStrzalow.count("not hit"))
