with open("26_1.txt") as fal:
    N = int(fal.readline())
    mas_l = [int(i) for i in fal]
mas_l.sort(reverse=True)
col = 1
pred = mas_l[0]
for i in mas_l:
    if i <= pred-3:
        pred = i
        col += 1
        print(i)
print(col, pred)