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
    return a

n = 0
ch = 250000

while n < 5:
    s = 0
    ch +=1
    t = f(ch)
    for i in t:
        if p(i):
            s += i
    if s and s % 17 == 0:
        n += 1
        print(ch, s)
