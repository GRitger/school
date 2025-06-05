def fu(cl1):
    ans1 = [x for x, y in cl1]
    ans2 = [y for x, y in cl1]
    ans1.sort()
    ans2.sort()
    k = len(cl1) // 2
    return ans1[k], ans2[k]


with open("27-86a.txt") as f:
    cl1 = []
    cl2 = []
    for s in f:
        x, y = [float(x) for x in s.split()]
        if x > 6:
            cl1.append([x, y])
        else:
            cl2.append([x, y])

c1 = fu(cl1)
c2 = fu(cl2)
srx = c1[0] + c2[0]
sry = c1[1] + c2[1]
print(int(abs(srx / 2 * 10000)), int(abs(sry / 2 * 10000)))
