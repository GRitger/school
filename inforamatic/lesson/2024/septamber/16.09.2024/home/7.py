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


ans = 0
m = -1000000000000000000000000
for i in range(450000, 10 ** 10):
    t = f(i)
    for j in t:
        if p(j):
            m = max(j, m)
    if len(t) != 0:
        print(i, m - t[0])
        ans += 1
    if ans == 4:
        break
