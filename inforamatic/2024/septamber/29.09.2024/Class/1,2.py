from itertools import *

for i in "0123456789":
    for j in "0123456789":
        s = "1" + i + "34567" + j + "9"
        if int(s) % 17 == 0:
            print(s, int(s)//4)
