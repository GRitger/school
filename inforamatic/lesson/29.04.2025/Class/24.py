with open("24-191.txt") as f:
    st = f.readline()
    c = 0
st = st.replace("A", " A")
st = st.replace("B", "B ")
a = st.split()
for i in a:
    if 0 < len(i) <=15 and i[0] == "A" and i[-1] == "B" and "F" in i:
        c += 1
print(c)