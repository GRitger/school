def f (x):
    d = 1
    a = []
    while d *d < x:
        if x % d == 0:
            a.append(d)
            a.append(x//d)
        d += 1
    if d *d == x:
        a.append(d)
    a.sort()
    return a

qwe = 288
temp = f(288)
print(temp , len(temp))