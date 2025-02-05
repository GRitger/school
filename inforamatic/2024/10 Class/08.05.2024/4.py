for i in range(10000):
    n = i
    r = bin(i)
    r = r[2:]
    if r.count("1") % 2 == 0:
        r = "11" + r[2:] + "00"
    else:
        r = "10" + r[2:] + "11"

    if r.count("1") % 2 == 0:
        r = "11" + r[2:] + "00"
    else:
        r = "10" + r[2:] + "11"
    if int(r, 2) < 100:
        print(i, int(r, 2))
