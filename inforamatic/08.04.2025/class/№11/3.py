from math import *

l = 303
for x in range(1, 1000000):
    i = ceil(log2(10 + 8190))
    b = ceil(i*l/8)
    if (b+x)*101    <=101 * 2 ** 10:
        print(x)