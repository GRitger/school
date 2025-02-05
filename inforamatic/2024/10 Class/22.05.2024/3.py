with open("k8-0.txt") as f:
    st = f.readline()

l = 1
ml = 0
count = 0
t = True
s = ""
st = "111222"
for i in range(1, len(st)):
    if st[i] == st[i-1]:
        l += 1
        ml = max(ml, l)
    else:
        l = 1

for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        l += 1
        if ml == l and t:
            s = st[i]
            t = False
    else:
        l = 1

print(s, ml)