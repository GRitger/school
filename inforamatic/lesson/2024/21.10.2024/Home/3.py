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
    d = 2
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

ch = 700000
n  = 0
a = []
while n < 5:
    ch += 1
    t = f(ch)
    for i in t:
        if i != 7 and i % 10 == 7:
            n += 1
            print(ch, i)
            break
a.sort()

for i in a:
    print(*i)