def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True
s =1
co = 0
ch = 0
while co < 9:
    ch += 1
    if p(ch):
        s *= ch
        co+=1
print(s,ch)
