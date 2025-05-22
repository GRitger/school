from itertools import *

count = 0
index = 1
for i in product("аукцион", repeat=4):
    x = "".join(i)
    if x.count("о") ==2 and x[1] != "к" :
        count += 1
    index += 1
print(count)
