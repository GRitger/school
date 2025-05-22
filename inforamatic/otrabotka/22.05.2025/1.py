with open("1.txt") as f:
    st = f.readline().lower()

ind = [0]* len(st)
c = 0
if st[0] == "a":
    ind[0] += 1
for i in range(1, len(st)):
    if st[i] == "a":
        ind[i] = ind[i-1] + 1
        c += ind[i-2]
    else:
        ind[i] = ind[i-1]

print(c)