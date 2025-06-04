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
    a.sort()
    return a

n = 0
ch = 450000

while n < 4:
    ch += 1
    temp = f(ch)
    P_max = 0
    flag= True
    P_min = 0
    for i in temp:
        if p(i):
            P_max = i
        if flag and p(i):
            flag = False
            P_min = i
    m = P_max - P_min
    if m % 29 == 11:
        print(ch, m)
        n += 1

