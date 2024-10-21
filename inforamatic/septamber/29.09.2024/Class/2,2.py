from itertools import *

for k in range(3):
    for i in product("0123456789", repeat=k):
        i = "".join(i)
        for j in '0123456789':
            for temp in "0123456789":
                s = "3" + j + "12" + temp + "14" + i + "5"
                if int(s) % 1917 == 0:
                    print(s, int(s) // 1917)
