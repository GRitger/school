with open("11.txt") as f:
    st = f.readline()

j= 0
i = 1
F = 0
a = []
while i < len(st):
    temp = st[j:i]
    c = temp.count("F")
    if c >= 2025:
        a.append(len(temp))
        j += 1
    if c < 2025:
        i += 1

print(min(a))
