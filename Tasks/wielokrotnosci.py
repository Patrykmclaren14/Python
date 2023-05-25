def solution(number):
    sum = 0
    if number > 0:
        for x in range(0,number):
            if x % 5 == 0 or x % 3 == 0:
                sum += x
        return sum
    else: return 0


print(solution(29))