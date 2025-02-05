with open ("1.txt") as f:
    s = f.readline()

s = s.replace("W", "0")
s = s.replace("R", "0")
s = s.replace("Q", "0")

a = s.split("0")

a.sort(key=len)

print(len(a[-1]))