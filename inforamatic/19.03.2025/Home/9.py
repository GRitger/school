def f(x, x2, m):
    if x + x2 >= 152:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x +3, x2, m - 1), f(x, x2 +3, m - 1), f(x * 3, x2, m - 1), f(x, x2 * 3, m - 1)]
    if m % 2:
        return any(h)
    else:
        return all(h)


for i in range(1, 139):
    if f(13,i,4) and not(f(13,i,2)):
        print(i)
