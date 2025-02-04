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


with open("27A.txt") as file:
    cl1 = []
    cl2 = []
    for s in file:
        x, y = [float(x) for x in s.split()]
        if x < 1:
            cl1.append([x, y])
        elif 1 < x < 3.5:
            cl2.append([x, y])


r1 = f(cl1)
r2 = f(cl2)

print((r1 + r2)/2 *10000)