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
i = 550001
while n < 5:
    temp = f(i)
    F = 0
    if len(temp) > 0:
        F = int(sum(temp) / len(temp))
    if F % 31 == 13:
        print(i, F)
        n += 1
    i += 1
