def f(x):
    d = 2
    while d * d <= x:
        if x% d == 0:
            return [d, x//d]
        d += 1

ch = 900000
n = 0
a = []
while n < 5:
    ch -= 1
    m = 0
    temp = f(ch)
    if temp:
        m = sum(temp)
    if m% 1000 == 112:
        a.append([ch, m])
        n += 1
a.sort()
print(*a)