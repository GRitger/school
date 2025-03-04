def f(x):
    st = ""
    while x:
        st = str(x%9) + st
        x = x //9
    return st
m = -1
ans = 0
for i in range(1, 2000):
    qwe = f(9**250 + 9**150 - i)
    if qwe.count("1") >= m:
        m = qwe.count("1")
        ans = i
print(ans)