with open ("1.txt") as f:
    st = f.readline()
count = 0
ans = 0
st = st.replace("A", "E")
a = st.split("E")
a.sort(reverse=True,key=len)
print(len(a[0]))