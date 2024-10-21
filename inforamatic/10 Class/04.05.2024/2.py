with open("17-2.txt") as f:
    a = [int(x) for x in f]

coun = 0
mas = 0
for i in range(len(a) - 1):
    if (a[i] % 2 == 0 and a[i+1] % 2 == 1) or (a[i] % 2 == 1 and a[i+1] % 2 == 0):
        coun += 1
        if a[i] % 2 == 0:
            mas += a[i]
        else:
            mas += a[i+1]
print(coun, mas)