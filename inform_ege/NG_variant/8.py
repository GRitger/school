from itertools import *

a = []
for i in product("аизм", repeat=5):
    x = "".join(i)
    if x.count("а") + x.count("и") == 1:
        a.append(x)
r = 1
for i in a:
    print(r, i)
    r += 1

