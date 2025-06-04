from string import ascii_uppercase
with open("24-332.txt") as f:
    st = f.readline()
st = st.replace("  ", ".")
alf = ascii_uppercase
for i in alf:
    st = st.replace(i, "A")
a = []
begin = st.find("A")
end = st.find(".")
while begin != -1:
    temp = st[begin:end+1]
    st = st[begin+1:]
    a.append(temp)
    begin = st.find("A")
    end = st.find(".")

a.sort(key = len)
print(a)


