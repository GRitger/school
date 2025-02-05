from itertools import *
count=0
for i in product("01234567", repeat=3):
    x = "".join(i)
    qwe = x
    for  j in "02468":
        qwe = qwe.replace(j,"0")
    for  j in "13579":
        qwe= qwe.replace(j,"1")
    if x[0] != "0" and x[0] != x[1] and x[0] != x[2] and x[1] != x[2] and qwe.count("11") == 0 and qwe.count("00") == 0 :
        count += 1

print(count)