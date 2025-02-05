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


for i in range(25317, 51237 + 1):
    temp = f(i)
    if len(temp) >= 8:
        for j in range(len(temp)-1, -1, -1):
            if p(temp[j]):
                print(i, temp[j])
                break
