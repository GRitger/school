with open("17.txt") as f:
    a = [int (x) for x in f]
    m = 1000000000000000000000000000000000000000000000000
    for i in a:
        if i % 41 == 0 and i > 0:
            m = min(i, m)
n = 0
ans = -10000000000000000000000000000000000000000000000000000000000
for i in range(len(a)-1):
    if a[i] != a[i+1] and abs(a[i]- a[i+1]) % m == 0:
        ans = max(a[i]+a[i+1], ans)
        n += 1
print(n, ans)
