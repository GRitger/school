
from itertools import product
count = 0
st = "0123456"
for i in product(st, repeat=6):
    x = "".join(i)
    nech = 0
    ch = 0
    for j in x:
        if j in "02468":
            ch += 1
        else:
            nech += 1
    if x[0] != "0" and not (x[-1] in "0123") and  ch == nech:
        count += 1
print(count)