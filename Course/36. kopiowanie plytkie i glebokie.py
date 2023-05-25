def evil_function(lista):
    lista[0] = 4
    print(lista)

myList = [1,4,2,1,52,3]

evil_function(myList.copy()) #jak zrobimy kopie id sie zmienia chodz wartosc jest taka sama
                             #lecz jak sie odwolamy do konkretej wartosci id bedzie takie samo