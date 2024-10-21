with open("13_4.txt") as f:
    a = [int(x) for x in f]
#a = [5, 25, 125, -5, 1, 4]
coun = 0
mas = 10**100
for i in range(len(a) - 1):
    c = 0
    if abs(a[i]) % 5 == 0 and abs(a[i]) % 3:
        c += 1
    if abs(a[i+1]) % 5 == 0 and abs(a[i+1]) % 3:
        c += 1
    if c == 2:
        coun += 1
        if (a[i] + a[i+1]) > 0:
            mas = min((a[i] + a[i+1]), mas)
print(coun, mas)
