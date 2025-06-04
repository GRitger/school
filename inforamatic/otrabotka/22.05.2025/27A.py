from math import dist

def fu(cl1, cl2):
    ans1 = []
    ans2 = []
    di = float("inf")
    for i in cl1:
        for j in cl2:
            r = dist(i,j)
            if r < di:
                ans1 = i
                ans2 = j
                di = r
    return ans1, ans2


with open("27-85a.txt") as f:
    cl1 = []
    cl2 = []
    for s in f:
        x,y = [float(x) for x in s.split()]
        if y < 6:
            cl1.append([x,y])
        else:
            cl2.append([x,y])

c1, c2 = fu(cl1, cl2)
srx = c1[0] + c2[0]
sry = c1[1] + c2[1]
print(int(abs(srx/2 * 10000)),int(abs(sry/2 * 10000)) )