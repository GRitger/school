def f(a):
    xc, xy = 0, 0
    sm = 10 ** 100
    for i in range(len(a)):
        s = 0
        x, y = a[i]
        for j in range(len(a)):
            x2, y2 = a[j]
            s += (x - x2) ** 2 + (y - y2) ** 2
        if s < sm:
            sm = s
            xc, xy = x, y
    return xc, xy


with open("27_B_1.txt") as fal:
    a = []
    b = []
    c = []
    for s in fal:
        x, y = [float(i) for i in s.split()]
        if y <= 4:
            a.append([x, y])
        if 4 <= y <= 7:
            b.append([x, y])
        if y >= 7:
            c.append([x, y])

temp = f(a)
temp2 = f(b)
temp3 = f(c)
print(f(a), f(b), f(c))
print(int((temp[0] + temp2[0] + temp3[0]) / 3 * 10000), int((temp[1] + temp2[1]+ temp3[1]) / 3 * 10000))
