def sum_cubes(n):
    result = 0
    for x in range(1, n+1):
        result += x ** 3
    return result


print(sum_cubes(3))
