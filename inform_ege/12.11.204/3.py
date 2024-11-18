from itertools import *

st = "агемнрту"
c =0
index = 1
for i in product(st, repeat=4):
    x = "".join(i)
    if len(set(x)) and x[0]<x[1]<x[2]<x[3]:
        c = index
    index+= 1
print(c)