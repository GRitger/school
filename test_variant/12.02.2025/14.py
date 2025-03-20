def f(x):
    st = ""
    while x:
        st = str(x % 5) + st
        x = x // 5
    return st

for x in range(2736):
    ch = f(5**2025 + 5**1500 - x)
    if ch.count("0") == 527:
        print(x)