from itertools import permutations

c = 0
for i in permutations ("0123456789", 6):
    x = ''.join(i)
    if int(x) % 4 == 0 and x[0] != "0":
        for qwe in "02468":
            x = x.replace(qwe, "2")
        if x.count("22") == 0:
            c += 1
print(c)
