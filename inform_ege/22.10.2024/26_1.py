with open ("26_1.txt") as f:
    n = int(f.readline())
    a = []
    hl = []
    kras = []
    for _ in range(1, n+1):
        x, y = [int(i) for i in f.readline().split() ]
        if x < y:
            hl.append([x, _])
        else:
            kras.append([y, _])

hl.sort()
kras.sort(reverse=True)
print(max(hl[-1][1], kras[0][1]))
if hl[-1][1] > kras[0][1]:
    print(hl[-1][1], len(hl)-1)
else:
    print(kras[0][1], len(hl))