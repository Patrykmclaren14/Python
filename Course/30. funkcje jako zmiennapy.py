import time

def sumuj_do (liczba):
    suma = 0

    for liczba in range(1,liczba+1):
        suma = suma + liczba
    
    return suma

def sumuj_do2 (liczba):
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3 (liczba):
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4 (liczba):
    return sum((liczba for liczba in range(1,liczba+1)))

def sumuj_do5 (liczba):
   return (1 + liczba)/2 * liczba

def finish_timer(start):
    end = time.perf_counter()
    return end - start



#funkcja jako zmienna



def function_performence(func,arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

def show_message(message):
    print(message)

print(function_performence(sumuj_do, 50000))
print(function_performence(sumuj_do2, 455555))
print(function_performence(sumuj_do3, 23443))
print(function_performence(sumuj_do4, 123))
print(function_performence(sumuj_do5, 4234))

def funkcja1(czaja):
    for czaja in range(1,czaja+1):
        print(czaja)

def funkcja2(x,y):
    x(y)
    return print("zrobione")
    

funkcja1(8)