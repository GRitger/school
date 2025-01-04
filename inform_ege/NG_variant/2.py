print("y z w x")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((x <= w) == y) <= (z==x)
                if not f and y:
                    print(y,z,w,x)