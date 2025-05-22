import math


def f(x):
    mas = []
    d = 1
    while d * d < x:
        if x % d == 0:
            mas.append(d)
            mas.append(x // d)
        d += 1
    if d * d == x:
        mas.append(d)
    mas.sort()
    return mas


def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


s = 0
pr = 0
ans = 0

for i in range(10, 100):
    if p(i):
        pr = i
print (pr)
print (pr **3)
for i in range(pr ** 3 + 1, 10000000000000000):
    temp = f(i)
    c = 0
    ma = 10**100
    for j in temp:
        if 100 <= j < 1000 and j % 10 == 3:
            ma = min(j, ma)
            c += 1
    if c == 3:
        print(i, ma)
        ans += 1
    if ans == 5 :
        break