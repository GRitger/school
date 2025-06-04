from functools import lru_cache

@lru_cache(None)
def f(x,m):
    if x >= 31: return m%2==0
    if m == 0:
        return False
    h = [f(x+1, m-1), f(x+5, m-1), f(x *2, m-1)]
    if m % 2 :
        return any(h)
    else:
        return all(h)

for i in range(1, 31):
    if any(f(i, m) for m in range(3,31,2)) and not(f(i,1)):
            print(i)