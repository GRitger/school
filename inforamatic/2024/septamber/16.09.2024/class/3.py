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
for i in range(268220, 270335 + 1):
    temp = f(i)
    if sum(temp) > ma and len(temp) <= 4:
        ma = sum(temp)
        ans = i
print(sum(f(ans)), len(f(ans)), f(ans))