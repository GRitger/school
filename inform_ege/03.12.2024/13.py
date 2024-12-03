with open ("13.txt") as f:
    s = f.readline()

a = s.split("F")
m = 0
for i in range(len(a)-1):
    m = max(m, len(a[i])+ len(a[i+1])+1)
print(m)