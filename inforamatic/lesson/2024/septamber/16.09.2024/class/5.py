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
ans_c= 0
ma = -1000000000000000000000000000
for i in range(2, 20000 + 1):
    temp = f(i)
    c = 0
    for j in temp:
        if p(j):
            c += 1
    if c > ma:
        ma = c
        ans = i
print(ans, ma)