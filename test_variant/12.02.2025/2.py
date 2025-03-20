print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (y <= z) and (w==(x <= y)) and (not x)
                if f:
                    print(x,y,w,z)