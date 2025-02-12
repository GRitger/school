def d(x,y):
    if x % y == 0:
        return 1
    else:
        return 0


for A in range (1, 300):
    flag = True
    if A == 172:
        wrk= 254
    for x in range(1, 1000):
        f = (d(x,14) <= (not(d(x,4)))) or (x + A >= 200)
        flag *= f
    if flag:
        print(A)
