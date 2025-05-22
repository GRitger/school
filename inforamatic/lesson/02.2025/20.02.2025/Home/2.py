from functools import lru_cache

def g(x):
    return x+1, x+3, x*4

@lru_cache(None)
def f(x):
    if x >= 211:
        return "+"
    if any(f(i)=="+" for i in g(x)):
        return "p1"
    if all(f(i) == "p1" for i in g(x)):
        return "v1"
    if any(f(i) == "v1" for i in g(x)):
        return "p2"
    if all(f(i) in ["p1","p2"] for i in g(x)):
        return "v2"
    if any(f(i) in ["v1","v2"] for i in g(x)):
        return "p3"

for i in range(1, 211):
    if f(i) == "v1":
        print(i, f(i))

for i in range(1, 211):
    if f(i) == "v2":
        print(i, f(i))

for i in range(1, 211):
    if f(i) == "p3":
        print(i, f(i))