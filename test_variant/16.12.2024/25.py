def f(x):
    d = 2
    a = []
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x//d)
        d += 1
    if d *d == x:
        a.append(x)
    a.sort()
    return a

ch = 770000
n = 0
while n <5:
    ch -=1
    temp= f(ch)
    temp.append(1)
    temp.sort()
    if len(temp):
        sr = sum(temp)//len(temp)
        if sr %100 == 12:
            print(ch, sr)
            n+=1