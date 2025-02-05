import math


def f(x):
    d = 2
    while d * d < x:
        if x % d == 0 and p(d) and p(x // d):
            return True, d
        d += 1
    return False, 0


def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


s = -10000000000000000000000000000000000000000
ans = 0
c = 0
for i in range(356738, 404321 + 1):
    temp = f(i)
    if temp[0]:
        c += 1
        if abs((i // temp[1]) - temp[1]) > s:
            s = (i // temp[1]) - temp[1]
            ans = i

print(c, ans)
3