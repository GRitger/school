from functools import lru_cache
import sys

@lru_cache(None)
def r(x):
    s = 0
    while x:
        s += x % 10
        x = x//10
    return s

@lru_cache(None)
def f(a,b, n, h=0):
    if a < 11 or n > 1:
        return 0
    if a == b:
        print(h)
        return 1


    return f(a+r(a)*3,b,n+1, a)+f(a-r(a)*3,b,n+1, a)

print(f(65,32,0))