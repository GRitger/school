with open("24_1.txt") as f:
    s = f.readline()

s = s.replace("+", "*")
s = s.replace("**", "* *")
s = s.replace("*0", "* 0")

a = s.split()
arr = []

for i in a:
    while len(i) and i[0] in "0*":
        i = i[1:]
    while len(i) and i[-1] in "*":
        i = i[:-1]
    arr.append(i)

arr.sort(key = len)

for i in arr:
    print(i, len(i)-i.count("*"))
