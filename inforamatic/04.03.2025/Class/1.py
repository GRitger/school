def f(x1, x2, m):
    if x1 + x2 >= 65:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x1+1, x2, m-1), f(x1*3, x2, m-1),f(x1, x2+1, m-1),f(x1, x2*3, m-1)]
    if m  % 2:
        return any(h)
    else:
        return any(h)

for i in range(1, 59):
    if f(6, i , 2):
        print(i, end=" ")
