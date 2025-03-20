for n in range(3, 10000):
    st = "2" + "5" * n
    while "25" in st or "355" in st or "555" in st:
        if "25" in st:
            st = st.replace("25", "5", 1)
        if "355" in st:
            st = st.replace("355", "522", 1)
        if "555" in st:
            st = st.replace("555", "3", 1)
    if st.count("2") == 10:
        print(n)
