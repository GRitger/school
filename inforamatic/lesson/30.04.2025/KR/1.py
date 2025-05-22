def f(x):
    a = []
    d = 2
    while d * d < x:
        if x % d ==0:
            a.append(d)
            a.append(x//d)
        d += 1
    if d *d == x:
        a.append(d)
    a.sort()
    return a

ch = 800000
n = 0

while n < 5:
    ch += 1
    temp = f(ch)
    M = 0
    if len(temp) > 0:
        M = temp[0] + temp[-1]
    if M % 10 == 4:
        print(ch, temp[0] + temp[-1])
        n += 1
