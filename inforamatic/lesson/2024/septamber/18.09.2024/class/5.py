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
    d = 2
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


n = 0
ch = 500000

while n < 5:
    D = 0
    ch += 1
    t = f(ch)
    for i in t:
        if i % 10 == 8 and i != 8:
            print (ch, i)
            n += 1
            break

