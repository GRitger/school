p = 4
q = 7
e = 13
for d in range(10000):
    if (d*e) %((p-1) * (q - 1)) == 1:
        if d < 75:
            print(d)