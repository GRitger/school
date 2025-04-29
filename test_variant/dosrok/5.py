a = []
for i in range(1, 1000):
    st = bin(i)[2::]
    if st.count("1") % 2 == 0:
        st = "10" + st[2:] + "0"
    else:
        st = "11" + st[2:] + "1"
    R = int(st,2)
    if R > 480:
        a.append(i)
print(min(a))