def f(x, m):
    if x <= 40:
        return m % 2 == 0
    if m ==0 :
        return False
    h = [f(x-2, m -1), f(x-4, m -1), f(x //3, m -1)]
    if m % 2:
        return any(h)
    else:
        return all(h)

for i in range(41, 200):
    if not f(i, 2) and f(i,4):
        print(i)