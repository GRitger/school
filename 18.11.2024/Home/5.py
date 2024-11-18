from itertools import *
count=0
for i in product("01234567", repeat=5):
    x = "".join(i)
    if x.count("2") == 0 and x[0] != "0" :
        count += 1

print(count)