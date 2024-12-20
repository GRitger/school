from itertools import *
a = []
for k in range(5):
    for i in product("0123456789", repeat=k):
        i = "".join(i)
        s = "12345"+i+"76"
        if int(s) < 10**10 and int(s) % 73 == 0:
            a.append(int(s))

a.sort()

print(a)
