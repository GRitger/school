from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 0 and n % 2 == 0:
        return f(n//10) + n% 10
    if n > 0 and n % 2:
        return f(n//10)
    return 0
for i in range(10**9):
    f(i)
c = 0
for i in range(10**9, 6 * 10**9):
    if f(i) == 2:
        c +=1
print(c)