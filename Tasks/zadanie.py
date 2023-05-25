import math

def silnia1(n):
    if n > 0:
        return n*silnia1(n-1)
    return 1

def silnia2(n):
    if n > 39:
        return n*silnia2(n-1)
    return 1


print(silnia1(13)*2/silnia2(52))


print(silnia2(52))


krotka1 = (1,2,3)
krotka2 = (4,5)

def czy_element_jest_w_krotce(krotka1,krotka2):
    for element in krotka1:
        for element2 in krotka2:
            if(element == element2):
                return True
            else: 
                return False
    
print(czy_element_jest_w_krotce(krotka1,krotka2))

print(__name__)




def sito(n):
    primes = [1 for x in range(n+1)]
    for i in range(2,n):
        for j in range(i+1,n):
            if j%i == 0:
                primes[j] = 0
    return primes
    
print(sito(30))