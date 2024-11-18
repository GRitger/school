from itertools import *

count = 0
index = 1
for i in product("ангел", repeat=5):
    x = "".join(i)
    if x.count("е") >= 1 and x[0] != "а" :
        count += 1
    index += 1
print(count)
