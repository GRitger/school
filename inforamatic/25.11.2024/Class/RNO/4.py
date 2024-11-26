with open ("4.txt") as f:
    s = f.readline()

s = s.replace("-", "*")
s = s.replace("**", "* *")
s = s.replace("*0", "* 0")
a = s.split()
m = 0
for i in a:
    while len(i) and i[0] in "0*":
        i = i[1:]
    while len(i) and i[-1] in "*":
        i = i[:-1]
    m = max(m, len(i))
print(m)
'''
m = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        m = max(m, len(a[i][j]))

print(m).txt") as f:
    s = f.readline()

s = s.replace("QW", "Q W")

a = s.split()

a.sort(key=len)

print(len(a[-1]))'''