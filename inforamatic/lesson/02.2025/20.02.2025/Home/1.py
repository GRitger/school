from functools import lru_cache

def g(x):
    return x+2, x+4, x*3

@lru_cache(None)
def f(x):
    if x >= 82:
        return "+"
    if any(f(i)=="+" for i in g(x)):
        return "p1"
    if all(f(i) == "p1" for i in g(x)):
        return "v1"
    if any(f(i) == "v1" for i in g(x)):
        return "p2"
    if all(f(i) in ["p1","p2"] for i in g(x)):
        return "v2"

for i in range(1, 82):
    if f(i) == "v1":
        print(i, f(i))

for i in range(1, 82):
    if f(i) == "p2":
        print(i, f(i))

for i in range(1, 82):
    if f(i) == "v2":
        print(i, f(i))