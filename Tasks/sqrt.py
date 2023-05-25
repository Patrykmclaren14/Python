from math import sqrt
from math import isqrt


def is_square(n):
    bool = False
    if n >= 0:
        if n == 0 or sqrt(n) % isqrt(n) == 0:
            bool = True
    return bool


print(is_square(0))
