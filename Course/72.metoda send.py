def mnozenie():
    number = 0
    while True:
        print('start number:', number)
        number = number + 1
        sample = yield number * number
        print('po yield number:', number)
        print('po yield sample:', sample)

generatedNumbers = []
        
numberGenerator = mnozenie()

print(next(numberGenerator))
print(next(numberGenerator))
print(numberGenerator.send(40))