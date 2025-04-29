from itertools import  *
c = 0
for i in product("дгиашэ",repeat = 5):
    st = "".join(i)
    if st[0] in "дгш" and st[-1] in "иаэ":
        c += 1
print(c)
