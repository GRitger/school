with open("k8-0.txt") as f:
    t = f.readline()
    print(t)
d = 0
md = 0
for i in range(1, len(t)):
    if t[i] == t[i-1]:
        d += 1
        md = max(d, md)
    else:
        d = 0
print(md)