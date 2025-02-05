with open ("2.txt") as f:
    s = f.readline()

s = s.replace("QW", "Q W")

a = s.split()

a.sort(key=len)
print(a[-1])
print(len(a[-1]))