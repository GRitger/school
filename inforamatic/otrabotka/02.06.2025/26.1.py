with open("26-153.txt") as f:
    a = {}
    for i in f:
        art, cen, status = [int(x) for x in i.split()]
        if status == 1:
            if a.get(art) is None:
                a[art] = [1, cen, 0]
            else:
                a[art][0] += 1
        else:
            if a.get(art) is None:
                a[art] = [-0, cen, 1]
            else:
                a[art][2] += 1

z = a.items()
for i in  z:
    print(i)

sr = 0
for i in z:
    sr += i[1][1]
sr = sr / len(z)

ans1 = 0
ans2 = 0
m = [0,0,0]
for i in z:
    temp = i
    if temp[1][2] == 59:
        wsdf = 585
    if m[2] == 59:
        sdfsd=34
    if i[1][1] > sr:
        if i[1][2] > m[2]:
            m = i[1]
            ans1 = (i[1][0] - i[1][2])*i[1][1]
            ans2 = i[0]
        elif i[1][2] == m[2]:
            if i[1][1] > m[1]:
                m = i[1]
                ans1 = i[1][0] * i[1][1]
                ans2 = i[0]
            elif i[1][1] == m[1]:
                if i[1][0] < m[0]:
                    m = i[1]
                    ans1 = (i[1][0] - i[1][2]) * i[1][1]
                    ans2 = i[0]
print(ans1, ans2)


