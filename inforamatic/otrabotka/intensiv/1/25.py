from fnmatch import fnmatch
def f (x):
    s = 0
    while x:
        s += x %10
        x //= 10
    return s


a = []
for i in range(8587,10**9, 8587):
    if fnmatch(str(i), "?05*22*3") and i % 8587 == 0:
        a.append([i, f(i)])
a.sort(key=lambda x :(x[1], x[0]))
for i in a:
    print(*i)