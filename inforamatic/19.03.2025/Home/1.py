def f(x,x2,m):
    if x + x2 >= 73:
        return m %  2 == 0
    if m == 0:
        return False
    h = [f(x+1,x2, m-1), f(x,x2+1, m-1),f(x*2,x2, m-1),f(x,x2*2, m-1)]
    if m % 2:
        return any(h)
    else:
        return all(h)

print(f(7, 31,1))