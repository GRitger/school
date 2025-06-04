def dlin(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def claster(qwerty):
    cl = [t for t in a if dlin(t, qwerty) < 1]
    if len(cl) > 0:
        for i in cl:
            a.remove(i)
        cl1 = [claster(i) for i in cl]
        cl = sum(cl1, []) + cl
    return cl


def centr(c):
    #tc = []
    sm = 10 ** 10
    for i in c:
        s = 0
        for j in c:
            s += dlin(i, j)
        if s < sm:
            sm = s
            tc = i
    return tc


with open("1A.txt") as f:
    a = []
    for i in f:
        x, y = [float(j) for j in i.split()]
        a.append([x,y])
center = []
while len(a) > 0:
    t = a.pop()
    cent = [t] + claster(t)
    if len(cent) > 10:
        center.append(cent)
        print(len(cent))
sc = []
for i in center:
    sc.append(centr(i))
    print(centr(i))
