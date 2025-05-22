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
ch = 250156

while n < 5:
    A = 0
    ch += 1
    t = f(ch)
    m1 = 0
    m2 = 0
    for i in range(len(t) - 1, -1, -1):
        if t[i] % 2 == 1 and m2 == 0:
            m2 = t[i]
        if t[i] % 2 == 0 and m1 == 0:
            m1 = t[i]
        if m1 != 0 and m2 != 0:
            A = abs(m1 - m2)
            break

    if p(A) and A % 10 == 9:
        print(ch, A)
        n += 1
