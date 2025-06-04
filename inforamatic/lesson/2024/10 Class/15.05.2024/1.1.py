with open("k7a-1.txt") as f:
    t = f.readline()
d = 0
md = 0
for i in t:
    if i in "ABC":
        d += 1
        md = max(d, md)
    else:
        d = 0
print(md)