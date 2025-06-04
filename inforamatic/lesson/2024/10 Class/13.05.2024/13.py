with open("13.txt") as f:
    a = [int(x) for x in f]
ma = 0
for i in a:
    if abs(i) % 10 == 3:
        ma = max(ma, i)

coun = 0
mas = 0
for i in range(len(a) - 1):
    c = 0
    if abs(a[i]) % 10 == 3:
        c += 1
    if abs(a[i+1]) % 10 == 3:
        c += 1
    if c == 1 and (a[i]**2 + a[i+1] **2) >= ma **2 :
        coun += 1
        mas = max((a[i]**2 + a[i+1] **2), mas)
print(coun, mas)
