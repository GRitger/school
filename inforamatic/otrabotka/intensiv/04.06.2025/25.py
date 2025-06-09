def f(x):
    d = 2
    a = []
    while d*d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d *d == x:
        a.append(x)
    a.sort()
    return a

ch = 10_000_000
n = 0
while n < 5:
    ch += 1
    temp = f(ch)
    s = 0
    if len(temp) >1:
        s += temp[-1] + temp[-2]
    if s < 100000 and s % 31 == 0 and s != 0:
        print(ch,s)
        n += 1