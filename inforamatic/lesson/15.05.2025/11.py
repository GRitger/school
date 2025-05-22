from math import *
l = 71118
for N in range(1,2000000):
    i = ceil(log2(N))
    if i*l*12288 < 2*2**33:
        print(N)