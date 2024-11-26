with open ("9.txt") as f:
    st = f.readline()
c = 0
for i in "QAZXSWEDCVFRTGBNHYUJMIKLOP":
    st = st.replace(i, "A")
a = st.split("A")
a.sort(reverse=False,key=len)
for i in a:
    if len(i) and i[-1] in "02468":
        print(i)
print(c)