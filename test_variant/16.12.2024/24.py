with open ("24.txt") as f:
    s = f.readline()

s = s.replace("A", "2")
s = s.replace("E", "2")
s = s.replace("B", "1")
s = s.replace("C", "1")
s = s.replace("D", "1")
s = s.replace("G", "1")
s = s.replace("H", "1")
s = s.replace("F", "1")

s = s.replace("112", "112 ")

a = s.split()

a.sort(key=len)
print(len(a[-1]))