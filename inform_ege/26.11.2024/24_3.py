with open("24_3.txt") as f:
    s = f.readline()
s = s.replace("B", "$B")
s = s.replace("A", " ")
s = s.replace("D", " ")
s = s.replace("C", " ")
s = s.replace("-", "*")
s = s.replace("**", " ")
a = s.split("$")
m =0
for i in range(len(a)):
    a[i] = a[i].split()
    if len(a[i]) and len(a[i][0])and a[i][0][-1] == "*":
        a[i][0]= a[i][0][:-1]
    if len(a[i]) and len(a[i][0]) >1 and a[i][0][1] in "0123456789":
        if len(a[i][0])+1 > m:
            m = max(m, len(a[i][0]))
            print(m, a[i][0])

print(m)
"""
for i in a:
    while len(i) and i[0] in "0*":
        i = i[1:]
    while len(i) and i[-1] in "*":
        i = i[:-1]
    arr.append(i)

arr.sort(key = len)

for i in arr:
    print(i, i.count("*")+ 1)
    """
