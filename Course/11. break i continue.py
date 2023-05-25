#break

wynik = 0

for i in range(3):   
    x = int(input("Podaj dodatnia liczbe:"))
    if(x>0):
        wynik += x 
    else:
        print("konczymy za kare") 
        break  

print("wynik dodawania liczb to:",wynik)



#conitune

wynik = 0

for i in range(3):   
    x = int(input("Podaj dodatnia liczbe:"))
    if(x>0):
        wynik += x 
    else:
        print("Miala byc liczba dodatnia!:") 
        continue  

print("wynik dodawania liczb to:",wynik)



wynik = 0

i = 0

while i<3: 
    x = int(input("Podaj dodatnia liczbe:"))
    if(x>0):
        wynik += x 
    else:
        print("Miala byc liczba dodatnia, sproboj jeszcze raz:") 
        continue  
    i+=1

print("wynik dodawania liczb to:",wynik)

