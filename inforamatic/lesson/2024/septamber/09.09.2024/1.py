def f(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

nomer = 1
ans = []
for i in range(3532000, 3532160 + 1):
    temp = f(i)
    if temp:
        print(nomer, i)
        nomer += 1
