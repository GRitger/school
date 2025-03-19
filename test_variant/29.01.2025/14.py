for a in range(1, 10000000):
    f = False
    for x in "0123456789ABCDE":
        m = int("432" + x + "3", 15)
        n = int("86" + x + "86", 15)
        f = ((m+a) % n == 0)
        if f:
            print(a)
            break