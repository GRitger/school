def fu(cl):
    ans1 = [x for x, y in cl]
    ans2 = [y for x, y in cl]
    ans1.sort()
    ans2.sort()
    l =  len(ans1) //2
    return ans1[l], ans2[l]


with open("27-86b.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in f:
        x, y = [float(j) for j in i.split()]
        if x > 4:
            cl1.append([x,y])
        elif y > 7:
            cl3.append([x, y])
        else:
            cl2.append([x,y])
print(len(cl1) + len(cl2) + len(cl3))

c1 = fu(cl1)
c2 = fu(cl2)
c3 = fu(cl3)

srx = (c1[0] + c2[0] + c3[0]) / 3
sry = (c1[1] + c2[1] + c3[1]) / 3

print(abs(int(srx * 10000)), abs(int(sry * 10000)))

