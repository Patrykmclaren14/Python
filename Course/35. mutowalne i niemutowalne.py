a = 4

listSample = [1, 4 ,512, 24]

listSample2 = listSample

listSample2.append(454)

print(listSample)

print(listSample2)

a=4

b=a

b=7

print(b)
print(a)

k=4
c=4 #id k i c jest takie samo poniewaz wartosc jest taka sama
    #czyli obiekty sa takie same
c=4
c=10 #id sie zmienia poniewaz wartosc sie zmienila





def dodaj_element(lista,element):
    print(id(lista))
    lista.append(element)
    print(id(lista))      #zmienna w funkcji jest wiszaca w powietrzu i jej id sie nie zmienia
                          #poniewaz zostala dopiero co wytworzona (nie bylo jej wczesniej)

print(dodaj_element(listSample,5)) 
