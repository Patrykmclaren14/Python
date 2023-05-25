
def checker(year):
    if year % 4 == 0:
        print('Leap year')
    else:
        print('Not leap year')


for year in range(2004, 2025):
    print(year)
    checker(year)
