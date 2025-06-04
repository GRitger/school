def fu(cl):
    ans = [0,0]
    rast = 10000000000000000000000000000000000000000000000000000000000000000000000000000
    for i in cl:
        x, y = i
        s = 0
        for j in cl:
            x2, y2 = j
            s += abs(x-x2) + abs(y-y2)
        if s < rast:
            rast = s
            ans = i
    return ans


with open("27_B.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    for s in f:
        x,y = [float(x) for x in s.split()]
        if x > 12:
            cl1.append([x,y])
        elif  14 < y < 17:
            cl2.append([x, y])
        elif  10 < y < 13:
            cl3.append([x, y])
        elif  6 < y < 9:
            cl4.append([x, y])
        else:
            cl5.append([x, y])

print(len(cl1)+len(cl2)+len(cl3)+len(cl4)+len(cl5))

c1 = fu(cl1)
c2 = fu(cl2)
c3 = fu(cl3)
c4 = fu(cl4)
c5 = fu(cl5)
print((c1[0]+c2[0]+c3[0]+c4[0]+c5[0])*1000, (c1[1]+c2[1]+c3[1]+c4[1]+c5[1])*1000 )