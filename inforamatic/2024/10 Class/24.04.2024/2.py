def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    if a % 2 == 0:
        return f(a - 1, b) + f(a // 2 , b)
    else:
        return f(a - 1, b)
print(f(16,5) * f(5, 3))