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


n = 0
ch = 700000-1
a = []
col_D = 0
while n < 5:
    ch += 1
    t = f(ch)
    if len(t) > col_D:
        n += 1
        col_D = len(t)
        a.append(ch)
        a.append(len(t))

for i in range(0,len(a)-1, 2):
    print(a[i], a[i+1])