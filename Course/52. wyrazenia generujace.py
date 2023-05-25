liczby = []

for i in range(2,470):
    if (i%7==0):
        if(not(i%5==0)):
            liczby.append(i)

print(liczby)


