def f(kl):
    m = 10000000000000000000000000000000000000000000000000000000000000000000000000000000
    ans = [0,0]
    s = 0
    for x,y in kl:
        s = 0
        for x2, y2 in kl:
            s += ((x2 - x)**2 + (y2 - y)**2)**0.5
        if s < m:
            m = s
            ans = x,y
    return ans

with open("27A.txt") as text:
    kl1= []
    kl2 = []

    for i in text:
        x, y = float(i.split()[0]), float(i.split()[1])
        if x <0.5:
            kl1.append([x,y])
        elif x > 0.5:
            kl2.append([x,y])

    k1 = f(kl1)
    k2 = f(kl2)
px = k1[0]+ k2[0]
py = k1[1]+ k2[1]
print(px/2 *10000, py / 2 * 10000)