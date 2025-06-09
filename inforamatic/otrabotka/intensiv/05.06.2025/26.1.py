def prow(a):
    for i in a:
        if i[2]:
            return True
    return False

with open("26-549.txt") as f:
    a = []
    for i in f:
        q, t = i.split()
        if t == "A":
            t = 1
        else:
            t = 2
        a.append([int(q), t, True])

a.sort(key=lambda x :(x[0], x[1]), reverse=True)

while prow(a):
    for i in a:
        p = 0




for i in a:
    print(i)