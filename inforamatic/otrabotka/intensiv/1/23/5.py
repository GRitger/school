arr = []
def f(a, k):
    if k > 13:
        return 0
    if k == 13 and a not in arr and a < 0:
        arr.append(a)
        return 1
    return f(a - 3, k + 1) + f(a * (-3), k + 1)

print(f(333, 0))