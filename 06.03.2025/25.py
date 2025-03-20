def p(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    d = 2
    a = []
    while d * d <= x:
        if x % d == 0 and p(d):
            a.append(d)
            if p(x // d):
                a.append(x // d)
        d += 1
    a.sort()
    return a

arr = []
ch = 23_600_000
n = 0
while n < 6:
    ch += 1
    temp = f(ch)
    m = 0
    if len(temp) > 2:
        m = temp[0] + temp[-1]
    if m % 213 == 171:
        arr.append([ch, temp[0], temp[-1]])
        n += 1
arr.sort()
for i in arr:
    print(*i)
