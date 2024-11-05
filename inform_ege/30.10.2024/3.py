from itertools import product
count = 0
st = "0123456789abcde"
for i in product(st , repeat=5):
    x = "".join(i)
    if x[0] != "0" and x.count("8") == 1 and x.count("a") + x.count("b") + x.count("c") + x.count("d") + x.count("e") >= 2:
        count += 1
print(count)