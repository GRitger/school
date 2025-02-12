a = []
for N in range(1, 1000):
    q = bin(N)[2:]
    if N % 2 == 0:
        q = q.replace("1", "11")
    else:
        q = q.replace("0", "00")
    R = int(q,2)
    if R < 70 and R != N:
        a.append(N)

print(max(a))