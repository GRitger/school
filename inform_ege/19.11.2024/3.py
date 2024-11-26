with open ("3.txt") as f:
    st = f.readline()
a = st.split("A")
ans = 0
for i in range(len(a)-1):
    ans= max(ans, len(a[i]) + len(a[i+1])+1)
print(ans)