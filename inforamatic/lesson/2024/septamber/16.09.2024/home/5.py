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

ans = 0
c = 0
for i in range(236228, 305283 + 1):
    d = 2
    sr = 0
    f = False
    while d * d < i:
        d2 = 2
        if i % d  == 0:
            x = i //d
            while d2 * d2 < x:
                if p(d) and p(d2) and p(x // d2) and d != d2 and d != x//d2:
                    c +=1
                    ans += i
                    break
                d2+= 1
            break
        d += 1

print(c, ans // c)
