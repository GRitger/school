from itertools import product
a = []
for k in range(0,5):
    if k == 1:
        continue
    for j in "0123456789":
        for j1 in product("0123456789", repeat=k):
            x = "".join(j1)
            for j2 in "0123456789":
                st = int("4" + j + "78" + x + "82" + j2 + '1')
                if st <= 10**11 and st % 25641 == 0 :
                    a.append(st)
a.sort()
for i in a:
    print(i, i // 3489)
