import random

a = random.randint(1, 5)

for i in range(1,100000):
    b = int(input("Podaj liczbe:"))
    if(a == b):
        print("Gratulacje zgadles")
        break
    elif(a<b):
        print("Liczba jest wieksza od zgadywanej liczby")
        continue
    elif(a>b):
        print("Liczba jest mniejsza od zgadywanej liczby")
        continue

