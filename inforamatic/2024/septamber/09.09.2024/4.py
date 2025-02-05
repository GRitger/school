def p(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def f(x):
    d = 2
    a = []
    while d * d < x:
        if x % d == 0 and p(d) and p(x // d):
            return True
        d += 1
    return False


ans = []
nomer = 1
#print(f(17))

for i in range(125697, 190234 + 1):
    temp = f(i)
    if temp:
        ans.append(i)
print(len(ans),ans[-1])
