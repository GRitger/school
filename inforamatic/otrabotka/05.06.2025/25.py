def p(x):
    d = 2
    while d*d <= x:
        if x% d == 0:
            return False
        d += 1
    return True

def d(x):
    d = 2
    a = []
    while d *d < x:
        if x % d == 0:
            if p(d):
                a.append(d)
            if p(x //d):
                a.append(x//d)
        d += 1
    if d * d == x:
        if p(d):
            a.append(d)

    a.sort()
    return a

ch = 1_200_000
n = 0
while n < 5:
    ch += 1
    temp = d(ch)
    m = 0
    if len(temp) > 1:
        m = temp[0] + temp[-1]
    if m> 2000 and m % 10 == 8:
        print(ch, m)
        n += 1