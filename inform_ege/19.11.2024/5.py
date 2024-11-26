with open ("5.txt") as f:
    st = f.readline()

st = st.replace("X", "Z")
st = st.replace("Y", "Z")
while "ZZ" in st:
    st = st.replace("ZZ", "Z Z")
a = st.split(" ")
a.sort(reverse=True,key=len)
print(len(a[0]))