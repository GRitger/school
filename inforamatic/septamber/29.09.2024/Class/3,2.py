from itertools import *

for k in range(3):
    for z in range(3):
        if k + z > 2:
            continue
        for i in product("0123456789", repeat=k):
            i = "".join(i)
            for j in product("0123456789", repeat=z):
                j = "".join(j)
                s = "12" + i + "45" + j
                if int(s) % 51 == 0:
                    print(s, int(s) / 51)
