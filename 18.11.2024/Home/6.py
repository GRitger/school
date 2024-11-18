from itertools import *

count = 0
for i in product("01234567", repeat=5):
    x = "".join(i)
    qwe = x
    for j in "02468":
        qwe = qwe.replace(j, "0")
    for j in "13579":
        qwe = qwe.replace(j, "1")
    if x.count("2") == 0 and x[0] != "0" and x.count(x[0]) == 1 and x.count(x[1]) == 1 and x.count(
            x[2]) == 1 and x.count(x[3]) == 1 and x.count(x[4]) == 1 and qwe.count("11") == 0 and qwe.count("00") == 0:
        count += 1

print(count)
