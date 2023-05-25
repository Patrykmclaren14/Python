def mnozenie():
    number = 0
    while True:
        number = number + 1
        yield number * number

generatedNumbers = []
        
numberGenerator = mnozenie()

for _ in range(20):
    generatedNumbers.append(next(numberGenerator))

for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)