list = [1,2,3,4]


def multiplication(arg):
    amount = 1
    for x in range(0,len(arg)):
        amount *= arg[x]
    return amount


print(multiplication(list))