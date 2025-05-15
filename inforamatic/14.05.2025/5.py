with open("5.txt") as f:
    k = 74619
    m = 0
    a = []
    for i in f:
        t = [int(j) for j in i.split()]
        m = max(m, t[1])
        a.append(t)

b = [-1] * (m+1)
b[1] = 0
a.sort()
for i in range(len(a)):
    p1,p2,d = a[i]
    if b[p1] != -1 and d + b[p1] <= k:
        if b[p2] == -1:
            b[p2] = b[p1] + d
        else:
            b[p2] = min(b[p2], b[p1] + d)

ans1 = 0
ans2 = 0
for i in range(len(b)):
    if b[i] != -1:
        ans1 = i
        ans2 = b[i]

print(ans1, k - ans2)
