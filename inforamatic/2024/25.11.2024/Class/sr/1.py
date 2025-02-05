with open ("1.txt") as f:
    s = f.readline()

s = s.replace("A", "E")
a = s.split("E")
a.sort(key=len)
print(len(a[-1]))

