def f(a, b):
    if a == b:
        return 1
    if a < b or a == 10:
        return 0

    if a % 3 == 0:
        return f(a-2, b) + f(a// 3, b)
    else:
        return f(a-2, b) + f(a-4, b)

print(f(38, 6))
