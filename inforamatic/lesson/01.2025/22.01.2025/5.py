def f(x):
    st = ""
    while x:
        st = str(x%3) + st
        x //= 3
    return st   
a = []
for i in range(4, 100):
    r = f(i)
    if r[-2:] == "10":
        r = "2" + r
    else:
        r = "1" + r
    R = int(r, 3)
    if R > 130:
        a.append(i)
print(min(a))