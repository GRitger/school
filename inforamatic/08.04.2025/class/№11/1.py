from math import *

l = 23
for n in range(1, 1000000):
    i = ceil(log2(n))
    b = ceil(i*l/8)
    if 500000 * b <= 21 * 2**20:
        print(n)