from math import dist
def center(cl):
    s =10**100
    cen = []
    for i in cl:
        su = 0
        for j in cl:
            su += dist(i,j)
        if su < s:
            s = su

            cen = i
    return cen

with open("27_B.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []

    for i in f:
        st = i.replace("\t", " ").replace(",", ".")
        x,y = [float(x) for x in st.split()]
        if  y < 10:
            cl1.append([x,y])
        elif x > 17:
            cl2.append([x,y])
        else:
            cl3.append([x,y])

c1 = center(cl1)
c2 = center(cl2)
c3 = center(cl3)
print(int(c3[0] * 10000), int(c1[1] * 10000))
