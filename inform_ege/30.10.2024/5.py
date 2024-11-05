from itertools import product
count = 0
st = "012345678"
for i in product(st , repeat=7):
    x = "".join(i)
    if x[0] != "0" and x[0] != "2" and x[0] != "4" and x[0] != "6" and not(x[-1] == x[-2] == x[-3]):
        count += 1
print(count)