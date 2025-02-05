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

while n < 7:
    ch -= 1
    s = 0
    temp = f(ch)
    for i in temp:
        if p(i):
            s += i
    if s and s % 10 == 0:
        print(ch, s)
        n += 1
