from itertools import product

count = 0
st = "01234567"
for i in product(st, repeat=7):
    x = "".join(i)
    ch = 0
    for j in x:
        if j in "02468":
            ch += 1

    sem = 0
    for j in range(len(x)):
        if x[j] in "135":
            x = x.replace(x[j], "a")

    if x[0] != "0" and ch == 2 and x.count("a7") ==0 and x.count("7a") == 0 and x.count("77") == 0 :
        count += 1
print(count)
