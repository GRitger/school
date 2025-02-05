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
x = 1273548
while n < 5:
    temp = f(x)
    M = 0
    if len(temp):
        M = temp[0] + temp[-1]
    if p(M % 100000):
        print(x, M)
        n += 1
    x += 1

