def p(x):
    if x == 1  or x == 0:
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
ch = 350300

while n < 6:
    ch += 1
    s = sum(f(ch))
    if s and s % 13 == 0:
        print(ch, s // 13)
        n += 1