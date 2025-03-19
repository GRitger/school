
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
    kl5 = []
    for i in text:
        x, y = float(i.split()[0]), float(i.split()[1])
        if 3 < x < 7 and y < 4 :
            kl1.append([x,y])
        elif 6 < x < 11 and 10 < x < 14:
            kl2.append([x,y])
        elif 21 < x < 25 and 5 < y < 8:
            kl3.append([x,y])
        elif  24 < x < 28 and 1 < y < 5:
            kl4.append([x, y])
        elif  28 < x < 32 and y < 4:
            kl5.append([x, y])
    print(len(kl1) + len(kl2) + len(kl3)+ len(kl4)+ len(kl5) )
    k1 = f(kl1)
    k2 = f(kl2)
    k3 = f(kl3)
    k4 = f(kl4)
    k5 = f(kl5)
px = k1[0]+ k2[0]+ k3[0]+ k4[0] + k5[0]
py = k1[1]+ k2[1]+ k3[1]+ k4[1] + k5[1]
print(px/5 *10000, py / 5 * 10000)