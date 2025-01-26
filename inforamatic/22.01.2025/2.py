#print("x y w z")
print("z x y w")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x or (not (y))) and (not (x == z))
                if f:
                    print(z,x,y,w)
