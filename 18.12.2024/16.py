from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(200000000)


@lru_cache()
def f(n):
    if n == 0:
        return 0
    if n < 10:
        return f(n - 1)
    elif n >= 10 and n % 2 == 0:
        return 3 * n - 1 + f(n - 3)
    else:
        return 5 * n +2 + f(n - 4)

print(f(4445) - f(4444))