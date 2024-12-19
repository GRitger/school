from itertools import *
a = [i for i in range(25)]
n= 0
for i in product(a, repeat=4):
    c = 0
    t = 0
    for j in i:
        if j % 2 ==0:
            c +=1
        if j>15:
            t += 1
    if c == 1 and t <= 2 and i[0] != 0:
        n+=1
print(n)