from math import ceil, log2

for x in range(1,1000000000):
    r = 3840*2160 * ceil(log2(x)) * 60 * 90 + 48000 *16 * 2 * 90

    if r // 8 <= 54691875 * (2 ** 10):
        print(x)
