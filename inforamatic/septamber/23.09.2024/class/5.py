def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x :
        if x % d == 0:
            return False
        d += 1
    return  True

def f(x):
    a = []
    d = 1
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d *d ==x:
        a.append(d)
    a.sort()
    return a

for i in range(190201, 190260):
    temp = f(i)
    a = []
    for j in temp:
        if j % 2 == 0:
            a.append(j)
    if len(a) == 4:
        print(a[-1], a[-2])
print(int(60000000 ** 0.25))