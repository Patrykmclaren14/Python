x=0

for i in range(200):    #zrob 200 warunkow
    x+=1 #x=x+1      #liczby beda sie zwiekszac do ostatniej podanej liczby w warunku petli for
    if(i % 5 == 0 and not(i % 2 == 0)):  #jesli liczby sa podzielne przez 5 a nie sa podzielne przez 2 to je wypisz
        print(i)

    