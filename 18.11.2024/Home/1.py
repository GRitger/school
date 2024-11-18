from itertools import *
count=0
for i in product("01234567", repeat=3):
    x = "".join(i)
    if x[0] != "0" and x[0] != x[1] and x[0] != x[2] and x[1] != x[2]:
        count += 1

print(count)