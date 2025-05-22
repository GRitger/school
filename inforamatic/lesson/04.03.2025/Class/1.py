def f(x, m):
    if  x < 20:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(x-10,  m-1), f(x//2,  m-1)]
    if m  % 2:
        return any(h)
    else:
        return all(h)

for i in range(20, 200):
    if f(i , 4):
        print(i, end=" ")
