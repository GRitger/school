for i in range(10000):
    n = i
    r = bin(i)
    r = r[2:]
    if r.count("1") % 2 == 0:
        r = "10" + r[2:] + "0"
    else:
        r = "11" + r[2:] + "1"
    if 40 < int(r, 2) < 1000000000000000000:
        print(i, int(r, 2))
    #print(i, int(r, 2))
