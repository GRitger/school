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
c = 0
for i in range(278932, 325396 + 1):
    d = 2
    while d * d < i:
        d2 = 2
        if i % d == 0:
            x = i // d
            while d2 * d2 < x:
                if x % d2 ==0 and p(d) and p(d2) and p(x // d2) and d != d2 and d != x // d2 and d % 10 == d2 % 10 == (x // d2) % 10:
                    c += 1
                    ans = i
                    break
                d2 += 1
            break
        d += 1
print(c, ans)
