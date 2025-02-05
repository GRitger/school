def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    a = []
    d = 1
    while d * d < x:
        if x % d == 0:
            a.append(x // d - d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


def d(x):
    a = []
    d = 1
    while d * d < x:
        if x % d == 0:
            if x // d - d <= 90:
                a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


ans = 0
for i in range(500000, 1000000 + 1):
    temp = f(i)
    c = 0
    for j in temp:
        if j <= 90:
            c += 1
    if c >= 3:
        qwe = d(i)
        print(i, qwe[-1])
