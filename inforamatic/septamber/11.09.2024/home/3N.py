def p(x):
    if x == 1:
        return False
    d = 2
    while d*d<=x:
        if x%d==0:
            return False
        d+=1
    return True

def f(x):
    a = []
    if x == 1:
        return 1
    d = 2
    k = 0
    while d*d<x:
        if x%d == 0:
            if p(d):
                k+=1
                a.append(d)
            if p(x//d):
                k+=1
                a.append(x//d)
        d+=1
    if d*d==x:
        if p(d):
            k+=1
            a.append(d)
    a.sort()
    return k, a

#print(f(15))

for i in range (25317, 51238):
    s = []
    x, s = f(i)
    if x >= 6:
        print(i, max(s), s)