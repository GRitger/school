with open ("3.txt") as f:
    s = f.readline()

s = s.replace("DD", "D D")

a = s.split()
m = 0
for i in a:
    if "FE" in i:
        m = max(m, len(i))
print(m)