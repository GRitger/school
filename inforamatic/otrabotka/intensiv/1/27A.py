def center(cl):
    l = len(cl)
    sx = 0
    sy = 0
    for i in cl:
        sx += i[0]
        sy += i[1]
    return sx/l, sy/l

with open('27-87a.txt') as f:
    cl1 = []
    cl2 = []
    for i in f:
        st = i.replace(",", ".")
        x, y = [float(x) for x in st.split()]
        if y > 5:
            cl1.append([x, y])
        else:
            cl2.append([x, y])

c1 = center(cl1)
c2 = center(cl2)

print(abs(int((c1[0] + c2[0]) *10_000/2)), abs(int((c1[1] + c2[1]) *10_000/2)))
