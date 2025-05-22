from functools import lru_cache

@lru_cache(None)
def f(x,m):
    if 36 <= x: return m%2==0
    if m == 0:
        return False
    h = [f(x+1, m-1)]
    if x * 2 <= 60:
        h.append(f(x*2, m-1))
    if x * 3 <= 60:
        h.append(f(x*3, m-1))
    if m % 2 !=0 :
        return any(h)
    else:
        return all(h)

for i in range(1, 36):
    if f(i,4) and not(f(i,2)):
        print(i)