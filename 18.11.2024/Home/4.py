from itertools import *
count=0
for i in product("0123456", repeat=6):
    x = "".join(i)
    if int(x[0]) > int(x[1]) > int(x[2]) > int(x[3]) > int(x[4]) > int(x[5]) and x[0] != "0" :
        count += 1

print(count)