def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d+=1
    return True

n = 1
for i in range(6638225, 6638322 + 1):
    if p(i):
        print(n, i)
        n += 1
