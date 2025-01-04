def p(x):
    d = 2
    flag = True
    while d*d<= x:
        if x % d ==0:
            return False
        d+=1
    return True

def f(x):
    a = []
    d = 2
    while d*d< x:
        if x % d ==0:
            a.append(d)
            a.append(x//d)
        d+=1
    if d*d==x:
        a.append(d)
    a.sort()
    return a

n = 0
qwe = 10000000
while n < 5:
    qwe += 1
    temp = f(qwe)
    if len(temp)>=3:
        S = temp[-1]+ temp[-2] +temp[-3]
        if p(S):
            n += 1
            print(S, qwe)
