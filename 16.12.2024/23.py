def f (a,b,d):
    if a > b or a == 30:
        return 0
    elif a == b:
        return 1
    else:
        return f(a+d,b,d)+f(a*2,b, d)

s = 0
for i in range(1,10):
    s += f(1,10, i)*f(10,100,i)
print(s)