with open("24_1.txt") as f:
    st = f.readline()
st = st.replace("+", "*")
while "**" in st:
    st = st.replace("**", "* *")

a = st.split()

a.sort(key=len)

for i in a:
    print(i, len(i))
