with open ("ECjxYCSUU.txt") as f:
    s = f.readline()

a = s.split("Y")
for i in range(len(a)):
    a[i] = a[i].split("......")

m = 0
for i in a:
    for j in i:
        m = max(m, len(j))

print(m)