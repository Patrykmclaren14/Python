def generate_even_numbers():
    print('start')
    for element in  range(400):
        print('przed yield')
        if element % 2 == 0:    
            yield element
            print('po yield')
    
a = generate_even_numbers()

print(next(a))
print(next(a))
print(next(a))
print(next(a))

def genearte_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1 

print(list(genearte_10_numbers()))

