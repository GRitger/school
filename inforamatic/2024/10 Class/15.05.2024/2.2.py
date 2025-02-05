with open("k7a-6.txt") as f:
    t = f.readline()
d = 0
md = 0
for i in t:
    if i in "BCDF":
        d += 1
        md = max(d, md)
    else:
        d = 0
print(md)