from itertools import *

st = "бенрстья"
c =0
index = 1
for i in product(st, repeat=5):
    x = "".join(i)
    if x[0] =="р" and x.count("ь") == 0 and index %2 == 0:
        c = index
    index+= 1
print(c)