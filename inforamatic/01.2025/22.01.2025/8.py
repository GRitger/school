from itertools import product
from timeit import repeat
n = 0
for i in product("0123456789AB", repeat=6):
    st = "".join(i)
    if st[0] != "0":
        for j in "02468A":
            st = st.replace(j, "0")
        if st.count("B") == 1 and st.count("0") == 3:
            n += 1
print(n)
