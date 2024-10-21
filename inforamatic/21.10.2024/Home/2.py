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


a=[]
for i in range(1000, 10000):
    t = f(i)
    s = sum(t)
    if s % 100 == 23:
        a.append([i, s])
a.sort()

for i in a:
    print(*i)