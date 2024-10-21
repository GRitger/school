q = int("3146", 8)
for i in range(8):
    for j in range(8):
        ch = int("2" + str(i) + str(j) + "5", 8)
        chp = int("52" + str(i) + str(j), 8)
        if ch + q == chp:
            print(i, j)

print(hex(int("2035", 8)))