from itertools import product
count = 0
st = "0123456789abcdef"
for i in product(st , repeat=3):
    x = "".join(i)
    if int(x[0], 16) > int(x[1], 16) > int(x[2], 16):
        count += 1
for i in product(st , repeat=5):
    x = "".join(i)
    if int(x[0], 16) > int(x[1], 16) > int(x[2], 16) > int(x[3], 16) > int(x[4], 16):
        count += 1
print(count)