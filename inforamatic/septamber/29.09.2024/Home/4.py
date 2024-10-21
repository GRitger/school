a = []
for m in range(50):
    for n in range(50):
        if m % 2 == 0 and n % 2 == 1:
            if 100000000 < 2**m * 7**n < 300000000:
                a.append([2**m * 7**n, m+n])
a.sort()
print(*a)