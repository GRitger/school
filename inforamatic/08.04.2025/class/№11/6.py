from math import *

l = 10 + 25
for n in range(1, 1000000):
    i = ceil(log2(n))
    b = ceil(i * l / 8)
    if (b + 48) * 1536 <= 120 * 2 ** 10:
        print(n)
