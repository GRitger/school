def d(t, t2):
    x1, y1 = t
    x2, y2 = t2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


with open("27-1b.txt") as f:
    a = []
    for i in f:
        x, y = [float(t) for t in i.split()]
        a.append([x, y])
print(len(a))


def claster(to):
    cl = [t for t in a if d(t, to) < 0.3]
    if len(cl) > 0:
        for i in cl:
            a.remove(i)

        cl1 = [claster(i) for i in cl]
        cl = cl + sum(cl1, [])
    return cl


center = []

while len(a) > 0:
    t = a.pop()
    cent = [t] + claster(t)
    print(len(cent))
    center.append(cent)


def centr(c):
    tc = []
    sm = 10 ** 10
    for i in c:
        s = 0
        for j in c:
            s += d(i, j)
        if s < sm:
            sm = s
            tc = i
    return tc


sc = []
for i in center:
    sc.append(centr(i))
    print(centr(i))
print((sc[0][0] + sc[1][0] + sc[2][0]) / 3 * 10000, (sc[0][1] + sc[1][1] + sc[2][1]) / 3 * 10000)
