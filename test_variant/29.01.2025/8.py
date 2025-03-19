from itertools import product

c = 0
for x in product([i for i in range(25)], repeat = 4):
    if x[0] != 0:
        if len([j for j in x if j % 2 == 0]) >= 1 and len([q for q in x if q > 15]) > 2:
            c += 1
print(c)