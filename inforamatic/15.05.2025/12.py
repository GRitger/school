from itertools import permutations

def s(x):
    su= 0
    for i in x:
        if i != ">":
            su+= int(i)
    return su

for n in range(1, 10000):
    st = 28* "2" + n*"7" + 11*"5"
    st = ">" + st
    while ">5" in st or ">7" in st or ">2" in st:
        if ">5" in st:
            st = st.replace(">5", "77>", 1)
        if ">7" in st:
            st = st.replace(">7", "222>", 1)
        if ">2" in st:
            st = st.replace(">2", "55>", 1)
    if s(st) > 1000 and s(st) % 20 == 0:
        print(n)
        break