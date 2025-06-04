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
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


for i in range(190201, 190280 + 1):
    temp = f(i)
    c = 0
    for i in temp:
        if i % 2 == 0:
            c += 1
    if c == 4:
        print()
        for i in temp:
            if i % 2 == 0:
                print(i, end=" ")

