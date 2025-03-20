with open("24.txt") as f:
    st = f.readline()

st = st.replace("*", "+")
st = st.replace("++", " ")
st = st.replace(" +", " ")
for i in "12346789":
    st = st.replace(i+"+", i+" +")
a = st.split()
a.sort(key=len)
for i in a:
    print(i, len(i))