from math import log2, ceil

for l in range(1, 10000):
    i = ceil(log2(900 + 10))
    if ceil(i*l /8) *1500 <= 780 * 2**10:
        print(l)