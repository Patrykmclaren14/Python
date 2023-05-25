import math

def palindromy(slowo):
    if slowo == slowo[::-1]:
        return print('podane slowo "'+slowo+'" jest palindormem')
    else: return print('podane slowo "'+slowo+'" nie jest palindormem')

palindromy('oko')


def dzielniki(liczba):
    for x in range(1,liczba+1):
        if liczba%x == 0:
            print(liczba/x)
        else:None


def liczby_pierwsze(liczba):
    dzielnik = 0
    for x in range(1,liczba+1):
        if liczba%x == 0:
            dzielnik +=1
    if(dzielnik>2):
        print('liczba zlonona')
    else: print('liczba pierwsza')

liczby_p = []
liczby_z = []
 
def funkcja_kwadratowa(liczba1,liczba2,znak):
    wzor = 0
    if znak == '+' or 'suma' or 'dodawanie':
        wzor = str(liczba1**2)+'x^2' +'+'+ str(2 * liczba1 *liczba2)+'x' + '+'+str(liczba2**2)
    if znak == '-' or 'roznica' or 'odejmowanie':
        wzor = str(liczba1**2)+'x^2' +'-'+ str(2 * liczba1 *liczba2)+'x' + '+'+str(liczba2**2)

    print(wzor)

funkcja_kwadratowa(2,4,'-')


def silnia(liczba):
    suma = 1
    for x in range(1,liczba+1):
        suma *= x
    return suma

print(silnia(4))

s2 = 1
suma = 0

n = 5
wynik = 2
suma=0
for x in range(0,n):
    wynik = wynik*10+2
    suma += wynik
print(suma)


x = 0
while x<5:
    x+=1
    print('*'*x)

x = 5
while x>1:
    x-=1
    print('*'*x)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
lista3 = []
for x in range(0,len(list1)):
    lista3.append(list1[x]+list2[x])

print(lista3)

numbers = [1, 2, 3, 4, 5, 6, 7]
result = []
for x in range(0,len(numbers)):
    result.append(numbers[x]**2)

print(result)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

listresult = []

for x in range(0,len(list1)):
    listresult.append(list1[0]+list2[x])
    listresult.append(list1[1]+list2[x])
print(listresult)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)

print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)

list1[index] = 200

print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)

print(list1)