from functools import lru_cache


@lru_cache(None)
def f(x, m):
    if 42 == x: return m % 2 == 0
    if m == 0:
        return False
    h = []
    if x < 42:
        h.append(f(x + 1, m - 1))
        h.append(f(x + 3, m - 1))
        h.append(f(x + 7, m - 1))
    elif x > 42:
        h.append(f(x - 1, m - 1))
        h.append(f(x - 3, m - 1))
        h.append(f(x - 7, m - 1))
    if m % 2 != 0:
        return any(h)
    else:
        return all(h)


for i in range(1, 100):
    if f(i, 4) and not (f(i, 2)):
        print(i)
