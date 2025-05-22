with open("24.txt") as f:
    st = f.readline()

i = 0
j = 1
m = 0
ans = ""
while j < len(st):
    temp = st[i:j]
    c = temp.count("A")
    f = temp.count("F")
    if c == 22 and f == 0:
        if len(temp) > m:
            m = len(temp)
            ans = temp
        j += 1
    else:
        if f > 0:
            i += 1
        if c < 22:
            j += 1

print(m, ans)