a = 4
b = 5

for i in range(1, 400):
    if i % 2:
        a -=1
        b += 2
    else:
        a += 2
        b -= 1
    print(i, a,b)