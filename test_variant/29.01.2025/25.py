def f(x):
    a = []
    d = 23
    while d * d < x:
        if x % d == 0 and ((str(d)[0] == "2" and str(d)[-2] == "3") or (str(x // d)[0] == "2" and str(x //d)[-2] == "3") ):
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


n = 0
c = 500000

while n < 5:
    c += 1
    temp = f(c)
    if len(temp) > 0:
        print(c, temp)
        n += 1