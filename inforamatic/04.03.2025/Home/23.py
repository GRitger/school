def f(a,b,c):
    if a > b:
        return 0
    if a == b:
        return 1
    if a % 2 and c <= 5:
        return f(a*2,b, c+1) + f(a+3,b,c)
    else:
        return f(a * 2 +1, b, c) + f(a + 3, b, c)
print(f(1,76,0))