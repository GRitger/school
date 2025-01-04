with open("17.txt") as f:
    a = [int(i) for i in f]

m = -1000000000000000000000000000000000000
for i in a:
    if 1000 <= i <= 9999 and i % 100 == 39:
        m = max(m, i)
print(m)
c = 0
ans = -100000000000000000000000000000000000
for i in range(len(a) - 1):
    if ((1000 <= a[i] <= 9999 and not(1000 <= a[i+1] <= 9999)) or (1000 <= a[i+1] <= 9999 and not(1000 <= a[i] <= 9999))) and (a[i]+ a[i+1])**2 <= m:
        c += 1
        ans = max(ans,a[i]+ a[i+1])
print(c, ans)