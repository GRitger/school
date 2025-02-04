with open("24.txt") as f:
    st = f.readline()

st = st.replace("B", "AB" )
st = st.replace("C", "A" )
st = st.replace("D", "A" )
st = st.replace("*", "A" )
while "++" in st:
    st = st.replace("++", "A")
while "--" in st:
    st = st.replace("--", "A")
while "+-" in st:
    st = st.replace("+-", "A")
while "-+" in st:
    st = st.replace("-+", "A")



a = st.split("A")
a.sort(key=len)

for i in range(len(a)):
    if len(a[i]) > 2:
        if a[i][0] in "+-":
            a[i] = a[i][1:]
        if a[i][-1] in "+-":
            a[i] = a[i][:-1]
l = 2
ans = []
for i in a:
    if len(i) == 20 and i[0] == "B" and i[1] in "0123456789":
        ans.append([i, len(i)])
        l = len(i)
print(ans)