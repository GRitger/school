def center(cl):
    l = len(cl)
    sx = 0
    sy = 0
    for i in cl:
        sx += i[0]
        sy += i[1]
    return sx/l, sy/l

with open("27-87b.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in f:
        st = i.replace(",", ".")
        x,y = [float(x) for x in st.split()]
        if x > 5:
            cl1.append([x,y])
        elif y > 6:
            cl2.append([x,y])
        else:
            cl3.append([x,y])

c1 = center(cl1)
c2 = center(cl2)
c3 = center(cl3)
print((c1[0]+c2[0]+c3[0])*10000/3, (c1[1]+c2[1] + c3[1])*10000/3)