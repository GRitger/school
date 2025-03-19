from itertools import *

c = 0
for i in product("0123456", repeat=6):
    x = "".join(i)
    for i in "246":
        x = x.replace(f'0{i}', "*")
        x = x.replace(f'{i}0', "*")
    if x[0] != "0" and x.count("0") == 1 and x.count("*") == 0:
        c += 1
        print(x)
print(c)
