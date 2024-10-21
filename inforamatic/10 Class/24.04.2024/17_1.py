with open("17_1.txt") as f:
    a = [int(x) for x in f]
ma = 0
for i in a:
    if 9 < i < 100:
        ma = max(ma, i)
# print(ma)
coun = 0
mas = 0
for i in range(len(a) - 1):
    c = 0
    if 9 < a[i] < 100:
        c += 1
    if 9 < a[i+1] < 100:
        c += 1
    if c == 1 and (a[i] + a[i+1]) % ma == 0:
        coun += 1
        mas = max(mas, a[i] + a[i+1] % ma)
print(coun, mas)
