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
for i in range(int(1820348**0.25), int(2880927 ** 0.25)+1):
    if p(i):
        print(i*i*i, i*i*i*i)