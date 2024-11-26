from math import *

n = 10+52+458
i = ceil(log2(n))
for e in range(1,1000):
    if ceil(e*i/8) * 862 <= 276 * (2**10):
        print(e)