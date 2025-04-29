from math import *

l = 12
for x in range(1, 1000000):
    i = ceil(log2(26+26+10))
    b = ceil(i * l / 8)
    if (b +28) * x <= 20 * 2 ** 10:
        print(x)
