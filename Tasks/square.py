def square_sum(numbers):
    sum = 0
    for x in range(0,len(numbers)):
        sum = numbers[x] ** 2 + sum
    return sum

print(square_sum([4,4]))
