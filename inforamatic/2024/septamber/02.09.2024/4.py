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

ans = []
mi = 1000000000000000000000000000000000000000000
ma = -1
max_len = 0
for i in range(586132, 586430+1):
    max_len = max()


print(mi)