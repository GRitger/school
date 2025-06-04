import itertools
c = 0
for i in itertools.product("0123456789abc", repeat=6):
    st = "".join(i)
    f = 1
    for t in "02468ac":
        for x in "abc":
            if st.count(t+x) + st.count(x+t):
                f *= 0
                break
        if f == 0:
            break
    if st[0] != "0" and f and st.count("1") == 2:
        c+=1
        #print(st)
print(c)