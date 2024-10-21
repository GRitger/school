with open("17-5.txt") as f:
    a = [int(x) for x in f]
ma = 10000000000
ma2 = -100000000000
for i in a:
    if len(str(abs(i))) == 2:
        ma = min(ma, i)
for i in a:
    if len(str(abs(i))) == 4 and abs(i) % 10 == 1:
        ma2 = max(ma2, i)
# print(ma)
coun = 0
mas = 0
for i in range(len(a) - 2):
    c = 0
    if a[i] > ma ** 2:
        c += 1
    if a[i+1] > ma ** 2:
        c += 1
    if a[i+2] > ma ** 2:
        c += 1

    if c == 2 and abs(a[i] * a[i+1] * a[i+2]) % ma2 == 0:
        coun += 1
        mas = max(abs(a[i]) + abs(a[i+1]) + abs(a[i+2]), mas)
print(coun, mas)
