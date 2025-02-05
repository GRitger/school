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
for i in range(250000, 10000000000000000 + 1):
    temp = f(i)
    s = 0
    for j in temp:
        if p(j) and j != i:
            s += j
    if s and s % 17 == 0:
        print(i, s)
        ans +=1
    if ans > 5:
        break
