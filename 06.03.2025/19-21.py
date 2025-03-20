from functools import lru_cache


@lru_cache(None)
def f(x, y, m):
    if x + y >= 449:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x + 1, y, m - 1), f(x * 2, y, m - 1), f(x, y + 1, m - 1), f(x, y * 2, m - 1)]
    if m % 2:
        return any(h)
    else:
        return all(h)


for i in range(1, 436):
    if f(i, 11, 4) and not (f(i, 11, 2) ):
        print(i, end=" ")
