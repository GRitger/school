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


for i in range(99999, 1048571 + 1):
    temp = p(i)
    l = int(math.log(i, 2))
    if temp and (abs(2 ** l - i) <= 5 or abs(2 ** (l+1) - i) <= 5):
        print(i, 2 ** l)

