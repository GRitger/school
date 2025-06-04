for i in range(10000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 1:
            M = M + (x % 10) // 2
        x = x // 10
    if L == 3:
        if M == 7:
            print(i)
