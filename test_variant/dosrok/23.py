def f(a,b):
    if a > b or a == 35 :
        return 0
    if a == b:
         return 1
    return f(a+1, b) + f(a+2, b) + f(a*2, b)

print(f(7,13) * f(13, 15) * f(15, 51))