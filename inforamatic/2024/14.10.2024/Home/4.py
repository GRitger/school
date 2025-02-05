from itertools import *
a = [(0, 0)]
for i in "13579":
    for k in range(6):
        for j in product("0123456789", repeat=k):
            j = "".join(j)
            if len(j) == 0 or j[-1] in "02468":
                s = int(i + "136" + j + "1")
                if s % 11071 == 0 and s < 10 ** 10:
                    a.append((s, s/11071))
a.sort()
print(*a)