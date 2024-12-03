import math
with open("5.csv") as f:
    n = 0
    k = 0
    for i in f:
        k+=1
        a = [int(x) for x in i.split(";")]
        a3 = [x for x in a if a.count(x) == 2]
        if len(a3) == 6 or int(math.sqrt(sum(a)/7)) == math.sqrt(sum(a)/7):
            n += 1
print(n)