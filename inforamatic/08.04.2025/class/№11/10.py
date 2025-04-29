from math import *

l = 25
for x in range(1, 1000000):
    i = ceil(log2(26+26+10 + 465))
    b = ceil(i * l / 8)
    if (b +x) * 1500 <= 77 * 2 ** 10:
        print(x)
