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
    return a


n = 0
ch = 350000

while n < 6:
    m = 0
    ch += 1
    t = f(ch)
    if len(t) != 0:
        m = t[0] + t[-1]

    if m and m % 23 == 9:
        n += 1
        print(ch, m)
