from itertools import product
count = 0
st = "012345678"
for i in product(st, repeat=7):
    x = "".join(i)
    if not (x[0] in "013579") and not(x[-1] in "036") and x.count("6") >= 1:
        count += 1
print(count)