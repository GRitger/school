with open("24_5.txt") as f:
    s = f.readline()
s = s.replace("**", " ")
s = s.replace("++", " ")
s = s.replace("+*", " ")
s = s.replace("*+", " ")
a = s.split()
m = 0
a.sort(key=len, reverse=True)
for i in a:
    if len(i) > m:
        if len(i) > 1 and i[0] in "+*":
            i = i[1:]
        if len(i) > 1 and i[-1] in "+*":
            i = i[:-1]
        b = i.split("+")
        l = 0
        for st in b:
            if "0" in st.split("*"):
                l += len(st) + 1
            else:
                l = 0
        m = max(m, l)
    else :
        break
# a[-1] = a[-1].replace("*")
print(m-1)
