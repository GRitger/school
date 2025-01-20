from itertools import *
v = 0
p = 0
for i in permutations("0000000111", 6):
    st = "".join(i)
    v += 1
    if st.count("1") == 3:
        p += 1
print(p)
