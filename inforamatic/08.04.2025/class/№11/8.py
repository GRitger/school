from math import *

l = 248
for l in range(1, 1000000):
    i = ceil(log2(26+10+450))
    b = ceil(i * l / 8)
    if (b)*575 > 100 * 2 ** 10:
        print(l)
        break