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


with open("27_A_1.txt") as fal:
    a = []
    b = []
    for s in fal:
        x, y = [float(i) for i in s.split()]
        if -3 <= x <= 1 and y <= 3:
            a.append([x, y])
        if x > 1 and y > 3:
            b.append([x, y])

temp = f(a)
temp2 = f(b)
print(f(a), f(b))
print(int((temp[0] + temp2[0]) / 2 * 10000), int((temp[1] + temp2[1]) / 2 * 10000))

