def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x :
        if x % d == 0:
            return False
        d += 1
    return  True

def f(x):
    a = []
    d = 2
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d *d ==x:
        a.append(d)
    a.sort()
    return a

n = 0
ch = 1010101010
while n < 4:
    ch += 1
    temp = f(ch)
    st = str(ch)
    flag = True
    if len(temp):
        if temp[-1] % 7 == 0:
            if st == st[::-1]:
                for i in range(len(st)-1):
                    if (int(st[i]) % 2 == 0 and int(st[i+1]) % 2 == 1) or (int(st[i]) % 2 == 1 and int(st[i+1]) % 2 == 0):
                        pass
                    else:
                        flag = False
            else:
                flag = False
        else:
            flag = False
    else:
        flag = False

    if flag:
        print(ch, temp[-1])
        n += 1

