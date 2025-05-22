from functools import lru_cache

def g(x):
    if x % 4 == 0:
        return  x-2, x-3, x//4
    else:
        return x-2, x-3

@lru_cache(None)
def f(x):
    if x < 32:
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

for i in range(32, 1000):
    if f(i) == "v1":
        print(i, f(i))

for i in range(32, 1000):
    if f(i) == "p2":
        print(i, f(i))

for i in range(32, 1000):
    if f(i) == "v2":
        print(i, f(i))