def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    mas = []
    d = 1
    while d * d <= x:
        if p(d) and p(x // d) and x % d == 0:
            return d
        d+=1
    return 0


for i in range(125697, 125721 + 1):
    temp = f(i)
    if f(i):
        print (i, temp, i // temp)
