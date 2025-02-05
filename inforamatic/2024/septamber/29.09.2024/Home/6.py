def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def f (x):
    a = []
    d = 2
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x//d)
        d += 1
    if d *d == x:
        a.append(d)
    a.sort()
    return a

for i in range(10000000):
    i = 810810000 # ответ
    temp = f(i)
    if len(temp) == 1000:
        print(i)
        break

