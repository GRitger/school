def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 2, b) + f(a + 3, b) + f(int(str(a) + "1"), b)
print(f(3, 12) * f(12, 25))
