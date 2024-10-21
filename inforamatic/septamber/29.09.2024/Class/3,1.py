for i in range(1245//51*51, 10**6, 51):
    st = str(i)
    if st[0:2] == "12" and st.count("45") >0 :
        print(i, i //51)