import math
for i in range(1,50):
    m = 256*2560*8
    if m * i //163840 <= 250:
        print(i)