with open ("1.txt") as f:
    a = []
    for i in f:
        a.append(int(i))

a.sort()
s = 0
index = 0
for i in range(len(a)):
    if s + a[i] > 8200:
        print(i)
        index = i - 1
        break
    else:
        s += a[i]
s -= a[index]
qwe = -1000000000000000000000
while a[index] <= 8200 - s:
    qwe =a[index]
    index += 1
print(qwe)
#8200 970