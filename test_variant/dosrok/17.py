with open("17_21416.txt") as f:
    a = [int(i) for i in f]
    s = 0
    for i in a:
        if i < 0:
            s += i

c = 0
ms = 0
for i in range(len(a)-2):
    print(a[i: i+3])
    su = min(a[i: i+3]) * max(a[i:i+3])
    if su > s:
        c += 1
        ms = max((sum(a[i:i+3])), ms)
print(c, abs(ms))