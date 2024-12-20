with open("24.txt") as f:
    s = f.readline()

s = s.replace("2", "1")
s = s.replace("4", "1")
s = s.replace("Q", "W")
s = s.replace("R", "W")
s = s.replace("WW", "W W")
s = s.replace("11", "1 1")
while "WW" in s:
    s = s.replace("WW", "W W")

while "11" in s:
    s = s.replace("11", "1 1")
a = s.split()

a.sort(key=len)

print(len(a[-1]))