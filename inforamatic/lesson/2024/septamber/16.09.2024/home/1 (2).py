def p(x):
    if x == 1:
        return False
    d = 2
    while d *d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def f(x):
    a = []
    d = 1
    while d *d < x:
        if x % d == 0:
            a.append(d)
            a.append(x //d)
        d += 1
    if d *d == x:
        a.append(d)
    a.sort()


с = 0
for i in range(2, 20000+1):

    if p(i):
        с+=1
print(с)