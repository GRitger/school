with open("24_5.txt") as f:
    st = f.readline()
st = st.replace("-", "*")
while "**" in st:
    st = st.replace("**", "* *")
st = st.replace("*0", "* 0")
a = st.split()
m = 0
for i in a:
    if i[-1] in "*":
        i = i[:-1]
    while len(i) and i[0] in "*0":
        i = i[1:]
    m = max(m, len(i))
print(m)
