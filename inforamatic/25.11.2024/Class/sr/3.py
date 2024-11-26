with open ("3.txt") as f:
    s = f.readline()

a = s.split(".")

m = 0
for i in a:
    if "AAA" in i:
        m = max(m, len(i))

print(m)