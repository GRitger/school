with open("17.txt") as f:
    s = f.readline()

s = s.replace("-", "*")
s = s.replace("**", "* *")
s = s.replace("A", " A")
s = s.replace("B", " ")
s = s.replace("C", " ")
s = s.replace("D", " ")

a = s.split()

m = 0

for i in range(len(a)- 1):

    while len(a[i]) and a[i][0] in "*0":
        a[i] = a[i][1:]
    while len(a[i]) and a[i][-1] in "*A":
        a[i] = a[i][:-1]
    if len(a[i]) > 0 and  a[i][0] in "A":
        #m = max(m, len(a[i]))
        if m < len(a[i]):
            print(a[i], len(a[i]))
            m = len(a[i])
print(m)