with open("13c.txt") as f:
    a = [int(x) for x in f]
ma = 10**10
for i in a:
    if i > 0:
        ma = min(ma, i)

coun = 0
mas = 10**10
for i in range(len(a) - 4):
    if a[i] % 111 != ma and a[i+1] % 111 != ma and a[i+2] % 111 != ma and a[i+3] % 111 != ma :
        coun += 1
        mas = min(a[i] + a[i+1] + a[i+2] + a[i+3], mas)
print(coun, mas)
