def f(a,b, k):
    if a > b or a in k:
        return 0
    if a == b:
        return 1
    return f(a+1, b, k) + f(a+4, b, k) + f(a*2, b,k)

print(f(1,8,[16,32])* f(8, 50, [16, 32]) + f(1,16,[8,32])* f(16, 50, [8, 32]) + f(1,32,[16,8])* f(32, 50, [16, 8]))