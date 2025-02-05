from itertools import product


def d(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    d = 1
    a = []
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


def chet(a):
    col = 0
    su = 0
    for i in a:
        if i % 2 == 0:
            col += 1
            su += i
    return col, su


ch = 0
n = 0
while n < 7:
    for k in range(2):
        for i in product("0123456789", repeat=k):
            i = "".join(i)
            for k2 in range(2):
                for j in product("0123456789", repeat=k2):
                    j = "".join(j)
                    for q in "02468":
                        ch = int("6" + j+ "97" + i + "5" + q)
                        if ch > 65000:
                            temp = f(ch)
                            a, b = chet(temp)
                            if a >= 4:
                                print(ch, b)
                                n += 1
