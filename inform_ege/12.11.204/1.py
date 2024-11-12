from itertools import *

st = "косуф"
c =0
index = 0
for i in product(st, repeat=5):
    x = "".join(i)
    if x.count("ф") ==0 and x.count("у") == 2:
        c = index
    index+= 1
print(c+1)