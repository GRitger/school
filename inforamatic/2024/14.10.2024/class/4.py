def d(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    d = 2
    a = []
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


ch = 250200
n = 0
while n < 5:
    ch += 1
    s = 0
    temp = f(ch)
    if len(temp) >= 2:
        s = temp[-2] + temp[1]
    if s and s % 123 == 7:
        print(ch, s)
        n += 1
