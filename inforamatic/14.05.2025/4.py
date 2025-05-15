from math import ceil
with open("4.txt") as f:
    a = []
    sa = 0
    n = int(f.readline())
    b = []
    for i in f:
        if int(i) > 250:
            a.append(int(i))
        else:
            b.append(int(i))
a.sort(reverse = True)
for i in range(len(a)):
    if i% 3 == 0:
        sa += ceil(a[i] / 3)
    else:
        sa += a[i]


print(sa + sum(b))

sa = 0
i = 0
j = len(a)-1
flag = True
while i != j:
    if i % 3 == 0 and flag:
        sa += ceil(a[j] / 3)
        j -= 1
        flag = False
    else:
        sa += a[i]
        i += 1
        flag = True
print(sa + sum(b))

print(a)