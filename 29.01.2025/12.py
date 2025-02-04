def f(x):
    s = 0
    for i in x:
        s += int(i)
    return s

a = []
for i in range (4, 10000):
    st = "8" + (i * "4")
    while "11" in st or "444" in st or "8888" in st:
        if "11" in st:
            st = st.replace("11", "4", 1)
        if "444" in st:
            st = st.replace("444", "88", 1)
        if "8888" in st:
            st = st.replace("8888", "1", 1)
    a.append(f(st))
    if f(st) == 106:
        print(st, i)
print(max(a))