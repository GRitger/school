from itertools import*
for k in range(3):
    for i in product("0123456789", repeat=k):
        i = "".join(i)
        for j in "0123456789":
            if int("12" + i +"4" + j + "65") % 161 == 0 and int("12" + i +"4" + j + "65") <= 100000000 :
                print("12" + i +"4" + j + "65", int("12" + i +"4" + j + "65") /161 )
