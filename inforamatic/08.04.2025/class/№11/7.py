from math import *

l = 248
for n in range(1, 1000000):
    i = ceil(log2(n))
    b = ceil(i * l / 8)
    if (b)*75600 <= 16 * 2 ** 20:
        print(n)
