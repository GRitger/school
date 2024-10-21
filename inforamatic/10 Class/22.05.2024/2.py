with open("k7a-6.txt") as f:
    st = f.readline()

l = 0
ml = 0

for i in st:
    if i in "BCF":
        l += 1
        ml = max(l, ml)
    else:
        l = 0
print(ml)