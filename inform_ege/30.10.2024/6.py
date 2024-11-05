from itertools import product
count = 0
st = "01234567"
for i in product(st, repeat=5):
    x = "".join(i)
    if not (x[0] in "013579") and not (x[-1] in "26") and x.count("7") <= 2:
        count += 1
print(count)