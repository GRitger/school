from itertools import *

st = "10"
c = 0
index = 0
for i in product(st, repeat=12):
    x = "".join(i)
    if x.count("1") == 7 and x.count("0") ==5 and x.count("00000") == 0:
        c += 1
print(index)
