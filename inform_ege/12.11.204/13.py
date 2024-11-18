with open("24_3.txt") as f:
    st = f.readline()
st = st.replace("A", "A")
st = st.replace("B", "A")
st = st.replace("C", "A")

st = st.replace("6", "1")
st = st.replace("7", "1")
st = st.replace("8", "1")
st = st.replace("9", "1")

while "AA" in st:
    st = st.replace("AA", "A A")
while "11" in st:
    st = st.replace("11", "1 1")

a = st.split()

a.sort(key=len)

print(len (a[-1]))
