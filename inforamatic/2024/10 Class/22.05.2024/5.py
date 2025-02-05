with open("24-4.txt") as f:
    st = f.readline()

l = 1
ml = 1
s = ""
for i in range(1, len(st)):
    if st[i] == st[i-1]:
        l += 1
        if l > ml:
            ml = l
            s = st[i]
    else:
        l = 1
print(ml*s)