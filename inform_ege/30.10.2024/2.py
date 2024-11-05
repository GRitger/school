from itertools import product

st = "0123456"
count = 0
for i in product(st, repeat= 7):
    x = "".join(i)
    if x[0] != "0" and x.count("0") + x.count("2") + x.count("4") + x.count("6") == 2 :
        count += 1
print(count)