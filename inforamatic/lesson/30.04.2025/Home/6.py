def f(x, m):
    if x <= 87:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x-2, m -1), f(x//2, m -1)]
    if m % 2:
        return any(h)
    else:
        return all(h)

for i in range(89, 200):
    if f(i, 4) and not(f(i,2)):
        print(i)