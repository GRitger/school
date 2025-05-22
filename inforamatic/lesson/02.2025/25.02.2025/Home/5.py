a = []
for i in range(1,1000):
    r = bin(i)[2:]
    if r.count("1") % 2 == 0:
        r = r + "0"
        r = "10" + r[2:]
    else:
        r = r + "1"
        r = "11" + r[2:]
    R = int(r, 2)
    if R < 35:
        a.append(i)

print(max(a))