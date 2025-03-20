a = []
for N in range(1,10000):
    r = bin(N)[2:]
    if len(r) % 2 ==0:
        r = r +"1"
    else:
        r = "1"+r+"0"
    R = int(r,2)
    print(N, R)
    if R > 666:
        a.append(R)
print(min(a))