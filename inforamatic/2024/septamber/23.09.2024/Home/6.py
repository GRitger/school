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
    d = 2
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d *d ==x:
        a.append(d)
    a.sort()
    return a

n = 0
ch = 200000000

while n < 5:
    ch += 1
    temp = f(ch)
    P = 0
    if len(temp) >= 5:
        P = 1
        for i in range(5):
            P *= temp[i]
    if P % 10 == 1 and P < ch:
        print(P, temp[4])
        n += 1

