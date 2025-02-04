from math import log2, ceil

i = log2(25+ 487)
for x in range(100000):
    if i * x * 345 > 70 * (2**13):
        print(x)
        break