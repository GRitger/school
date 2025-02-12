a = []

with open("17.txt") as f:
    for i in f:
        a.append(int(i))

c = 0
m = 10**100
for i in range(len(a) - 1):
    if a[i] % 30 == min(a) or a[i + 1] % 30 == min(a):
        c += 1
        m = min(a[i] + a[i+1], m)
print(c, m)
