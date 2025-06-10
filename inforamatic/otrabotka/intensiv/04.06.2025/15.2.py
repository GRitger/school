p = [x for x in range(128764, 775637+1)]
q = [x for x in range(280932, 894567+1)]
r = [x for x in range(754683, 929871+1)]
a = []
for x in range(1,10000000, 4):
    f = (not(x in a) <= (((x in p)==(x in q)) <= ((x in r) == (x in q))))
    if not f:
        print(x)