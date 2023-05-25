import time

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setConteiner = {i for i in range(1000)}
listConteiner = [i for i in range(1000)]

def czy_znajduje_sie_w_zbiorze(x):
    if x in setConteiner and listConteiner:
        return True
    else:
        return False

def czy_znajduje_sie_w_liscie(x):
    if x in setConteiner and listConteiner:
        return True
    else:
        return False


print(czy_znajduje_sie_w_zbiorze(999))

print(function_performance(czy_znajduje_sie_w_zbiorze,500, how_many_times=50000))

print(czy_znajduje_sie_w_liscie(999))

print(function_performance(czy_znajduje_sie_w_liscie,500, how_many_times=50000))

