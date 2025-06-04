def f(x, x2, m):
    if x + x2 >= 38:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x +1, x2, m - 1), f(x, x2 +1, m - 1), f(x * 2, x2, m - 1), f(x, x2 * 2, m - 1)]
    if m % 2:
        return any(h)
    else:
        return all(h)
print(f(8,13,4))
"""
for i in range(1, 139):
    if f(13,i,4) and not(f(13,i,2)):
        print(i)"""
