from functools import lru_cache

@lru_cache(None)
def f(x, m):
    if x <= 90:
        return m %2 == 0
    if m == 0:
        return False
    h = [f(x - 11, m -1), f(x // 3, m-1)]
    if m % 2:
        return any(h)
    else:
        return all(h)

for i in range(91, 5001):
    if f(i, 3) and not(f(i, 1)):
        print(i)