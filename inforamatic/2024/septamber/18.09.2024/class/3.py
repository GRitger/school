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
ch = 550000

while n < 5:
    F = 0
    ch += 1
    t = f(ch)
    if len(t):
        F = int(sum(t) // len(t))
    if F % 31 == 13:
        print(ch, F)
        n += 1