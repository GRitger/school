def f(x):
    a = []
    d = 2
    while d *d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d +=1
    if d * d==x:
        a.append(d)
    a.sort()
    return a

ch = 452022
n =0
while n < 5:
    ch +=1
    temp = f(ch)
    m = 0
    if len(temp) > 1:
        m = temp[0]+ temp[-1]
    if m % 7 == 3:
        print(ch, m)
        n += 1