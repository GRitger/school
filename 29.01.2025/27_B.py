def f(cl):
    m = 10000000000000000000000000000000000000000000000000000000000000000000000000000000
    ans = 0
    for x, y in cl:
        s = 0
        r = -1000
        for x2, y2 in cl:
            s += ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
            r = max(r,((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5 )
        if s < m:
            m = s
            ans = r
    return ans


with open("27B.txt") as file:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    for s in file:
        x, y = [float(x) for x in s.split()]
        if x < -1.5:
            cl1.append([x, y])
        elif 1.8 < x < 4.2 and y < 5.5:
            cl3.append([x, y])
        elif x > 4.2:
            cl4.append([x, y])
        elif y > 5 and x < 3:
            cl5.append([x, y])

print(len(cl1))
print(len(cl3))
print(len(cl4))
print(len(cl5))

r1 = f(cl1)
r3 = f(cl3)
r4 = f(cl4)
r5 = f(cl5)

print((r1 + r3 + r4 + r5)/4 *10000)