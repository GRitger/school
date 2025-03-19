for n in range(1000):
    st = ">" + 17 * "0" + n * "3" + 17 * "2"
    while ">3" in st or ">2" in st or ">0" in st:
        if ">3" in st:
            st = st.replace(">3", "22>")
        elif ">2" in st:
            st = st.replace(">2", "2>")
        elif ">0" in st:
            st = st.replace(">0", "3>")
    st = st.replace(">", "0")
    st = st.replace("0", "0 ")
    st = st.replace("2", "2 ")
    st = st.replace("3", "3 ")

    a = st.split()

    for j in range(len(a)):
        a[j] = int(a[j])

    if int(sum(a) ** 0.5) == sum(a) ** 0.5:
        print(sum(a))
        print(n)
        break
