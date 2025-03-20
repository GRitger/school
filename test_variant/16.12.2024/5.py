a = []
for i in range(0, 1000, 2):
    n = bin(i)[2:]
    if i == 6:
         j4oje = 4
    if i % 3 == 0:
        n = "1"+n[:-2]+"11"
    else:
        n = "10" + n + "0"
    ans = int(n,2)
    if ans > 999:
        a.append(ans)
print(min(a))