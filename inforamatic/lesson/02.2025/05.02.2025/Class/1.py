from functools import lru_cache

def g(x):
    return x+1,x+2, x*3

@lru_cache(None)
def f(x):
    if x >= (74):
        return "+"
    if any(f(i)== "+" for i in g(x)):
        return "p1"
    if all(f(i)== "p1" for i in g(x)):
        return "v1"
    if any(f(i)== "v1" for i in g(x)):
        return "p2"
    if all(f(i) in ["p1", "p2"] for i in g(x)):
        return "v2"
    if any(f(i) in ["v1", "v2"] for i in g(x)):
        return "p3"
    if all(f(i) in ["p1", "p2", "p3"] for i in g(x)):
        return "v3"

for i in range(1, 73):
    print(i, f(i))