from fnmatch import *
for i in range(30120145//1917*1917, 10**10, 1917):
    st = str(i)
    if fnmatch(st, "3?12?14*5"):
        print(i, i //1917)