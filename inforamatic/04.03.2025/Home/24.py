with open("24.txt") as fil:
    st = fil.readline()

st = st.replace("Y", "X")

i = 1
j = 0
m = 0
while i <= len(st):
    temp = st[j:i]
    c = temp.count("X")
    if c <= 5:
        i += 1
        m = max(m, len(temp))
    else:
        j += 1
print(m)