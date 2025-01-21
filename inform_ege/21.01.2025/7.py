with open("7.txt") as f:
    m = 0
    a = []
    for i in f:
        a.append(int(i))
        i = int(i)
        if abs(i) % 10 == 3 and 99 < abs(i) < 1000:
            m = max(m, i)

ans = 0
ans2 = []
for i in range(len(a) - 2):
    c = 0
    if abs(a[i]) % 10 == 3 and 99 < abs(a[i]) < 1000:
        c += 1
    if abs(a[i+1]) % 10 == 3 and 99 < abs(a[i+1]) < 1000:
        c += 1
    if abs(a[i+2]) % 10 == 3 and 99 < abs(a[i+2]) < 1000:
        c += 1
    if c >= 1 and (a[i] + a[i + 1] + a[i + 2]) < m:
        ans += 1
        ans2.append((a[i] + a[i + 1] + a[i + 2]))
        print(a[i], a[i+1], a[i+2])
print(ans, max(ans2))
