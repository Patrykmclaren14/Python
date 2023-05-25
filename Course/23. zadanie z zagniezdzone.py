#dodaj nowe definicje
#szukaj istniejace definicje
#usuwaj istniejace definicje

definicje = {23: 'czaja',
             48: 'marcin',}  #def ={klucz, definicja}
        
print(definicje)

while(True):
    a = int(input("Jesli chcesz dodac cos do tego slownika podaj - 1 jesli chcesz usunac - 2, jesli chcesz cos z niego wyszukac - 3:"))

    if(a==1):
        klucz = input("podaj klucz do zdefiniowania: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz]=definicja   
        print(definicje)
    elif(a==2):
        klucz = int(input("podaj klucz zeby usunac definicje: "))
        if klucz in definicje:
            del definicje[klucz]
            print(definicje)
    elif(a==3):
        klucz = int(input("czego szukasz: "))
        if klucz in definicje:
            print(definicje[klucz])
    else: break
        
    

