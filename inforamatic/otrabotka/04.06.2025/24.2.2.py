from string import ascii_lowercase
with open("24-292.txt") as f:
    st = f.readline().lower()

for i in ascii_lowercase:
    if i not in "xyz":
        st = st.replace(i, "*")

ans = 0
k = 0
for i in range(1, len(st) - 2, 2):
    if st[i:i+2] in ("xx","yy","zz") and st[i:i+2] != st[i-2:i]:
        k += 2
        ans = max(ans, k)
    else:
        if st[i:i+2] == st[i-2:i]:
            k = 2
        else:
            k = 0
print(ans)