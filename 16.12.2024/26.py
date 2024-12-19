from operator import index

with open("26.txt") as f:
    n = int(f.readline())
    a = []
    for i in range(n):
        t = [int(x) for x in f.readline().split()]
        a.append(t)

a.sort(key=lambda x : x[0])
s = 0
for i in a:
    s += i[1]
s = s/len(a)
print(s)

qw = []
for i in a:
    if i[1] > s:
        qw.append(i)
#арикул, цена, остаток
qaz =[[0,0,0]]
print(qaz)
for i in qw:
    for j in qaz:
        if j[0] == i[0]:
            if i[2] == 0:
                j[2] -= 1
            else:
                j[2] += 1


