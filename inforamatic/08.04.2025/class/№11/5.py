from math import *

l = 261
for n in range(1, 1000000):
    i = ceil(log2(n))
    b = ceil(i*l/8)
    if b * 252500    <= 31 * 2 ** 20:
        print(n)