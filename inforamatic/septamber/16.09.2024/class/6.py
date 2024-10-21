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


ans = 0
ma = -1000000000000000000000000000
for i in range(1686, 13276 + 1):
    s = 0
    f = True
    x = i
    while x:
        if (x % 10) % 2 == 0:
            f = False
            break
        x //= 10
    if f:
        while i:
            ans += i % 10
            i //= 10
print(ans)
