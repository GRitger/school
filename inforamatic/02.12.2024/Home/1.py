from math import *

n = 1789
i = ceil(log2(n))
for e in range(1,10000):
    if ceil(((i*70)+(5*7))/8) <= 200000000000:
        print((3*2**20-ceil(((i*70)+(5*7))/8))/16384)