from functools import lru_cache
def g(x):
    if x % 2 ==0:
        return x-1,x-2,x //2
    return x-1,x-2

@lru_cache(None)
def f(x):
    if x <= 10:
        return "+"
    if any( f(i) == "+" for i in g(x)):
        return "p1"
    if all( f(i) == "p1" for i in g(x)):
        return "v1"
    if any( f(i) == "v1" for i in g(x)):
        return "p2"
    if all( f(i) in ["p1", "p2"] for i in g(x)):
        return "v2"

for i in range(11, 73):
    if f(i) == "v2":
        print(i, f(i))