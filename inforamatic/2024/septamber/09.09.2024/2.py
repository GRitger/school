def f(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

nomer =1
ans = []
for i in range(2532000, 2532160 + 1):
    temp = f(i)
    if temp:
        ans.append(i)

for i in range(0, len(ans), 3):
    print(i+1, ans[i])
