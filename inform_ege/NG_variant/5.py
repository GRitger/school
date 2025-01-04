def f(x, o):
    st = ""
    while x:
        st = str(x %o) + st
        x = x//o
    return st

def d(st):
    su = 0
    for i in st:
        su += int(i)
    return  su
a = []
for N in range(42, 100):
    s = str(d(f(N, 7)))
    while len(s) > 1:
        s = str(d(f(int(s), 7)))
    R = s
    s = str(d(f(N, 8)))
    while len(s) > 1:
        s = str(d(f(int(s), 8)))
    R = R + s
    if  R == "67":
        print(N)
