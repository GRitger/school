from fnmatch import fnmatch


def f(x):
    c = 0
    d = 2
    su = 0
    while d *d < x:
        if x % d == 0:
            if  (x // d) % 2 == 0:
                c += 1
                su += (x // d)
            c += 1
            su += d
        d += 2
    if d * d == 0:
        c += 1
        su += d
    return c, su
n = 0
for i in range(65002, 1000000, 2):
    if fnmatch(str(i), "6*97*5?"):
        c, su = f(i)
        if c >= 4:
            print(i,su)
            n += 1
    if n >7:
        break
