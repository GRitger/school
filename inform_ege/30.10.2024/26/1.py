with open("i8rvpGJ_d.txt") as f:
    a = []
    k = int(f.readline())
    n = int(f.readline())
    for i in range(n):
        t1, t2 = [int(x) for x in f.readline().split()]
        a.append([t1, t2])
a.sort(key=lambda x: x[0])

mas = [0] * (k+1)
count = 0
for i in a:
    t1, t2 = i
    for j in range(1, k+1):
        if t1 > mas[j]:
            count += 1
            mas[j] = t2
            ans = j
            break
print(count, ans )

