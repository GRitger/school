with open ("hpn423kfk.txt") as f:
    a = []
    n = int(f.readline())
    for i in range(n):
        t1, t2, ch = f.readline().split()
        t1 = int(t1)
        t2 = int(t2)
        a.append([t1,t2,ch])

a.sort()

A = [0] * 100
B = [0] * 30

ans = 0
vs = 0

for i in a:
    t1, t2, ch = i
    if ch == "A":
        for j in range(100):
            if t1 >= A[j]:
                A[j] = t1 + t2
                vs += 1
                break
    else:
        for j in range(69, 100):
            if t1 >= A[j]:
                A[j] = t1 + t2
                vs += 1
                ans += 1
                break

print(ans, n -vs)