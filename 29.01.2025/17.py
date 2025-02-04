with open("17.txt") as f:
    a = []
    for i in f:
        a.append(int(i))

ans = 0
ans2 = 0
for i in range(len(a) - 2):
    c = 0
    if str(a[i]).count("0") == 0:
        c += 1
    if str(a[i + 1]).count("0") == 0:
        c += 1
    if str(a[i + 2]).count("0") == 0:
        c += 1

    if c >= 2 and a[i] + a[i + 1] + a[i + 2] < (max(a) /2 ):
        ans += 1
        ans2= max(ans2,  a[i] + a[i + 1] + a[i + 2])
print(ans, ans2 )