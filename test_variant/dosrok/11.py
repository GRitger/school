from math import *
l = 257
for n in range(1,   100000):
    i = ceil(log2(n))
    b = ceil(i*l/8)
    if 295740*b <= 33 *2 **20:
        print(n)