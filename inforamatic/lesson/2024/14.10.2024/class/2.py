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

a = []
for i in range(3, 1000):
    if d(i):
        for j in range(10000):
            if 35000000 <= i**4 * 2**j <= 100000000:
                a.append([i**4 * 2**j, i**4])
a.sort()
print(*a)