with open("5.txt") as f:
    a =[]
    for i in f:
        a.append(int(i))

ans = 0
ans2 = []
for i in range(len(a)-2):
    c = 0
    if a[i] > 0:
        c += 1
    if a[i+1] > 0:
        c += 1
    if a[i+2] > 0:
        c += 1
    if c <= 1 and abs(a[i]+a[i+1]+a[i+2])%10 == abs(min(a))% 10:
        ans += 1
        ans2.append(abs(a[i]+a[i+1]+a[i+2]))
print(ans, max(ans2))