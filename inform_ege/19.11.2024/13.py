with open ("13.txt") as f:
    st = f.readline()
for i in "QZXSWVRTGNHYUJMIKLOP":
    st = st.replace(i, ".")
a = st.split(".")
a.sort(reverse=False,key=len)
print(len(a[-1]))