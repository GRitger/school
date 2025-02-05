with open ("2.txt") as f:
    s = f.readline()

s = s.replace("P", "0")
s = s.replace("R", "1")
a = s.split("01")
for i in range(len(a)):
    a[i] = a[i].split("10")
m = 0
for i in a:
    for j in i:
        m = max(len(j), m )
print(m)

