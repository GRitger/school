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
mi = 10**100
a = []
c = 0
for i in range(3159, 31584 + 1):
    d = 2
    sr = 0
    while d * d < i:
        if i % d == 0 and p(d) and p(i // d):
            sr = (d + i //d) / 2
            if abs(sr - i) < mi:
                mi = abs(sr-i)
                ans = i
            a.append(d)
        d += 1

print(len(a), ans )
