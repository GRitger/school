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


a = []
for i in range(12620, 1000000):
    a.append(i * i)
    if i * i > 973146286:
        break
#print(a)
for i in range(159264873, 973146285, 2000):
    if i in a:
        print(i)
