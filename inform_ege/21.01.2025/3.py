with open("3.txt") as f:

    a = []
    for i in f:
        a.append(int(i))

ans = 0
ans2 = []
for i in range(len(a)-1):
    if (a[i]%3 == max(a)% 3) or a[i+1]%3 == max(a)% 3:
        if (a[i]%7 == min(a)% 7) or a[i+1]%7 == min(a)% 7:
            ans +=1
            ans2.append(a[i]+ a[i+1])

print(ans, max(ans2))