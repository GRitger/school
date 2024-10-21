def func(a, s, index, nomer):
    s -= a[index - nomer]
    for i in range(len(a) - 1, index, -1):
        if s + a[i] > max_s:
            continue
        else:
            s += a[i]
            break
    return s


with open("3.txt") as f:
    c, max_s = map(int, f.readline().split())
    a = []
    for i in f:
        a.append(int(i))
s = 0
col = 0
index = 0
for i in a:
    if 200 <= i <= 210:
        s += i
        col += 1
a.sort()
for i in range(len(a)):
    if 200 <= i <= 210:
        continue
    if s + a[i] > max_s:
        index = i - 1
        break
    else:
        s += a[i]
        col += 1

print(col)

for j in range(50):
    s = func(a, s, index, j)

print(s)
