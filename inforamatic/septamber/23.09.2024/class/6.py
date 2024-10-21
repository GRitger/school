a = []
for m in range(40):
    for n in range(40):
        if m % 2 == 0 and n % 2 == 1:
            if 200000000 <=(2**m)*(3**n) <= 400000000:
                a.append((2**m)*(3**n))
a.sort()
print(*a)