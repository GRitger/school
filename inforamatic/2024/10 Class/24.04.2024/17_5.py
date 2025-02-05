with open("17_5.txt") as f:
    a = [int(x) for x in f]
ma = 0
for i in a:
    if 999 < abs(i) < 10000 and abs(i) % 100 == 39:
        ma = max(ma, i)
# print(ma)
coun = 0
mas = 0
for i in range(len(a) - 1):
    c = 0
    if 999 < abs(a[i]) < 10000:
        c += 1
    if 999 < abs(a[i+1]) < 10000:
        c += 1
    if c == 1 and (a[i] + a[i+1])**2 <= ma**2:
        coun += 1
        mas = max((mas, a[i] + a[i+1]))
print(coun, mas)