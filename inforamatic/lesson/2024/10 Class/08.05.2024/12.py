count = 0
for i in range(0, 100000, 2):
    s = i
    n = 160
    while s > 0:
        s = s // 8
        n = n - 8
    if n == 144:
        count += 1
print(count)