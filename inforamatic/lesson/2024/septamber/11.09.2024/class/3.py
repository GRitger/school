import math


def f(x):
    mas = []
    d = 1
    while d * d < x:
        if x % d == 0:
            mas.append(d)
            mas.append(x // d)
        d += 1
    if d * d == x:
        mas.append(d)
    mas.sort()
    return mas


def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


s = 0
ans = 0
for i in range(105673, 220784 + 1):
    d1 = 2
    while d1 * d1 < i:
        if i % d1 == 0:
            d2 = 2
            x = i // d1
            while d2 * d2 < x:
                if x % d2 == 0:
                    if p(d1) and p(d2) and p(x // d2) and d1 != d2 and d1 != x // d2:
                        s += 1
                        ans = i
                    break
                d2 += 1
            break
        d1 += 1
print(s, ans)
