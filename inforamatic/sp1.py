for i in range(102346//2024*2024, 10**10, 2024):
    st = str(i)
    if st[0] == "1" and st[-1] == "6" and st[2:5] == "234":
        print(i, i //2024)