def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


for i in range(int(525784203 ** 0.25 )+ 1, int(728943762 ** 0.25) + 1):
    if p(i):
        print( i * i * i, i * i * i * i)
