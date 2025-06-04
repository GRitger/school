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
for i in range(3159, 31584 + 1):
    temp = p(i)
    if temp:
        qwe = i
        while qwe:
            s += qwe % 10
            qwe //= 10
print(s)
