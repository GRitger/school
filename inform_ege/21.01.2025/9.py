with open("9.txt") as f:
    m = 0
    a = []
    for i in f:
        a.append(int(i))
        i = int(i)
        if abs(i) % 10 == 7 and 9999 < abs(i) < 100000:
            m = max(m, i)

ans = 0
ans2 = []
for i in range(len(a) - 2):
    c = 0
    if abs(a[i]) % 100 == 12:
        c += 1
    if abs(a[i+1]) % 100 == 12:
        c += 1
    if abs(a[i+2]) % 100 == 12:
        c += 1
    if c == 2 and (a[i] + a[i + 1] + a[i + 2]) < m:
        ans += 1
        ans2.append((a[i] + a[i + 1] + a[i + 2]))
        print(a[i], a[i+1], a[i+2])
print(ans, min(ans2))
