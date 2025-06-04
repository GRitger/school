from functools import lru_cache


@lru_cache(None)
def f(x, m):
    if x >= 51:
        return m == 0
    if m == 0:
        return False
    if x % 2:
        h = [f(x * 3, m - 1)]
    else:
        h = [f(x + 3, m - 1), f(x + 1, m - 1)]
    if m % 2:
        return any(h)
    else:
        return all(h)


for i in range(1, 51):
    if f(i, 4):# and not f(i, 1):
        print(i)
