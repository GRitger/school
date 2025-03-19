with open("24.txt") as f:
    st = f.readline()
while "++" in st or "--" in st or "+-" in st or "-+" in st:
    st = st.replace("++", " ")
    st = st.replace("--", " ")
    st = st.replace("+-", " ")
    st = st.replace("-+", " ")
    st = st.replace("-0", " ")
    st = st.replace("+0", " ")

a = st.split()
a.sort(key=len)
for i in range(len(a)):
    if len(a[i]) > 2:
        while a[i][0] in "+-":
            a[i] = a[i][1:]
        while a[i][-1] in "+-":
            a[i] = a[i][:-1]
print(a)
