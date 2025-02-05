for i in range(1000):
    x = i
    a, b = 1, 1
    while x >= 1:
        if x % 5 >= 2:
            a += x % 5
        else:
             b *= x % 5
        x //= 5
    if a == 6 and b == 0:
        print(i)