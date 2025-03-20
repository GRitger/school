def f(x):
    st = ""
    while x:
        st = str(x % 3) + st
        x = x // 3
    return st
a = []
for i in range(1, 1000):
    r = f(i)
    if r.count("1") % 2 == 0:
        r = r + "0"
        r = "12" + r[2:]
    else:
        r = r + "2"
        r = "10" + r[2:]
    R = int(r, 3)

    if R > 105:
        a.append(i)
print(min(a))