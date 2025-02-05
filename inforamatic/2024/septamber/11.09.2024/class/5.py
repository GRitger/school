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
ans = 0

for i in range(862346, 1056242 + 1):
    temp = f(i)
    flag = True
    for j in range(1, len(temp)-2):
        if temp[j] + 100 != temp[j+1]:
            flag = False
            break
    if flag and len(temp) >3:
        print(i, temp[-2])
