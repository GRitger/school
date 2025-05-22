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
    d = 1
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
x = 700001
while n < 5:
    temp = f(x)
    for i in temp:
        if i % 10 == 7 and i != 7:
            print(x, i)
            n += 1
            break
    x += 1