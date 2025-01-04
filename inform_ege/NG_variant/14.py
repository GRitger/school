def f(x):
    st = ""
    while x:
        st = str(x%9) + st
        x //= 9
    return st



for i in range(2025):
    t = f(9 ** 2024 + 9 ** 1987-i)
    if t.count("8") == 1984:
        print(i)


