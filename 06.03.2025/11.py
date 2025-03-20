from math import  log2, ceil

for n in range(1, 20000000):
    i = ceil(log2(n))
    r = ceil(i * 317 /8)
    if r * 487321 > 130 * 2 **20:
        print(n)
        break