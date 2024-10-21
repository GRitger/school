def p(x):
    if x == 1 or x == 0:
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
ch = 1273547

while n < 5:
    ch += 1
    temp = f(ch)
    m = sum(temp)

    if p(m % 100000):
        print(ch, m)
        n += 1
