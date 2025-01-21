with open("11.txt") as f:
    st = f.readline()

j= 0
i = 1
F = 0
a = []
while i < len(st):
    temp = st[j:i]
    A = temp.count("A")
    B = temp.count("B")
    if A > 200 or B > 25:
        j += 1
    elif A == 200 and B == 25:
        i += 1
        a.append(i-j)
    else:
        i += 1

print(max(a)-1)
