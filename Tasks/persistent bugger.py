def persistance(n):
    multiplication = 1
    n = str(n)
    for x in range(0,len(n)):
        multiplication *= int(n[x])
    print(multiplication)
    n = str(multiplication)
    choice(n)

def choice(x):
    x = int(x)
    if x > 9:
        z= persistance(x)
    else: z= 0
    
         
   


print(choice(999))