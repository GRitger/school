import cmath


def p(x):
    if x == 1 or x == 0:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    a = []
    d = 2
    ans = 0
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
            ans = d
        d += 1
    '''if d * d == x:
        a.append(d)
    '''
    a.sort()
    return ans


n = 0
ch = 710017
mpr = -1
while n < 5:
    ch += 1
    m = 0
    k = f(ch)

    if k and ch % k == 0 and k*k != ch:
        m = k + ch // k

    if m % 10 == 0 and m > mpr:
        mpr = m
        print(ch, m)
        n += 1
