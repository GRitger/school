for i in range(30120145//1917*1917, 10**10, 1917):
    st = str(i)
    if st[0] == "3" and st[-1] == "5" and st[2:4] == "12" and st[5:7] == "14":
        print(i, i //1917)