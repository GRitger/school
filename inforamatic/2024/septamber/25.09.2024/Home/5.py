def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


for i in range(100000000, 101000001, 2):
    if (i // 2) ** 0.5 == int((i // 2) ** 0.5) and p(int((i // 2) ** 0.5)):
        print(i)
