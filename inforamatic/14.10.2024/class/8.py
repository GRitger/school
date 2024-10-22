from itertools import product


def d(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    d = 1
    a = []
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


def q(a):
    s = 0
    while a:
        s += a % 10
        a //= 10
    return s

for k in range(15):
    for i in product("0123456789", repeat=k):
        i = "".join(i)
        if d(q(i)):
            pass

