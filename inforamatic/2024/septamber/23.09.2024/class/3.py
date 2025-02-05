def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

m1 = 1
m2 = 1
for i in range(int(106732567**0.25)+1, int(152673836 ** 0.25)+1):
    if p(i):
        print(i**4, i*i*i)