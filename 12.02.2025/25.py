def f(x):
    d = 2
    while d *d <= x:
        if x % d == 0:
            return [d, x // d]
        d += 1
    return [0,0]
n = 0
ch = 1000000
while n < 5:
    ch += 1
    m = sum(f(ch))
    if m % 10 == 6:
        print(ch, m)
        n += 1