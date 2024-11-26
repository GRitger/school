from itertools import *

count = 0
index = 1
for i in product("аукцион", repeat=4):
    x = "".join(i)
    if x.count("о") ==1:
        count += 1
    index += 1
print(count)
