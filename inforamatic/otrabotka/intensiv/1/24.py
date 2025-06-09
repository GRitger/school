from string import ascii_lowercase
with open("24-278.txt") as f:
    st = f.readline().lower()
    alf = "qazwsxedcrvtgbyhujmiop13579"
    for i in alf:
        st = st.replace(i, "*")

k = 0
ans = 0
for i in range(1,len(st)):
    if st[i] in "knlf":
        k += 1
    else:
        if st[i] in "02468" and st[i] == st[i-k-1]:
            ans = max(ans,k)
        k = 0
print(ans)