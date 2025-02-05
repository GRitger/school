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


ch = 200000000
n = 0
while n < 5:
    ch += 1
    temp = f(ch)
    if len(temp) >= 5:
        s = temp[0] * temp[1] * temp[2] * temp[3] * temp[4]
        if s < ch:
            n += 1
            print(s, ch)
