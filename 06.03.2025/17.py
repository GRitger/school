with open("17.txt") as f:
    a = []
    for i in f:
        a.append(int(i))
    c_7= 0
    for i in a:
        if abs(i) % 10 == 7:
            c_7 += 1
c = 0
m = -100000000000000000000000000000000000000000000000000000000000
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if x*y < 0 and x + y <  c_7:
        c += 1
        m = max(x+y, m)
print(c, m)