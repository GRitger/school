for n in range(4, 10000):
    st = "3" + n*"1"

    while "31" in st or "211" in st or "1111" in st:
        if "31" in st:
            st = st.replace("31", "1",1)
        if "211" in st:
            st = st.replace("211", "13",1)
        if "1111" in st:
            st = st.replace("1111", "2",1)
    s =0
    s = sum([int(i) for i in st ])
    if s == 15:
        print(n)