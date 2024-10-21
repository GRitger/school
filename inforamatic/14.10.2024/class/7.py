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


def chet(a):
    col = 0
    su = 0
    for i in a:
        if i % 2 == 0:
            col += 1
            su += i
    return col, su

a = []
for k in range(4):
    for i in product("13579", repeat=k):
        i = "".join(i)
        for j in "0123456789":
            s = int("78"+j+"56"+i+"321")
            if s % 279 == 0:
                a.append([s, s//279])
a.sort()

print(*a)