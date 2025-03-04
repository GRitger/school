import math

for N in range(1,10000):
    i = math.ceil(math.log2(N))
    l = 20
    if math.ceil(i*20/8) *600000 > 11*2**20:
        print(N)
        break
