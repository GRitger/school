def f(x):
    st = ""
    while x:
        st = str(x%3) + st
        x = x // 3
    return st

a = []
for N in range(10, 1000):
    r = f(N)
    if N % 4 == 0:
        r = r + r[-3:]
    else:
        r = "1" + r + "20"
    R = int(r, 3)
    if R > 423:
        a.append(R)
print(min(a))