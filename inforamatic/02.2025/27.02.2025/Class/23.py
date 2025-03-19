from functools import lru_cache

@lru_cache(None)
def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1
    if a % 6 == 0:
        return f(a - 1, b) + f(a // 2, b) + f(a // 3, b)
    elif a % 2 == 0 or a % 3 == 0:
        if a % 2 == 0:
            return f(a - 1, b) + f(a // 2, b)
        else:
            return f(a - 1, b) + f(a // 3, b)

    return f(a-1, b)

print(f(122, 57) * f(57, 11))