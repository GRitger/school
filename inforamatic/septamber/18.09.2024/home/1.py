def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x :
        if x % d == 0:
            return False
        d += 1
    return  True

def f(x):
    a = []
    d = 2
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d *d ==x:
        a.append(d)
    return a

n = 0
ch = 800000

while n < 5:
    ans = 10 ** 100
    ch +=1
    t = f(ch)
    for i in t:
        if i % 10 == 9 and i != 9:
            ans = min(ans, i)
    if ans < 10**100:
        n+=1
        print(ch, ans)
