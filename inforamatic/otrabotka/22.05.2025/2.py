def p(x:int):
    d = 2
    while d *d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def d(x:int):
    a = []
    d = 2
    while d *d < x:
        if x % d == 0:
            if p(d):
                a.append(d)
            if p(x//d):
                a.append(x//d)
        d += 1
    if d * d == x:
        if p(d):
            a.append(d)
    a.sort()
    return a


ans = []
ch = 9500000
n = 0
while n < 5:
    ch += 1
    temp = d(ch)
    sr = 0
    if len(temp) > 0:
        sr = sum(temp) // len(temp)
    if sr and sr % 813 == 0:
        ans.append([ch, sr])
        n +=1
ans.sort(key=lambda x : (x[1], x[0]))
for i in ans:
    print(*i)

