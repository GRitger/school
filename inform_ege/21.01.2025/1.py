with open("1.txt") as f:
    a = []
    n = 0
    for i in f:
        temp = int(i)
        a.append(temp)
        if 9 < temp < 100:
            n += 1
ans = 0
mi = []
for i in range(len(a) -1):
    if int(str(a[i])[-1]) + int(str(a[i+1])[-1]) == n:
        ans += 1
        mi.append(a[i]+a[i+1])
print(ans, min(mi))