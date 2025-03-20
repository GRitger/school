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
    for s in f:
        x,y = [float(x) for x in s.split()]
        if x < -12:
            cl1.append([x,y])
        if -12 < x < 16:
            cl2.append([x,y])
        if x > 16:
            cl3.append([x,y])
    print(len(cl1)+len(cl2)+len(cl3))

c1 = fu(cl1)
c2 = fu(cl2)
c3 = fu(cl3)
print(((c1[0]+c2[0]+c3[0])/3)*1000, ((c1[1]+c2[1]+c3[1])/3)*1000 )