def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def f (x):
    a = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            a.append(x//d)
        d += 1
    a.sort(reverse=True)
    return a

a =[]
for i in range(3 , int(75000000 ** 0.25) + 1):
    if p(i):
        x = i ** 4
        while x < 75000000:
            if 63000000 < x < 75000000:
                a.append(x)
            x *= 2
a.sort()
for i in a:
    temp = f(i)
    for j in range(len(temp)):
        if temp[-j] % 2 == 1:
            print(i, temp[-j])

