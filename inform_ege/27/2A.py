def f(x):
    xc, yc = 0, 0
    sm = 10 ** 1000
    for i in range(len(a)):
        x, y = x[i]
        s = 0
        for j in range(len(a)):
            x1, y1 = a[j]
            s += (x - x1) ** 2 + (y - y1) ** 2
        if s < sm:
            sm = s
            xc, yc = x, y
    return xc, yc


with open("27_A_2.txt") as fal:
    a = []
    b = []
    c = []
    d = []
    for i in fal:
        x, y = [float(j) for j in i.split()]
        if y < 4:
            a.append([x, y])
        elif x > 15:
            b.append([x, y])
        elif 5 < x < 10 and 10 < y < 14:
            c.append([x, y])
        else:
            d.append([x, y])

ca = f(a)
cb = f(b)
cc = f(c)
cd = f(d)
print(ca, cb, cc, cd)
print(int((ca[0] + cb[0] + cc[0] + cd[0]) / 4 * 10000), int((ca[1] + cb[1] + cc[1] + + cd[1]) / 4 * 10000))
