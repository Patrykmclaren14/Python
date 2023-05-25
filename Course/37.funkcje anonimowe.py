#funkcje bez nazwy

def podwoj(x):
    return x*2

def funkcja_dla_przefiltruj(x):
    if(x%2)==0:
        return x

print(podwoj(4))

test = lambda x: x*2

print(test(4))

print((lambda x: x*2)(4))

my_list = {2,14,22,7,6,4,5,17}

przefiltrowana_lista = (list(filter(lambda x: x % 2 == 0, my_list)))
przefiltrowana_lista2 = (list(filter(funkcja_dla_przefiltruj, my_list)))
przefiltrowana_lista3 = (x for x in my_list if(x%2)==0)

print(przefiltrowana_lista)
print(przefiltrowana_lista2)
print(przefiltrowana_lista3)

