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
    d = 1
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


for i in range(326496, 649632 + 1):
    temp = f(i)
    ch = 0
    nech = 0
    m = 10**100
    if len(temp) < 140:
        continue
    for j in temp:
        if j % 2 == 0:
            ch += 1
        else:
            nech += 1
        if 1000 < j < m:
            m = j
    if ch >= 70 and nech >= 70 and ch == nech:
        print(i, m)

