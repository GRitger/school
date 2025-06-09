def f(a,b,k):
    if a > b:
        return 0
    if a == b and k != 3:
        return 1
    return f(a+2, b, 1) + f(a+5, b , 2) + f(a*a, b , 3)

print(f(4,36, 0))