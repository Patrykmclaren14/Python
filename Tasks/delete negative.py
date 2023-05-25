arr = [-2,-3]


def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number
        else: number = 0
    return sum


print(positive_sum(arr))
