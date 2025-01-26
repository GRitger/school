
for n in range(1000):
    st = ">" + "0"*17 + n*"3" + 17*"2"
    while ">3" in st or ">2" in st or ">0" in st:
        if ">3" in st:
            st = st.replace(">3", "22>")
        elif ">2" in st:
            st = st.replace(">2", "2>")
        elif ">0" in st:
            st = st.replace(">0", "3>")
    su = 0
    for i in st:
        if i != ">":
            su += int(i)
    if int(su**0.5) == su **0.5:
        print(n)
        break