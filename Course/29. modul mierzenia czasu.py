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

start = time.perf_counter()
print(sumuj_do(2893988))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(2893988))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do3(2893988))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do4(2893988))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do5(2893988))
print(finish_timer(start))
    
