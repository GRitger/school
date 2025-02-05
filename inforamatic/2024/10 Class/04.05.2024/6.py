with open("17-6.txt") as f:
    a = [int(x) for x in f]
ma2 = -100000000000
for i in a:
    if len(str(abs(i))) == 4 and abs(i) % 100 == 39:
        ma2 = max(ma2, i)
# print(ma)
coun = 0
mas = 0
for i in range(len(a) - 1):
    c = 0
    if len(str(abs(a[i]))) == 4:
        c += 1
    if len(str(abs(a[i+1]))) == 4:
        c += 1

    if c == 1 and (a[i] + a[i+1]) ** 2 <= ma2 ** 2:
        coun += 1
        mas = max(a[i] + a[i+1], mas)
print(coun, mas)
