
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


with open("27_A.txt") as text:
    kl1= []
    kl2 = []
    kl3 = []
    kl4 = []
    for i in text:
        x, y = float(i.split()[0]), float(i.split()[1])
        if x > 15 and 10 < y < 14:
            kl1.append([x,y])
        elif y < 4 and 10 < x < 15:
            kl2.append([x,y])
        elif 14 > y > 10 and 10 > x > 5:
            kl3.append([x,y])
        else:
            kl4.append([x, y])
    k1 = f(kl1)
    k2 = f(kl2)
    k3 = f(kl3)
    k4 = f(kl4)
px = k1[0]+ k2[0]+ k3[0]+ k4[0]
py = k1[1]+ k2[1]+ k3[1]+ k4[1]
print(px/4 *10000, py / 4 * 10000)