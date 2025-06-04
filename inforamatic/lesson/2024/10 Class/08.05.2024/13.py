with open("13.txt") as f:
    a = [int(x) for x in f]
ma = 10**10
for i in a:
    if i % 10 == 5 and len(str(i)) == 3:
        ma = min(ma, i)

coun = 0
mas = 0
for i in range(len(a) - 1):
    c = 0
    if len(str(a[i])) == 3:
        c += 1
    if len(str(a[i+1])) == 3:
        c += 1
    if c == 1 and (a[i] + a[i+1]) % ma == 0:
        coun += 1
        mas = max((a[i]**2) + (a[i+1]**2), mas)
print(coun, mas)
