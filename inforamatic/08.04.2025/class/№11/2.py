from math import *

l = 20
for n in range(1, 1000000):
    i = ceil(log2(n))
    b = ceil(i*l/8)
    if 600000 * b > 11 * 2**20:
        print(n)
        break