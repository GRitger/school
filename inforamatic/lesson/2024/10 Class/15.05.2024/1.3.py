with open("k7-m2.txt") as f:
    t = f.readline()
d = 0
md = 0
coun = 0
for i in t:
    if i in "C":
        if d == 0:
            coun += 1
        d += 1
        md = max(d, md)
    else:

        d = 0
print(md, coun, len(t))