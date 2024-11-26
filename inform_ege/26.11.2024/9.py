from math import *

n = 70
i = ceil(log2(10 + 60))
for e in range(1, 1000):
    if ceil(i * e / 8) * 999 > 88 * (2 ** 10):
        print(e)
        break