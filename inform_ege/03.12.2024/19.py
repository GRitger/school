with open("19.txt") as f:
    s = f.readline()

s = s.replace("X", " X")
a = s.split()

a.sort(key=len)
y = a[0].count("Y")
m = len(a[0])
for i in range(len(a)-1, -1,-1):
    if a[i].count("Y") >= y:
        m = len(a[i])
        print(a[i])
        y = a[i].count("Y")
print(m+1)