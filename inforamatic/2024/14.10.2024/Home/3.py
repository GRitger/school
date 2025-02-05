from itertools import*
for i in product("0123456789", repeat=3):
    i = "".join(i)
    for j in "01234567890":
        s = "13" + i + "57" + j + "9"
        if int(s) % 999 == 0:
            print(s, int(s) / 999)