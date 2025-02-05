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


col = 0
for i in range(1000893530, 2000000000, 7 * 13 * 17 * 23 * 29):
    if i % 3 != 0 and i % 5 != 0:
        temp = f(i)
        c = 0
        for j in temp:
            if j % 2 == 1:
                c += 1
        if c > 100:
            col += 1
print(col)
