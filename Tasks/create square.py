def is_square(n):
    bool = False
    for x in range(0, n + 1):
        if x ** 2 == n:
            bool = True
            break
        else:
            bool = False
    return bool


print(is_square(230423040))
