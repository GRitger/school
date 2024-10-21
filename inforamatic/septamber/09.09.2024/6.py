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
    d = 1
    a = []
    while d * d <= x:
        if x % d == 0 and p(d) and p(x // d):
            return True, d
        d += 1
    return False


ans = []
nomer = 1
for i in range(478392, 502439 + 1):
    temp = f(i)
    s = 0
    if temp[0]:
        ans.append(i, d - i//d)
