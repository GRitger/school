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

for i in range(78920, 92430+1):
    temp = f(i)
    if (len(temp) == 5):
        print(*temp)