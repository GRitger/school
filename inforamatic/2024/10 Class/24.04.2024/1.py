def f(a, b):
    if a > b or a == 8:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(2 * a, b) + f(3* a, b)
print(f(3,9) * f(9, 23))