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


chet = 0
sum_chet = 0
pr = 0
sum_pr = 0
ans = 0

for i in range(100000000, 10000000000000000):
    chet = 0
    sum_chet = 0
    pr = 0
    sum_pr = 0
    temp = f(i)
    for j in temp:
        if p(j) and j != i:.
            pr += 1
            sum_pr += j
        if j % 2 == 0:
            chet += 1
            sum_chet += j
    if pr == chet and pr != 0:
        ans += 1
        print(i, abs(sum_pr - sum_chet ))
    if ans == 5:
        break