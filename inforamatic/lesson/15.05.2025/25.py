def prost(x):
    d = 2
    while d*d <= x:
        if x%d == 0:
            return True
        d += 1
    return False

def dl(x):
    d = 2
    a = []
    while d *d < x:
        if x% d == 0:
            if prost(d):
                a.append(d)
            if prost(x//d):
                a.append(x//d)
        d += 1
    if d *d == x:
        if prost(d):
            a.append(d)
    a.sort()
    return a

ch = 987_653
n = 0
while n < 5:
    ch -= 1
    temp = dl(ch)
    r = sum(temp)
    if r % 10 == 7:
        print(ch)
        n += 1