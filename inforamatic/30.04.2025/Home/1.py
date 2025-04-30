def f(x):
    a = []
    d = 2
    while d * d <= x:
        if x % d ==0:
            a.append(d)
            a.append(x//d)
        d += 1
    a.sort()
    return a

ch = 800000
n = 0
while n < 5:
    ch += 1
    temp = f(ch)
    flag = 0
    ans = 0
    for i in temp:
        if i!= 9 and i % 10 == 9:
            flag = True
            ans = i
            break
    if flag:
        print(ch, ans)
        n  += 1
