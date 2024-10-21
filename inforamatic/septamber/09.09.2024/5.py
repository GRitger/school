def f(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


ans = []
nomer = 1
for i in range(33333, 55555 + 1):
    temp = f(i)
    s = 0
    qwe = i
    while i:
        s += i % 10
        i //= 10

    if temp and s > 35:
        print(qwe, s)
