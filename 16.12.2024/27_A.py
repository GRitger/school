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


with open("27_A.txt") as f:
    cl1 = []
    cl2 = []
    for s in f:
        x,y = [float(x) for x in s.split()]
        if x < 23:
            cl1.append([x,y])
        else:
            cl2.append([x,y])

c1 = fu(cl1)
c2 = fu(cl2)
print(((c1[0]+c2[0])/2)*1000, ((c1[1]+c2[1])/2)*1000 )