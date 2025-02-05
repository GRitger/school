from itertools import permutations
def p(x):
    if x == 1:
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
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


for i in range(1411111115, 1411111127):
    if i == 1411111120:
        continue
    st = str(i)
    qwe = set(permutations(st))
    for j in qwe:
        t = "".join(j)
        if p(int(t)):
            print(i)
            break
