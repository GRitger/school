for a in range(500):
    f = True
    for x in range(40):
        for y in range(1000):
            f *= ((x < 7) or (y >= (5 * x + a - 60)) or (x >= 36) or (y < 225))
        if f==0:
            break
    if f==1:
        print(a)

