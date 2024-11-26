from math import *

n = 10+26+450
i = ceil(log2(n))
for e in range(1,1000):
    if ceil(e*i/8) * 708 > 213 * (2**10):
        print(e)