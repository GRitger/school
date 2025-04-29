def qwe(a):
    for i in range(len(a)):
        if a[i][1]:
            return i

with open ("26-101.txt") as f:
    n, k= [int (i) for i in f.readline().split()]
    a = []
    for i in f:
        i = i[:-1]
        a.append([int(i),True])

a.sort(reverse=True)
ans1 = 0
ans2 = 0
while n > 0:
    ind = qwe(a)
    c = 1
    n -=1
    ans1 +=1
    for i in range(ind+1,len(a)):
        if a[ind][0] >= a[i][0] + k and a[i][1]:
            a[i][1] = False
            a[ind][1] = False
            n -=1
            c += 1
            ind = i
        ans2 = max(c, ans2)
print(ans1,ans2)