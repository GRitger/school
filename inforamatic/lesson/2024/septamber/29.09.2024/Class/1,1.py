for i in range(103456709//17*17, 10**9, 17):
    st = str(i)
    if st[0] == "1" and st[-1] == "6" and st[2:7] == "34567":
        print(i, i //17)