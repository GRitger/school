from fnmatch import *
for i in range(103456709//17*17, 10**9, 17):
    st = str(i)
    if fnmatch(st, "1?34567?9"):
        print(i, i //17)