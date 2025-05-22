for m in range(50):
    for n in range(50):
        if m % 2 == 1 and n % 2 == 0:
            if 100000000 < 2**m * 7**n < 300000000:
                print(2**m * 7**n, m+n)