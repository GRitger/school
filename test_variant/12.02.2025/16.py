import sys

from functools import lru_cache

sys.setrecursionlimit(2_000_000)


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)
for i in range(1,3001):
    f(i)

print((f(3000) // 150 + f(2999)) // f(2998))
