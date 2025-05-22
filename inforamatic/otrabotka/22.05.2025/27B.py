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


with open("27-85b.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []
    for s in f:
        x,y = [float(x) for x in s.split()]
        if y < 4 and x < 2:
            cl1.append([x,y])
        elif x > 2 and y < 5:
            cl2.append([x,y])
        else:
            cl3.append([x,y])

c1, c2 = fu(cl1,cl2)
c3, c4 = fu(cl2,cl3)
c5, c6 = fu(cl1,cl3)

srx = c1[0] + c2[0] + c3[0] + c4[0]+ c5[0] + c6[0]
sry = c1[1] + c2[1] + c3[1] + c4[1]+ c5[1] + c6[1]
print(int(abs(srx/6 * 10000)),int(abs(sry/6 * 10000)) )