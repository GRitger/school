with open("26-90.txt") as f:
    n = int(f.readline())
    a = [int(x) for x in f]

a.sort(reverse=True)
i = 0
j = len(a)-1
s = 0
flag = False
while i <= j:
    if i% 3 == 0 and flag:
        s += a[j]*0.5
        j -= 1
        flag = False
    else:
        s += a[i]
        i += 1
        flag = True

a.sort()
i = 0
j = len(a)-1
s2 = 0
flag = False
while i <= j:
    if i!= 0 and i% 3 == 0 and flag:
        s2 += a[j] * 0.5
        j -= 1
        flag = False
    else:
        s2 += a[i]
        i += 1
        flag = True
print(s2,s)