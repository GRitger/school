from functools import lru_cache
import sys

sys.setrecursionlimit(100000000)
print(sys.getrecursionlimit())

@lru_cache(None)
def r(x):
    s = 0
    while x:
        s += x% 10
        x = x//10
    return s

@lru_cache(None)
def f(a,b, n):
    if a <= 11 or n > 999:
        return 0
    if a == b:
        return 1
    return f(a+r(a)*3,b,n+1)+f(a-r(a)*3,b,n+1)

print(f(65,11,0))