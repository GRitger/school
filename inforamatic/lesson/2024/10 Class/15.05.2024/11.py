def f (a, b):
    if a > b or a == 16:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 3, b) + f(a*a, b)
print(f(3, 20) * f(20, 26))










'''def f(a, b):
    if a > b or a == 17:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b)
print(f(1, 10) * f(10, 35))'''