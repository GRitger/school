for A in range(10000):
    f = True
    for x in range(100):
        for y in range(100):
            f *= (x >= 27) or (2*x < 3*y) or ((x+2)*(y-3)< A)
    if f:
        print(A)
        break