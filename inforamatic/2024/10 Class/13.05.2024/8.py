p = 13
q = 17
e = 11
for d in range(1271):
    if (d*e) %((p-1) * (q - 1)) == 1:
        print(d)