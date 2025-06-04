from string import ascii_lowercase
with open("24-292.txt") as f:
    st = f.readline().lower()

for i in ascii_lowercase:
    if i not in "xyz":
        st = st.replace(i, " ")

st = st.replace("xxx", "xx xx")
st = st.replace("yyy", "yy yy")
st = st.replace("zzz", "zz zz")
st = st.replace("xxx", "xx xx")
st = st.replace("yyy", "yy yy")
st = st.replace("zzz", "zz zz")
st = st.replace("xxx", "xx xx")
st = st.replace("yyy", "yy yy")
st = st.replace("zzz", "zz zz")
a = st.split()
a.sort(key = len)
print(len(a[-1]))