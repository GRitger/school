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
ch = 600000

while n < 6:
    m = 0
    ch += 1
    if ch % 6 == 0 and p(ch + 1) and p(ch - 1):
        print(ch + 1, ch - 1)
        n += 1
