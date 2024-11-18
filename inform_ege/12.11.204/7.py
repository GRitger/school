from itertools import *

st = "совести"
c = 0
index = 0
qwe = set(permutations(st))
for i in qwe:
    x = "".join(i)
    for i in "свст":
        x = x.replace(i, "0")
    for i in "оеи":
        x = x.replace(i, "1")
    if not(x.count("00") > 0 and x.count("11") > 0):
        index += 1
print(index)
