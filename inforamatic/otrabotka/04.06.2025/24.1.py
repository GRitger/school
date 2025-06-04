from string import ascii_uppercase, ascii_lowercase

with open("24-332.txt") as f:
    st = f.readline()
alf = ascii_uppercase
for i in ascii_uppercase:
    st = st.replace(i, "A")
for i in ascii_lowercase:
    st = st.replace(i, "b")
st = st.replace("  ", "*")
st = st.replace(" .", "*")
st = st.replace(".", ".*")
st = st.replace("bA", "b*A")
ans = []
while "AA" in st:
    st = st.replace("AA", "A*A")
a = st.split("*")
a.sort(key=len)
for i in a:
    b = i.find("A")
    if b == -1:
        continue
    i = i[b:]
    if i[-1] == ".":
        ans.append(i)
ans.sort(key=len)
print(len(ans[-1]))


