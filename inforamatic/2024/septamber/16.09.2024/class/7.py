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
    a = []
    d = 1
    while d * d < x:
        if x % d == 0:
            a.append(d)
            a.append(x // d)
        d += 1
    if d * d == x:
        a.append(d)
    a.sort()
    return a


ans =0
ans_c = 0
ma = 1000000000000000000000000000
for i in range(309829, 365874 + 1):
    d = 2
    while d * d < i:
        if i % d == 0 and p(d) and p(i // d):
            if i//d - d < ma:
                ma = i//d - d
                ans = d
                ans_c = i // d
        d += 1
print(ans, ans_c)
