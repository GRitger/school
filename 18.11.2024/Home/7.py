from itertools import *

count = 0
index = 1
for i in product("агемнрту", repeat=5):
    x = "".join(i)
    if x[0] != 'г' and x.count("е") >= 3 and index % 2 == 1:
        count += 1
    index += 1
print(count)
