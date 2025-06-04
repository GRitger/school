with open("26.txt") as f:
    a = []
    zk = 99909
    rad = 4004
    k_in_rad = 400004
    b = [0] * (rad+2)
    for i in f:
        t = [int(j) for j in i.split()]
        b[t[0]] += 1
        a.append(t)
a.sort()
#print(a)
ans1 =10**100
ans2 = 0
for i in range(1,rad):
    a.append([i,0])
    a.append([i, k_in_rad+1])

a. sort(key=lambda x: (x[0], x[1]))
for i in range(1, len(a)):
    x,y = a[i]
    if x != 1 and x != rad:
        if a[i][0] == a[i-1][0] and abs(a[i][1] - a[i-1][1]) > 2:
            if b[x] >= 35 and b[x+1] + b[x-1] <= ans1:
                ans1 =  b[x+1] + b[x-1]
                ans2 = x
print(ans1, ans2)

