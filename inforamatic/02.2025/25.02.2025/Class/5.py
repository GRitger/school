from functools import lru_cache


@lru_cache(None)
def f(x, m, hod=0):
    if 62  <= x: return m % 2 == 0
    if m == 0:
        return False
    h = []
    if hod == 1:
        h.append(f(x + 2, m - 1, 2))
        h.append(f(x * 3, m - 1, 3))
    elif hod == 2:
        h.append(f(x + 1, m - 1, 1))
        h.append(f(x * 3, m - 1, 3))
    elif hod == 3:
        h.append(f(x + 2, m - 1, 2))
        h.append(f(x + 1, m - 1, 1))
    else:
        h.append(f(x + 2, m - 1, 2))
        h.append(f(x + 1, m - 1, 1))
        h.append(f(x * 3, m - 1, 3))

    if m % 2 != 0:
        return any(h)
    else:
        return all(h)


for i in range(1, 62):
    if f(i, 4) and not(f(i,2)):
        print(i)
