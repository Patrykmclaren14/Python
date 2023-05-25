import time

def function_performance(func, how_many_times = 1, **arg):
    
    sum = 0
    print(arg.get("wartosc"))
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setConteiner = {i for i in range(1000)}
listConteiner = [i for i in range(1000)]

def czy_znajduje_sie_w(wartosc, conteiner):
    if wartosc in conteiner:
        return True
    else:
        return False

print(function_performance(czy_znajduje_sie_w, how_many_times=1, wartosc=2, conteiner = setConteiner ))
print(function_performance(czy_znajduje_sie_w, how_many_times=1, wartosc=2, conteiner = listConteiner ))

