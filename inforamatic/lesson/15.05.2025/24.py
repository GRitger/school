with open("24.txt") as f:
    st = f.read()

st = st.replace(".", ".+")
a = st.split("+")
m = 0
ans = ""

for t in a:
    i = t
    if "  " in t:
        i = t.split("  ")[-1]
    if i[0] == " ":
        i = i[1:]
    if i[0] not in "NLD":
        N = 10 ** 100
        L = N
        D = N
        if i.find("N") != -1:
            N = i.find("N")
        if i.find("L") != -1:
            L = i.find("L")
        if i.find("D") != -1:
            D = i.find("D")
        ind = min(L, N, D)
        if ind == 10**100:
            continue
        i = i[ind:]
    if len(i) > 0 and i[0] in "LND":
        if i[-2] in "lnd":
            b = i.split()
            c = 0
            temp = []
            for j in b:
                if b.count(j) > 1 and j not in temp:
                    c+= 1
                    temp.append(j)
            if c <= 2:
                if len(i) > m :
                    m = len(i)
                    ans = i
print(m, ans)