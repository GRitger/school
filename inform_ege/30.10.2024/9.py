from itertools import product
count = 0
st = "0123456789abcd"
for i in product(st , repeat=5):
    x = "".join(i)
    if x[0] != "0" and (x[-1] == "0" or x[-1] == "3"):
        t = []
        for i in x:
            if not (i in t):
                t.append(i)
        if len(t) == 2:
            count += 1
print(count)