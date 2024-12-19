from itertools import *
n= 0
for i in product("012345", repeat=6):
    i = "".join(i)
    f = True
    if i == "555425":
        qeoqkfq = 561
    for x in range(1, 5):
        if (i[x] in "135" and  (i[x-1] == "2" or i[x+1] == "2")) or (i[x] == "2" and i[x-1] in "135" or i[x+1] in "135") :
            f = False
            #print(i)
    if i[0]!="0" and f and  i.count("2") == 1:
        print(i)
        n+=1
print(n)