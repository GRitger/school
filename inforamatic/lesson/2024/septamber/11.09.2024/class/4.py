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
for i in range(33333, 55555 + 1):
    temp = f(i)
    s = 0
    for j in temp:
        if p(j) and j != i:
            s += j
    if s > 250 and i % s == 0:
        print(i, s)
