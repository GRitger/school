def d(x):
    d = 1
    a = []
    while d *d < x:
        if x% d == 0:
            a.append(d)
            a.append(x//d)
        d += 1
    if d *d == x:
        a.append(d)
    return sum(a)

from fnmatch import fnmatch
n = 0
for i in range(666, 1000000000):
    if fnmatch(str(i), "?6*6*?6") and (i % 6== 0 and i % 7== 0 and i % 8== 0):
        n += 1
        print(i, d(i))

    if n == 7 :
        break