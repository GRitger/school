def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


n = 1
for i in range(2532000, 2532160 + 1):
    if p(i) and i % 10 == 7:
        print(n, i)
        n += 1
