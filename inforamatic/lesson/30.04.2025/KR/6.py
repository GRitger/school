def f(x, m):
    if x >= 58:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x+1, m -1), f(x+4, m -1), f(x*2, m -1)]
    if m % 2:
        return any(h)
    else:
        return all(h)

for i in range(1, 58):
    if f(i, 4) and not(f(i,2)):
        print(i)