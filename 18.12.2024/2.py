print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (((z==x) <= w) and (w <= (y and x)))
                if f:
                    print(x,y,w,z)