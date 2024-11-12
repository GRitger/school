from itertools import *

st = "просто"
c =0
index = 1
qwe = set(permutations(st))
for i in qwe:
    x = "".join(i)
    if x.count("оо") ==0:
        c +=1
    index+= 1
print(c)