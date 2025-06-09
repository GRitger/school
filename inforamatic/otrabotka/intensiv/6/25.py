def p(x):
    d = 2
    if x == 1 or x ==0 :
        return False
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def f(x):
    d = 2
    a = []
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


ch = 10_000_000
n = 0
while n < 5:
    ch += 1
    temp = f(ch)
    sn = 0
    if len(temp) > 3:
        sn = temp[-1] + temp[-2] + temp[-3]
    if p(sn):
        print(ch, sn)
        n += 1
