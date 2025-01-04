for A in range(1000):
    f = True
    for x in range(100):
        for y in range(100):
            f *= (15 < x*x+y*y)or (abs(x) +  abs(y) < A)
    if f:
        print(A)