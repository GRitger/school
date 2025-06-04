with open("17-3.txt") as f:
    a = [int(x) for x in f]
ma = 1000000
for i in a:
    if abs(i) % 100 == 15:
        ma = min(ma, i)
# print(ma)
coun = 0
mas = 0
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 2 == 0:
        coun += 1
        mas = max(abs(a[i] - a[i+1]), mas)
print(coun, mas)
