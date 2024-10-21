from itertools import *

for k in range(4):
    for i in product("0123456789", repeat=k):
        i = "".join(i)
        for j in '0123456789':
            s = "1" + j + "234" + i + "6"
            if int(s) % 2024 == 0:
                print(s, int(s) // 2024)
