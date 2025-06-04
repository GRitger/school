with open("17-4.txt") as f:
    a = [int(x) for x in f]
ma = 0
for i in a:
    if abs(i) % 19 == 0:
        ma = max(ma, i)
# print(ma)
coun = 0
mas = 0
for i in range(len(a) - 1):
    if a[i] > ma or a[i+1] > ma:
        coun += 1
        mas = max(a[i] + a[i+1], mas)
print(coun, mas)