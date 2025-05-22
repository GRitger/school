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
a = 1000000000000000000000000000000000000000000

for i in range(573213, 575340+1):
    temp = f(i)
    if (len(temp) == 4):
        qwe = sum(temp)
        if qwe < a:
            a = qwe
            ans = temp
print(a, ans[-1])