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


ch = 450000
n = 0
while n < 7:
    ch += 1
    temp = f(ch)
    s = 0
    minp = 0
    maxp = 0
    for j in temp:
        if d(j) and minp == 0:
            minp = j
        if d(j):
            maxp = j
    s = maxp - minp
    if s % 29 == 11:
        print(ch, s)
        n += 1

