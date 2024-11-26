from math import *

e = 24

for i in range(1,1000):
    if ceil(e*i/8) *5100 <= 170 * (2**10):
        print(2**i-62)