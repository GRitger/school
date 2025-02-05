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
for i in range(194441, 196500 + 1):
    temp = f(i)
    if temp and i % 100 == 93:
        print(nomer, i)
        nomer += 1
