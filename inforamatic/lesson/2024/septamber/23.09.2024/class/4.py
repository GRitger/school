def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


x = 0
c = 0
a = []
for i in range(int(3), int(60000000 ** 0.25) + 1):
    if p(i):
        a.append(i)

for i in a:
    x = i ** 4
    while x <= 60000000:
        if 55000000 <= x <= 60000000:
            print(x, i**4)
        elif x >= 60000000:
            break
        x *= 2