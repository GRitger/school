with open ("24-298.txt") as f:
    s = f.readline()

s = s.replace("-", "*")
s = s.replace("**", "* *")
a = s.split()
for i in range(len(a)):
    a[i] = a[i].split("*0")
m = 0
for i in a:
    while len(i) and i[0] in "0*":
        i = i[1:]
    while len(i) and i[-1] in "*":
        i = i[:-1]
    m = max(m, len(i))
print(m)

