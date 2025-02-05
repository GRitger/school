def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


for i in range(int(1820348 ** 0.25) + 1, int(2880927 ** 0.25) + 1):
    if p(i):
        print(1, i, i*i, i*i*i, i*i*i*i)
