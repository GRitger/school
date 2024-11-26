with open ("7.txt") as f:
    st = f.readline()
c = 0
for i in "0123456789":
    st = st.replace(i, "0")
a = st.split("0")
print(a)
for i in a:
    if len(i) == 5:
        c += 1
a.sort(reverse=True,key=len)
print(c)