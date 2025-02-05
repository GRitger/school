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


ch = 10000000
n = 0
a = []
while n < 3:
    ch-=1
    if p(ch):
        a.append(ch)
        n += 1
ch = 10000000
while n < 6:
    ch+=1
    if p(ch):
        a.append(ch)
        n += 1
a.sort()
for i in range(0, len(a)):
    print(abs(10000000-a[i]), a[i])