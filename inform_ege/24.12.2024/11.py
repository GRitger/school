with open("11.txt") as f:
    st = f.readline()

print(len(st))
i = 0
j = 1
m = -100000000000000000000000000000000000000000000000000000000000000000000000000000000
while j < len(st) -1:
    temp = st[i:j+1]
    if temp.count("CD") < 160:
        j += 1
    elif temp.count("CD") == 160:
        j += 1
        m = max(m, len(temp))
    elif temp.count("CD") > 160:
        i += 1
print(m)