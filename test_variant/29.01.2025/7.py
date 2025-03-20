from math import log2

i = log2(65536)
R = i * 3840*2160
for x in range(100000):
    if R *x <= 16 * (2**33):
        print(x)