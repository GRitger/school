from functools import lru_cache


def g(x):
    return x + 2, x * 3


@lru_cache(None)
def f(n, x=5):
    if x >= n:
        return "+"
    if any(f(n, i) == "+" for i in g(x)):
        return "p1"
    if all(f(n,i) == "p1" for i in g(x)):
        return "v1"
    if any(f(n,i) == "v1" for i in g(x)):
        return "p2"
    if all(f(n,i) in ["p1", "p2"] for i in g(x)):
        return "v2"
    if any(f(n,i) in ["v1", "v2"] for i in g(x)):
        return "p3"
    if all(f(n,i) in ["p1", "p2", "p3"] for i in g(x)):
        return "v3"


for i in range(20, 131):
    if f(i) == "v2":
        print(i, f(i))
